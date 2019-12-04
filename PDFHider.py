#!/usr/bin/python

#Pedro Sicilia
#Nicholas Tateo
#CIS4362
#PDFHider: PDF angecryption CLI tool 

import sys
from Crypto.Cipher import AES

test_key = "ABCDEFGHIJKLMNOP"
#pdfmagic = "%PDF-"
c0 =  "%PDF-obj\nstream\n"
chunk_end = "\nendstream\nendobj\n"
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
	
	#DEBUG ONLY---!
	#print(infile1[:16], infile2[:16])
	
	ptxt = infile2[:cphr.block_size]
	
	c0 = ecb.decrypt(c0.encode())
	
	initV1 = ""

	for i in range(cphr.block_size):
		x = ord(c0[i]) ^ ord(ptxt[i])
		initV1 += chr(x)
	
	#initV2 = "".join([chr(ord(c0[i]) ^ ord(ptxt[i])) for i in range(cphr.block_size)])

	print("\nIV Results:\n")
	print(len(initV1), initV1)

	cbc = cphr.new(test_key, cphr.MODE_CBC, initV1)
	
	output = cbc.encrypt(infile1)
	
	output = output + chunk_end + infile2
	
	with open(outfile, "w") as o:
		o.write(output)
	
	
#DEBUG ONLY---!
print("\nTerminating program...\n")
#-----------------End-----------------