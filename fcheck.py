#!/usr/bin/python

import sys

infile1 = sys.argv[1]
infile2 = sys.argv[2]

with open(infile1, 'rb') as g:
	file1 = g.read()
	
with open(infile2, 'rb') as g:
	file2 = g.read()
	
for i in range(len(file1)):
	if(file1[i] != file2[i]):
		print("FALSE")
		
print("Check completed")