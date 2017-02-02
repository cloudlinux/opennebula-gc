# OpenNebula Garbage Collector

A lib/cli tool that allows to cleanup a certain resources older than a given  
timeout in OpenNebula cloud.

Tested with OpenNebula version 4.X.  
Works via OpenNebula XML-RPC bindings:  
https://github.com/python-oca/python-oca

Supported resources:
* VMs
* Blocked IPs (basing on VM metadata)

Blocked IPs are taken from `reserved_ips` VM metadata attribute, expected to  
be comma-separated string like: `XX.XX.XX.XX,YY.YY.YY.YY`. They are cleaned  
through `vn.release`. This part of GC is ignored if attribute is missing.


## Installation
```
git clone https://github.com/cloudlinux/opennebula-gc.git && cd opennebula-gc
# You may want to use venv here
python setup.py install 
``` 

## Usage
Command line:
```
opennebula-gc clean \
    --outdated-hours 2 \
    --network $ON_CI_NETWORK \
    --endpoint $ON_API_URL \
    --user $ON_USER \
    --password $ON_PASSWORD
```
Python import:
```
from opennebula_gc import clean_opennebula
```

## Related projects:
AWS Garbage Collector: https://github.com/cloudlinux/aws-gc
