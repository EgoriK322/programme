import random

abc="abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_len=int(input("Длина пароля"))
password=""

for i in range(password_len):
    num = random.randint(0, len(abc)-1)
    password = password + abc[num]

print(password)
