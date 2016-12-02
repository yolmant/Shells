#!/usr/bin/python
import os

print('installing git')
os.system('sudo yum -y install git)

url= raw_input('introduce you URL from github').lower()
os.system('git clone '+url)


