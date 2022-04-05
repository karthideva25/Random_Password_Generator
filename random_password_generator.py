import random
import string

length = int(input("Enter the length of password : "))
all = string.ascii_lowercase + string.ascii_uppercase + \
    string.digits + string.punctuation
temp = random.sample(all, length)
# generate password
password = "".join(temp)
print(f'Password is : {password}')
