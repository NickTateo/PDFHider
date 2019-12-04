#!/usr/bin/python3

#Pedro Sicilia
#Nicholas Tateo
#CIS4362
#PDFHider: PDF angecryption CLI tool 

import sys
from Crypto.Cipher import AES

#first cipher block: "%PDF-\0obj\nstream"
test_key = "ABCDEFGHIJKLMNOP"

def checkArgs(v):
	if(len(sys.argv) == 4):
		infile1, infile2, outfile = sys.argv[1:4]
		print("\nArguments:\n", infile1, infile2, outfile, "\nEnd")
		return True
		
	elif(len(sys.argv) > 4):
		print("Error: excess arguments\nUsage: ./PDFHider <input1.pdf> <input2.pdf> <output.pdf>")
	else:
		print("Error: missing arguments\nUsage: ./PDFHider <input1.pdf> <input2.pdf> <output.pdf>")

	return False
	
#def checkFiles():
	#with open(fname1, "rb") as f1
		#assert f1.startswith

#def pad():
	

#----------Begin main script----------

if(checkArgs(sys.argv)):
	print(AES.block_size, AES.MODE_CBC)


#-----------------End-----------------