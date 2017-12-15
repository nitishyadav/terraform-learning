######################################################################################################
# Author : Nitish K Yadav                                      #
# Desc   : Script is written to create a SSH key in IBM cloud  #
# Parametrs:As of now taking through command line arguments
######################################################################################################

from terrascript import *
from terrascript.softlayer.r import *
import json
import os
import sys
import logging

keyname = sys.argv[1]
publickey_path = sys.argv[2]

provider('softlayer')

softlayer_ssh_key('test_ssh_key', label = 'test_ssh_key_name', public_key = '${file('+'"'+publickey_path+'"'+')}')

jsonstr = dump()
jsonobj = json.loads(jsonstr)

with open("softlayer-ssh.tf.json",'w')as outfile:
    json.dump(jsonobj,outfile)

print(dump())
#python3.6 createssh.py test_ssh_key '/home/cloud_user/.ssh/id_rsa.pub'
