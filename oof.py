#!/usr/bin/python

#Pedro Sicilia
#Nicholas Tateo
#CIS4362
#PDFHider: PDF angecryption CLI tool 

import sys

from Crypto.Cipher import AES
#import Crypto.cipher
#from Crypto.Cipher import AES


#check if arv[1] = -d or -e
#if true then 3 argv if false then argv 4
#check if pdf is valid





def myfunction():
	print ("do stuff")


#with open("file.pdf", "rb") as f:




	
#define functions here


#---Begin main script---


#do stuff here

if sys.argv[1].lower() == "-d":
	print("TEST")

	
elif sys.argv[1].lower() == "-e":
	print("TEST")

else:
	with open(sys.argv[1], "rb") as g:
		f = g.read()
	with open(sys.argv[2], "rb") as g:
		s = g.read()
	
	fcheck = f[:4].decode("ascii")
	scheck = s[:4].decode("ascii")
	#fcheck = fcheck.decode("ascii")

	print(fcheck)
#	print(chr(fcheck))
	print(scheck)

	if ((fcheck != "%PDF") or (scheck != "%PDF") ):
		print("Error: Wrong File Type")
	
myfunction()

h = b''
for i in range(8):
	h+=b'80'
	h+=b'23'


c = b"%PDF-\0obj\nstream"

res = c + b"GARasndjaksndjkasndkBAGE" + b"\nendstream\nendobj\n" + f



with open(sys.argv[1], "wb") as g:
	g.write(res)
	#g.write(extra, 'as')





#----------End----------