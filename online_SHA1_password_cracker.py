from urllib.request import urlopen 
import hashlib

hashsha1 = input('Please enter the SHA1 hash you wish to crack: ')
wordlist = input('Please enter the URL of the wordlist you would like to use: ')
allw = str(urlopen(wordlist).read(), 'utf-8')

for crack in allw.split('\n'):
    hashcrack = hashlib.sha1(bytes(crack, 'utf-8')).hexdigest()
    if hashcrack == hashsha1:
        print('PASSWORD FOUND: ', str(crack))
        quit()
    elif hashcrack != hashsha1:
        print("Password Crack ", str(crack), " Not Found")
print("Please choose another wordlist and try again")