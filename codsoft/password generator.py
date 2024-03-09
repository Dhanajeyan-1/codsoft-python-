import string
import random
a = string.ascii_lowercase
b = string.ascii_uppercase
c = string.digits
w = input("Enter the level of the difficulty password you want (Easy/Medium/Hard): ").lower()
q = int(input("Enter the length of the password you want: "))
password = None
if q >= 0:
    if w == 'easy':
        password = a
    elif w == 'medium':
        password = a + b
    elif w == 'hard':
        password = a + b + c
else:
    print("ENTER THE RANGE GREATER THAN 0")
    password = None
if password:
    passwordis = "".join(random.choice(password) for _ in range(q))
    print(f"The password is {passwordis}")
