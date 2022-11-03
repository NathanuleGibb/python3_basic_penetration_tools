#!/usr/bin/python3

import sys
import colorama
import hashlib
from colorama import Fore, Back, Style

# crack md5 hashes via wordlists
def md5crack():
	print (Fore.GREEN + "MD5 hashes Crack , store Hashes & Lists in .txt")
	md5crack = hashlib.md5()
	print("")
	hashfile = input("name of hash file ?  ")
	wordlists = input("name of Wordlists file  ")
	try:
		hashdocument = open(hashfile, "r")
	except IOError:
		print("wrong file name")
		input()
		sys.exit
	else:
		crack = hashdocument.readline()
		crack = crack.replace("\n", (''))

	try:
		wordlists = open(wordlists, "r")
	except IOError:
		print('wrong file name')
		input()
		sys.exit
	else:
		pass
		for line in wordlists:
			md5crack = hashlib.md5()
			line = line.replace("\n", (""))
			md5crack.update(line.encode('utf-8'))
			word_hash = md5crack.hexdigest()
			if word_hash==crack:
				print('')
				print(Fore.BLUE + "Great! The word match to the given hash is ", line)
				sys.exit()
			else:
				print("no matches for the hashes")
				sys.exit()
print('MD5 CARCK'), md5crack()
