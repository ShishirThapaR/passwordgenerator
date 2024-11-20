import random

uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letter.lower()
digits = "1234567890"
symbols = "*!@#$%&*()_+-"

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letter

if lower:
    all +=lowercase_letter

if nums:
    all +=digits

if syms:
    all +=symbols

length = 12
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)