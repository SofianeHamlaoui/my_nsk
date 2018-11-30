
import os
import sys
import subprocess
import ./mac_lookup as mac


def output(file):
    #output = subprocess.check_output([sys.executable, './my_nsk.py'])
    file_obj = open(file,"a+")
    file_obj.write(mac.company)

