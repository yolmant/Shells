#!/usr/bin/python
import os, subprocess

#function to instal Apache server
def ApacheI():

	print('\ninstalling Apache serve\n')
	os.system('sudo yum -y install httpd')
	print('enabling Apache server\n')
	os.system('sudo systemctl enable httpd.service')
	print('Staring Apache server\n')
	os.system('sudo systemctl start httpd.service\n')
	print('open the security setting for port 80 in your server, to observer the Apache server working')

#function to verify COW
def CowI():

	print('appling verification of COW in kernel.\n')
	os.system('sudo rpm -q --changelog kernel | grep CVE-2016-5195')

#function to install github(you will be able to introduce the URL for your github reponsotory
def GithubI():

	print('intalling Git\n')
	os.system('sudo yum -y install git')
	Url=raw_input('introduce you URL from GitHub:\n').lower()
	os.system('git clone '+Url)

#fuction to create a croned message that will send you a text every hour to check the activity in the server
def CronI():

	#Shell with the message that will be sent every hour
	#Ask to the user what the email is to send the message
	Email=raw_input('Introduce your email: \n').lower()
	#Allow the user introduce the name of the file and it will be in home directory
	file=raw_input('Introduce the name of the Shell script: \n')
	#create the file that will be croned
	os.system('sudo echo "new" >> /home/ec2-user/'+file+'.bash')
	#open the file with python
	Ifile= open('/home/ec2-user/'+file+'.bash', 'w')
	#write into the file
	Ifile.write("""#!/bin/bash

Users=$(/usr/bin/who | grep -c "")
System=$(uname)
time=$(cut -f1 -d\| /proc/uptime)
message="the machine with system ${System} is ON with ${Users} user logged in. There is not activity. Please stop the VM"

if [ $Users -eq 0 ] && [ $time > 3600 ]; then
	echo "${message}" | mail -s "report" """+Email+"""
else
fi""")
	#change the permission of cron, add the crontab line and restore the permissions
	os.system('sudo chmod 777 /var/spool/cron; sudo echo "0 */1 * * * ~/'+file+'.bash" >> /var/spool/cron/ec2-user; sudo chmod 700 /var/spool/cron')
	#end of the function 
	print('crontab and file installed: new crontab added')

#Fuction to install Django
def DjangoI():

	#look the version of python
	ver=os.system('python --version')
	print('Python version: '+str(ver))
	#installing virtual environment
	os.system('sudo rpm -iUvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm; sudo yum -y install python-pip; sudo pip install virtualenv')
	#create a directory for Django and the virtual environment
	os.system('cd /opt; sudo mkdir django; sudo chown -R ec2-user django; sleep 4; cd django; sudo virtualenv django-env')

	#activating virtualenv
	os.system('source /opt/django/django-env/bin/activate; sudo chown -R ec2-user /opt/django; cd /opt/django; pip install django; django-admin --version; django-admin startproject project1; sudo yum -y install tree; tree project1; sleep 1')

#Function to Update kernel
def UpKernelI():

	#clean and update the kernel. otherwise reply an error message
	os.system('sudo yum clean all && sudo yum -y update kernel && sudo reboot || echo "FAILUREEE"')

#Function to create 2 pages in the Apache server
def WebsideI():

	#change the perssion to work with python
	os.system('sudo chmod 777 /var/www/html')
	#sk the user to name the html files to be shown in the Apache server
	ff=raw_input('Introduce the name of the first html file: \n')
	sf=raw_input('Introduce the name of the second html file: \n')
	
	#creating variables which address the html files
	fone=('/var/www/html/'+ff+'.html')
	os.system('sudo mkdir /var/www/html/2pages')
	dir=('/var/www/html/2pages')
	fsecond=(dir+'/'+sf+'.html')
	#a variable which address to the setting file of apache
	authfile=('/etc/httpd/conf/httpd.conf')

	#create the first html file
	os.system('sudo echo "new" >> '+fone)
	#open the file
	page=open(fone, 'w')
	#write into the file
	page.write("""<!DOCTYPE>
	<html>
		<head>
			<title> first page </title>
		</head>
		<body>
			<h1 style="font-size: 40px; color:blue"> HELLO.. WORLD..!!</H1>
			<a href=\"2pages/"""+sf+""".html\"; style=" 30px; color: violet"> GO TO THE NETX PAGE</a>
		</body>
	</html>""")

	#Authentication inside the html configuration file
	os.system('sudo sed -i "151s/None/AuthConfig/1" '+authfile)
	os.system('sudo sed -i \'159i <Directory "'+dir+'">\' '+authfile)
	os.system('sudo sed -i \'160i AllowOverride AuthConfig\' '+authfile)
	os.system('sudo sed -i \'161i </Directory>\' '+authfile)
	
	#create a file which contain the passwords and users to access the second page
	htpasswd=(dir+'/.htpasswd')
	UserOne= raw_input('\nIntroduce user1: \n')
	Pone= raw_input('Introduce password: \n')
	UserTwo= raw_input('Introduce user2: \n')
	Ptwo= raw_input('Introduce password: \n')
	
	os.system('sudo htpasswd -ci '+htpasswd+' '+UserOne+' <<< '+Pone)
	os.system('sudo htpasswd -i '+htpasswd+' ' +UserTwo+' <<< '+Ptwo)

	os.system('sudo chmod 777 '+dir)
	os.system('sudo echo "new" >> '+dir+'/.htaccess')
	htaccess=open(dir+'/.htaccess', 'w')
	htaccess.write("""Authtype Basic
AuthName "users: """+UserOne+', '+UserTwo+' passwords: '+Pone+', '+Ptwo+"""
AuthUserFile """+htpasswd+"""
Require valid-user""")
	
	#permissions for the file htaccess and htpasswd
	os.system('sudo chmod 644 '+dir+'/.htaccess')
	os.system('sudo chmod 644 '+htpasswd)

	#create the second page of the webside
	os.system('sudo echo "new" >> '+fsecond)
	page=open(fsecond, 'w')
	page.write("""<!DOCTYPE html>
	<html>
		<head>
			<title> second page </title>
		</head>
		<body style="background-color: red">
			<h1 style="font-size: 40px; color: white"> SECOND PAGE...!! </h1>
			<a href=\"../"""+ff+""".html\"; style=" 30px; color: violet"> BACK TO THE FIRST PAGE</a>
		</body>
	</html>""")
	
	#restart the Apache server
	os.system('sudo service httpd restart')

#Function to add the IP into Django server
