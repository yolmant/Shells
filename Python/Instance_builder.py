#!/usr/bin/python

#you should have already installed boto3 to make this program works. 
#to install boto3: yum -y install python-pip; pip install boto3

import boto3,pprint,base64

tk = boto3.resource('ec2')

keyP= raw_input('Introduce you key_pair: \n')	#key pair that the server will use to run
Seg= str(raw_input('Introduce the security group: \n'))	#the firewall that your server will use to allow or deny inbounds
image = raw_input('Introduce your image: \n')  #runing with red hat server for example ami-6f68cf0f

Type = 't2.micro'	#Type of linux using, in this case amazon linux
firewall=[Seg]	
Data="""#!/usr/bin/python
import os,sys

print('installing git')
os.system('yum -y install git')
print('clone the reposotory from github')
os.system('git clone https://github.com/yolmant/Shells.git /home/ec2-user/Shells')

sys.path.append('/home/ec2-user/Shells/Python')

import function

function.ApacheI()

function.DjangoI()

function.IpAccessI()

#activate the django environment and run the server
os.system('source /opt/django/django-env/bin/activate; python /opt/django/project1/manage.py runserver 0.0.0.0:8000')"""

def VM():
	#create the instance
	instances = tk.create_instances(
		ImageId = image,
		InstanceType = Type,
		MinCount = 1,
		MaxCount = 1,
		KeyName = keyP,
		SecurityGroupIds = firewall,
		UserData = Data

		)
	
	pprint.pprint(instances)

VM()
print('\nInstance has been created')
print(image)
print(Type)
print(keyP)
print(firewall)
