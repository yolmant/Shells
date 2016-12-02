#!/usr/bin/python
import os

print('installing git')
os.system('sudo yum -y install git')

Url= raw_input('introduce you URL from github ').lower()
os.system('git clone '+Url)


