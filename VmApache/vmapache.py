from terrascript import *
from terrascript.softlayer.r import *
from terrascript.softlayer.d import *
import json
import os
import sys
import logging


logging.basicConfig(filename= 'VmApachelogs.log', level=logging.DEBUG)
logging.debug('These message should go to the log file')
logging.info('So should this')
logging.warning('And this ,too')

#Variables

servername=sys.argv[1]
domain_id=sys.argv[2]
region_id=sys.argv[3]
image_id=sys.argv[4]
cpu_cores=sys.argv[5]
ram_memory=sys.argv[6]
key_path=sys.argv[7]
source_path_script=sys.argv[8]
source_path_property=sys.argv[9]


provider('softlayer')
logging.info('cloud provider:Softlayer')

#Establishing the connection
logging.info('establishing connection using the ssh key')
conn = connection(type='ssh',user='root',private_key='${file('+'"'+key_path+'"'+')}')
logging.info('connection established using the private key')
#conn = connection(type='ssh', user = 'root', password= '$(var.root_password}')


#Provisioning what is needed-- installing httpd
prov0 = provisioner('file',source = source_path_script, destination='/tmp/apache.sh',connection=conn)
logging.info('apache.sh script copied to the server')
prov1 = provisioner('file',source = source_path_property, destination='/tmp/user.properties',connection=conn)
logging.info('property file copied to the server')

prov = provisioner('remote-exec',inline =['chmod +x /tmp/apache.sh' ,'chmod +x /tmp/user.properties','/tmp/apache.sh',connection = conn)
logging.info('executing the properties files copied to the server')

#creation of the VM
logging.info('VM creation in softlayer is started')
softlayer_virtual_guest('softlayer-instance',hostname = servername,domain = domain_id,datacenter = region_id, network_speed = 100,hourly_billing= True, os_reference_code = image_id,cores = cpu_cores,memory = ram_memory,local_disk = True,ssh_key_ids = ['${data.softlayer_ssh_key.es_key.id}'], provisioner=[prov0,prov1,prov])

#passibng the dump in a variable
jsonstr = dump()
jsonobj = json.loads(jsonstr)

#writing to a tf.json file
with open("Vmapache.tf.json",'w')as outfile:
    json.dump(jsonobj,outfile)

logging.info('Dumping the output to the screen')

#printing the dump on the screen
print(dump())
