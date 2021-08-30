import random

print("welcome to password")

s = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

number = int(input ("amount of password U want: "))


length= int(input('length of the password: '))

print('\npasswords: ')

for psw in range(number):
    psw = ''
    for c in range (length):
        psw+= random.choice(s)
    print(psw)