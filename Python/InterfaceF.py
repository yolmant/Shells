#!/usr/bin/python
import function

task = 1
print('Welcome to the multi-tasker of python\n')

while task != 0:
	print("""Here are the package:
		
		Apache - Server HTTPD
		Cow - Verification of COW
		Cron - Script message with cron configuration
		Django - Python Web Framework
		Ip host - Allowed the VM to work with the Django server
		Git - Reponsotories in github
		Upk - Update kernel
		Wedsides - create the first and second web pages
		Exit - finish the program\n""")

	task = raw_input('What would you like to do? \n').lower()

	if task == 'apache':
		function.ApacheI()

	elif task == 'cow':
		function.CowI()
	
	elif task == 'cron':
		function.CronI()

	elif task == 'django':
		function.DjangoI()

	elif task == 'ip host':
		function.IpAccessI()

	elif task == 'git':
		function.GithubI()

	elif task == 'upk':
		function.UpKernelI()

	elif task == 'websides':
		function.WebsideI()

	elif task == 'exit':
		print('program end. Good bye')
		break
	
	else:
		print('Error101. wrong package. '+task+' doesn\'t exist')

	ask = ' '
	while ask != 'y':
		ask = raw_input('\nWould you like to install another package? (y/n) ').lower()

		if ask == 'n':
			task = 0
			print('\nprogram end. Good bye\n')
			break

		elif ask != 'n':
			print('Error102. '+ask+' is not an option\n')
