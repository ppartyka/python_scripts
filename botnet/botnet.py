#!/usr/bin/python

import pxssh
from sys import argv
from hashlib import sha512

svr = ['server1', 'server2', 'server3', 'server4']

def auth_check():
	""" (str) -> Bool
	Checks user password to run the script.
	"""
	PW = raw_input("> ")
	if sha512(PW).hexdigest() == 'hashed sha512 password':
		return True
	else:
		return False

def send_cmd(s, cmd):
	'''(NoneType, str) -> str
	This function a command to the bot server
	'''
	s.sendline(cmd)
	s.prompt()
	print s.before

def login(host, user, passwd):
	''' (str, str, str) -> NoneType
	This function returns a NoneType pxssh object to send commands to.
	'''
	try:
		s = pxssh.pxssh()
		s.login(host, user, passwd)
		return s
	except:
	    print '[-] Error Connecting'
	    exit(0)

def usage():
	''' () -> NoneType
	Usage function that exits if not enough arguments are given.
	'''
	try:
		script, cmd = argv
		return argv
	except:
	    print "This program needs at least 1 input in quotes as a command to send to bot nodes:"
	    print "./pexp.py 'ls'"
	    print ""
	    exit(0)

if __name__ == '__main__':
	if auth_check() == True:
		cmd = usage()
		for box in svr:
			print box
			s = login(box, 'username', 'password')
			send_cmd(s, str(cmd[1]))
	else:
		exit(0)
