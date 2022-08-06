import string
import random

number = int(input("number of pasword that you want: "))
lenght = int(input("enter the lenght of password: "))

s1 = str(string.ascii_letters)
s2 = str(string.digits)
string = s1 + s2
# lists = list(string.split(" "))

for passwords in range(number):
    password = " "
    for words in range(lenght):
        password += random.choice(string)
        # print(password)
    print(password)