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

# def hashPassword(password):
#     salt = uuid.uuid4().hex
#     return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def md5(length):
    f = open("MD5hashes.txt","w+")
    print("Easy Passwords: ")
    for i in range(length):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(length):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(length):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    f.close() 

def sha1(length):
    f = open("SHA1hashes.txt","w+")
    print("Easy Passwords: ")
    for i in range(length):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(length):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(length):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    f.close() 

def sha256(length):
    f = open("SHA256hashes.txt","w+")
    print("Easy Passwords: ")
    for i in range(length):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(length):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(length):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    f.close() 

def sha512(length):
    f = open("SHA512hashes.txt","w+")
    print("Easy Passwords: ")
    for i in range(length):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(length):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(length):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    f.close()

def main():
    md5(10)
    sha1(10)
    sha256(10)
    sha512(10)
    
main()