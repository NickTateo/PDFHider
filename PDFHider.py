#!/usr/bin/python
#
#written for Python 2.7
#
#Pedro Sicilia
#Nicholas Tateo
#CIS4362
#PDFHider: PDF angecryption CLI tool 

import sys
from Crypto.Cipher import AES

c0 =  "%PDF-obj\nstream\n"
chunk_end = "\nendstream\nendobj\n"
CHUNK_END_SIZE = len(chunk_end)
cphr = AES
pdfmagic = "%PDF-"
test_key = "ABCDEFGHIJKLMNOP"

#takes argument vector as parameter
def checkArgs(v):
	if(len(v) == 4):
		return True
	elif(len(v) > 4):
		print("Error: excess arguments\n")
	elif(len(v) < 3):
		print("Error: missing arguments\n")

	return False
	
#takes argument vector as parameter
def checkFlag(v):
	if(len(v) > 1 and v[1][0] != '-'):
		return False
	else:
		if(len(v) != 3):
			print("Error: number of arguments\n")
			return False
		else:
			if(v[1] == "-e"):
				enc(v[2])
			elif(v[1] == "-d"):
				dec(v[2])
			else:
				print("Error: unknown flag\n")
				return False
				
		return True
		
#def checkFiles():
	#with open(fname1, "rb") as f1
		#assert f1.startswith(pdfmagic)

def enc(file):
	with open(file, "rb") as input:
		output = input.read()
	
	
	#cbc_e = cphr.new(test_key, cphr.MODE_CBC, retrieveIV(reverse))

	
	print file

def dec(file):
	with open(file, "rb") as input:
		output = input.read()

	i = (output.find(pdfmagic, cphr.block_size))
	reverse = output[:(i - CHUNK_END_SIZE)] + output[i:]
	#iv = retrieveIV(output)
	iv = output[(-cphr.block_size):]
	
	cbc_d = cphr.new(test_key, cphr.MODE_CBC, iv)
	
	#DEBUG ONLY---!
	print("Decrypting file", file, "with iv", iv)

	reverse = cbc_d.decrypt(reverse)
	
	with open("reverse.pdf", "w") as o:
		o.write(reverse)
		
	
#retrieves IV from combined files	
def retrieveIV(file):
	

	return file
		
#pads data to a multiple of cipher block size
def pad(fdata):
	return fdata + ((cphr.block_size - len(fdata) % cphr.block_size) * chr(cphr.block_size - len(fdata) % cphr.block_size)).encode()

#----------Begin main script----------

if(checkFlag(sys.argv)):
	#DEBUG ONLY---!
	print("\nFlag detected\n")	
	
elif(checkArgs(sys.argv)):
	infile1, infile2, outfile = sys.argv[1:4]
	
	with open(infile1, "rb") as input:
		infile1 = pad(input.read())
		
	with open(infile2, "rb") as input:
		infile2 = pad(input.read())
	
	ptxt = infile1[:cphr.block_size]
	
	ecb = cphr.new(test_key, cphr.MODE_ECB)
	c0 = ecb.decrypt(c0.encode())
	
	initV = ""

	for i in range(cphr.block_size):
		x = ord(c0[i]) ^ ord(ptxt[i])
		initV += chr(x)
		
	#initV2 = "".join([chr(ord(c0[i]) ^ ord(ptxt[i])) for i in range(cphr.block_size)])

	cbc_e = cphr.new(test_key, cphr.MODE_CBC, initV)
	
	infile1 += initV
	output = cbc_e.encrypt(infile1)
		
	output = output + chunk_end + infile2 + initV
	
	with open(outfile, "w") as o:
		o.write(output)
	
	
#DEBUG ONLY---!
print("\nTerminating program...\n")

#-----------------End-----------------