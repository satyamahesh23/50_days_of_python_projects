import random
char ="!@#$%^&*abcdefghijklmnopqrstuvwxyz12345678910"

password=""
for i in range(8):
    password+=random.choice(char)
    print("generate password is :",password)