def xor(b1,b2):
	a=bytearray(b1)
	for i in range(len(b1)):
		a[i]=b1[i]^b2[i]
	return a


b = "fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7"
b1=bytearray.fromhex(b)
for i in range(256):
	b2=[i]*len(b1)
	plantext=bytes(xor(b1,b2))
	print plantext
