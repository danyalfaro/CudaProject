import uuid
import hashlib
import random
import string

def createPasswordEasy(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def createPasswordMedium(length):
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(length))

def createPasswordHard(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(length))

def md5(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        hash = hashlib.md5(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        hash = hashlib.md5(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        hash = hashlib.md5(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    

def sha1(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        hash = hashlib.sha1(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        hash = hashlib.sha1(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        hash = hashlib.sha1(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    
def sha512(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        hash = hashlib.sha512(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        hash = hashlib.sha512(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        hash = hashlib.sha512(password.encode()).hexdigest()
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")

def main():
    f = open("MD5hashes6.txt","w+")
    md5(6, f)
    f.close()

    f1 = open("MD5hashes7.txt","w+")
    md5(7, f1)
    f1.close()

    f2 = open("MD5hashes8.txt","w+")
    md5(8, f2)
    f2.close()

    f3 = open("SHA1hashes6.txt","w+")
    sha1(6, f3)
    f3.close()
    
    f4 = open("SHA1hashes7.txt","w+")
    sha1(7, f4)
    f4.close()

    f5 = open("SHA1hashes8.txt","w+")
    sha1(8, f5)
    f5.close()

    f6 = open("SHA512hashes6.txt","w+")
    sha512(6, f6)
    f6.close()

    f7 = open("SHA512hashes7.txt","w+")
    sha512(7, f7)
    f7.close()

    f8 = open("SHA512hashes8.txt","w+")
    sha512(8, f8)
    f8.close()
    
main()