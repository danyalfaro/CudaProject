import uuid
import hashlib
import random
import string

def createPasswordEasy(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def createPasswordMedium(length):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(length))

def createPasswordHard(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(length))

def hashPassword(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def main():
    f = open("hashes.txt","w+")
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(10)
        hash = hashPassword(password)
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(10)
        hash = hashPassword(password)
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(10)
        hash = hashPassword(password)
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    f.close() 

main()