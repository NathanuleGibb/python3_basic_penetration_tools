import string
import random

passcount = int(input('how many passwords? :'))
password = string.ascii_letters + string.digits
char = ''
file = open("wordlists.txt", "w")
for count in range(passcount):
    for x in random.sample(password,random.randint(8,8)):
        char+=x
    file.write(char+'\n')
    char=''
file.close()
print('wordlist is ready')
