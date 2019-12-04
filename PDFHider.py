#!/usr/bin/python3

#Pedro Sicilia
#Nicholas Tateo
#CIS4362
#PDFHider: PDF angecryption CLI tool 

import sys
from Crypto.Cipher import AES

test_key = "ABCDEFGHIJKLMNOP"
#pdfmagic = "%PDF-"
c0 =  "%PDF-\0obj\nstream"
cphr = AES
ecb = cphr.new(test_key, cphr.MODE_ECB)

def checkArgs(v):
	if(len(v) == 4):
		return True
	elif(len(v) > 4):
		print("Error: excess arguments\nUsage: ./PDFHider <input1.pdf> <input2.pdf> <output.pdf>")
	else:
		print("Error: missing arguments\nUsage: ./PDFHider <input1.pdf> <input2.pdf> <output.pdf>")

	return False
	
#def checkFiles():
	#with open(fname1, "rb") as f1
		#assert f1.startswith(pdfmagic)

def pad(fdata):
	return fdata + ((cphr.block_size - len(fdata) % cphr.block_size) * chr(cphr.block_size - len(fdata) % cphr.block_size)).encode()

#----------Begin main script----------

if(checkArgs(sys.argv)):
	infile1, infile2, outfile = sys.argv[1:4]
	
	#DEBUG ONLY---!
	print("\nArguments:\n", infile1, infile2, outfile, "\nEnd")

	with open(infile1, "rb") as input:
		infile1 = pad(input.read())
		
	with open(infile2, "rb") as input:
		infile2 = pad(input.read())
	
	ptxt = infile1[:cphr.block_size]
	
	print("Before decrypt:", type(c0.encode('utf-8')), c0.encode('utf-8'))
	c0 = ecb.decrypt(c0)
	print(type(c0), c0, type(ptxt), ptxt)
	
	initV1 = ""

	# for i in range(cphr.block_size):
		# print(i, "- C0:", c0[i], "P:", ptxt[i])
		# x = c0[i] ^ ptxt[i]
		# print(x, chr(x))
		# initV1 += chr(x)
	
	#initV2 = "".join([chr(c0[i] ^ ptxt[i]) for i in range(cphr.block_size)])

	# print("\nIV Results:\n")
	# print(len(initV1), initV1)
	# print(len(initV1.encode()), initV1.encode())

	#print(len(initV2.encode()))
	#print(type(c0[15]), c0[15], type(ptxt[15]), ptxt[15], c0[15] ^ ptxt[15])

	#cbc = cphr.new(test_key, cphr.MODE_CBC, initV1)
	#output = cbc.encrypt()
	
	
#DEBUG ONLY---!
print("\nTerminating program...\n")
#-----------------End-----------------