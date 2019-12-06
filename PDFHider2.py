#!/usr/bin/python
#
#written for Python 2.7
#
#Pedro Sicilia
#Nicholas Tateo
#CIS4362
#PDFHider: PDF angecryption CLI tool 
#
#Usage: ./PDFHide [cover.pdf] [hidden.pdf] [output.pdf]
#
#Encrypt: ./PDFHide -e [output.pdf]
#
#Decrypt: ./PDFHide -d [output.pdf]
#

import sys
from Crypto.Cipher import AES

c0 =  "%PDF-obj\nstream\n"
chunk_end = "\nendstream\nendobj\n"
CHUNK_END_SIZE = len(chunk_end)
cphr = AES
pdfmagic = "%PDF-"
sym_key = "ABCDEFGHIJKLMNOP"
EOF = "%%EOF"
EOF_SIZE = len(EOF)

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

#encrypts result file
def enc(file, iv):
	with open(file, "rb") as input:
		output = input.read()
		
	#iv = output[(i+EOF_SIZE):(i+EOF_SIZE) + cphr.block_size]
	print("Enc IV:", iv)
	
	cbc_e = cphr.new(sym_key, cphr.MODE_CBC, iv)
	
	enc = cbc_e.encrypt(output)
	
	i = (enc.find(pdfmagic, cphr.block_size))
	print("\nEnc i: ", i, "\n")
	
	enc = enc[:i] + chunk_end + enc[i:]
	#enc = enc[:(i + EOF_SIZE + cphr.block_size)] + chunk_end + encfile[(i + EOF_SIZE + cphr.block_size):]

	with open("encrypted.pdf", "w") as o:
		o.write(enc)

	print "Encrypted file", file

#decrypts result file
def dec(file, iv):
	with open(file, "rb") as input:
		output = input.read()

	i = (output.find(pdfmagic, cphr.block_size))
	dec = output[:(i - CHUNK_END_SIZE)] + output[i:]
	#iv = output[(-cphr.block_size):]
	print("Dec IV:", iv)
		
	cbc_d = cphr.new(sym_key, cphr.MODE_CBC, iv)
		
	dec = cbc_d.decrypt(dec)
	
	with open("decrypted.pdf", "w") as o:
		o.write(dec)

	print "Decrypted file", file 

#pads data to a multiple of cipher block size
def pad(fdata):
	return fdata + ((cphr.block_size - len(fdata) % cphr.block_size) * chr(cphr.block_size - len(fdata) % cphr.block_size)).encode()

#----------Begin main script----------

if(checkFlag(sys.argv)):
	print("\nSuccessfully converted file!")
	
elif(checkArgs(sys.argv)):
	infile1, infile2, outfile = sys.argv[1:4]
	
	with open(infile1, "rb") as input:
		infile1 = pad(input.read())
		
	with open(infile2, "rb") as input:
		infile2 = pad(input.read())
	
	ptxt = infile1[:cphr.block_size]
	
	ecb = cphr.new(sym_key, cphr.MODE_ECB)
	c0 = ecb.decrypt(c0.encode())
	
	initV = ""

	for i in range(cphr.block_size):
		x = ord(c0[i]) ^ ord(ptxt[i])
		initV += chr(x)
	
	print(initV)#------------------------------------------DEBUG
	cbc_init = cphr.new(sym_key, cphr.MODE_CBC, initV)
	
	infile1 += initV
	output = cbc_init.encrypt(infile1)
		
	output = output + chunk_end + infile2 + initV
	
	with open(outfile, "w") as o:
		o.write(output)
	
	print("\nSuccessfully wrote combined file", outfile, "!")
	
	print("Beginning decrypt...\n")
	
	dec(outfile, initV)
	
	print("Beginning encrypt...\n")
	
	enc("decrypted.pdf", initV)

print("\nTerminating program...\n")

#-----------------End-----------------