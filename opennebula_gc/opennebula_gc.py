# Initial author: Dmitry Tyzhnenko <t.dmitry@gmail.com>

import datetime
import oca


def clean_opennebula(hours, network, user, pwd, endpoint):
    now = datetime.datetime.utcnow()
    delta = datetime.timedelta(hours=hours)
    client = oca.Client(
        '{user}:{pwd}'.format(user=user, pwd=pwd),
        'https://{host}:2633/RPC2'.format(host=endpoint))
    vms = oca.VirtualMachinePool(client)
    vms.info()
    vns = oca.VirtualNetworkPool(client)
    vns.info()
    net = vns.get_by_name(network)
    net.info()
    to_delete = []
    print("{uid:<6} {name:10} {started}".format(
        uid="#", name="Name", started="Started"))
    for vm in vms:
        text = "{uid:<6} {name:10} {started!s:10}".format(
            uid=vm.id,
            name=vm.name,
            started=datetime.datetime.fromtimestamp(vm.stime))
        print(text)
        if now - datetime.datetime.fromtimestamp(vm.stime) > delta:
            to_delete.append(vm)

    for vm in to_delete:
        # Release cluster IP on hold, if any
        if getattr(vm.user_template, 'reserved_ips', None):
            ips = vm.user_template.reserved_ips.split(',')
            for ip in ips:
                text = "{} IP on hold - released".format(ip)
                print(text)
                client.call(
                    'vn.release', net.id,
                    'LEASES=[IP={}]'.format(ip))
        # Delete VM
        text = "{uid:<6} {name:10} {started!s:10} - deleted".format(
            uid=vm.id,
            name=vm.name,
            started=datetime.datetime.fromtimestamp(vm.stime))
        print(text)
        vm.delete()
