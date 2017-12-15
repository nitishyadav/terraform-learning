from terrascript import *
from terrascript.softlayer.r import *
import json
import os
import sys
import logging

#command line argument
servername=sys.argv[1]
domain_id=sys.argv[2]
region_id=sys.argv[3]
image_id=sys.argv[4]
cpu_cores=sys.argv[5]
ram_memory=sys.argv[6]


#provider('softlayer',username = 'IBM1503401', api_key = 'b6d678df4b74421d1b360c0b76c7fba263b1021ec093585589a67e3bfa5e9037')
provider('softlayer')

softlayer_virtual_guest('softlayer-instance',hostname = servername,domain = domain_id,datacenter = region_id, network_speed = 100,hourly_billing = True,os_reference_code = image_id,cores = cpu_cores,memory = ram_memory,local_disk = True)
#softlayer_virtual_guest('softlayer-instance',name = 'softlayer-instance',domain = 'ibm.com',region = 'che01', public_network_speed = 10,hourly_billing= True,image = 'UBUNTU_14_64',cpu = 1,ram = 1024,local_disk = True)



jsonstr = dump()
jsonobj = json.loads(jsonstr)

with open("softlayerVM.tf.json",'w')as outfile:
    json.dump(jsonobj,outfile)

print(dump())

#python3.6 createvm.py softlayer-instance 'ibm.com' che01 'UBUNTU_14_64' 1 1024
