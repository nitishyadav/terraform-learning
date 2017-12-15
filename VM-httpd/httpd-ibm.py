from terrascript import *
from terrascript.softlayer.r import *
import json
import os
import sys
import logging

logging.basicConfig(filename= 'testlogs.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this ,too')

#the Cloud Provider--IBM Cloud
provider('softlayer')
logging.info('cloud provider:Softlayer')


#Establishing the connection
#conn = connection(type='ssh',user='root',private_key='${file("/home/cloud_user/.ssh/id_rsa")}')
conn = connection(type='ssh', user = 'root', password= '$(var.root_password}')


#Provisioning what is needed-- installing httpd
prov = provisioner('remote-exec',inline = ['sudo apt-get -y update','sudo apt-get -y apache2'],connection = conn)

#creation of the VM
logging.info('VM creation in softlayer is started')
softlayer_virtual_guest('softlayer-instance',name = 'soft-apache',domain = 'ibm.com',region = 'che01', public_network_speed = 10,hourly_billing= True, image = 'UBUNTU_14_64',cpu = 1,ram = 1024,local_disk = True, provisioner = prov)

#passibng the dump in a variable
jsonstr = dump()
jsonobj = json.loads(jsonstr)

#writing to a tf.json file
with open("softlayerVM.tf.json",'w')as outfile:
    json.dump(jsonobj,outfile)

logging.info('Dumping the output to the screen')

#printing the dump on the screen    
print(dump())
