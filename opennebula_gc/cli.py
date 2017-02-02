import sys
import argparse

from opennebula_gc import clean_opennebula


def cli():
    parser = argparse.ArgumentParser(
        prog="Clean OpenNebula Resources",
        description="CLI tool to clean outdated resources in OpenNebula")

    commands = parser.add_subparsers(
        title="Commands",
        dest="command")

    cmd_clean = commands.add_parser(
        "clean",
        help="Delete outdated resources",
        description="Delete outdated resources in OpenNebula cloud")
    cmd_clean.set_defaults(func=clean_opennebula)

    cmd_clean.add_argument(
        "-O", "--outdated-hours", default=2, dest='hours')
    cmd_clean.add_argument(
        "-n", "--network", dest='network')
    cmd_clean.add_argument(
        "-H", "--endpoint", dest="nebula_endpoint")
    cmd_clean.add_argument(
        "-u", "--user", dest="user")
    cmd_clean.add_argument(
        "-p", "--password", dest="pwd")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


def main():
    args = cli()
    args.func(
        hours=args.hours,
        network=args.network,
        user=args.user_name,
        pwd=args.pwd,
        endpoint=args.nebula_endpoint,
    )
