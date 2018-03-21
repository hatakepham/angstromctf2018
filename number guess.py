import socket
from ctypes import CDLL

host = "shell.angstromctf.com"
port = 1235

libc = CDLL("libc.so.6")

def recv():
	global s
	# bien global
	recv=s.recv(1024).strip()
	if recv == '':
		recv = s.recv(1024).strip()
	return recv

	# nhan du lieu

def  send(mess):
	global s
	s.send(str(mess) + '\n')
	# gui du lieu



def flag():
	global s
	global resault
	n = recv()
	# print n
	name = "aaa"
	send(name)
	libc = CDLL("libc.so.6")
	a=libc.time(0)
	libc.srand(a)

	a1 = libc.rand()%1000000
	print a1
	a2 = libc.rand()%1000000
	print a2
	a3=a1+a2
	n1 = recv()
	# print n1
	send(a3)
	# print resault
	n2 = recv()
	print n2
	if n2[0]=="C":
		print n2
		raw_input()

if 1:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host,port))
	# print " ket  noi thanh cong"
	flag()
