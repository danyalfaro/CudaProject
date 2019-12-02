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
#      return hashlib.sha256(password.encode()).hexdigest()

def md5(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    

def sha1(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha1(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    

def sha256(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")

def sha512(length, f):
    print("Easy Passwords: ")
    for i in range(10):
        password = createPasswordEasy(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Medium Passwords: ")
    for i in range(10):
        password = createPasswordMedium(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")
    print("Hard Passwords: ")
    for i in range(10):
        password = createPasswordHard(length)
        salt = uuid.uuid4().hex
        hash = hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ':' + salt
        print("Password: ", password)
        print("Hash: ", hash)
        f.write(hash)
        f.write("\n")

def main():
    f = open("MD5hashes.txt","w+")
    md5(8, f)
    md5(10, f)
    md5(12, f)
    md5(14, f)
    f.close()

    f2 = open("SHA1hashes.txt","w+")
    sha1(8, f2)
    sha1(10, f2)
    sha1(12, f2)
    sha1(14, f2)
    f2.close()

    f3 = open("SHA256hashes.txt","w+")
    sha256(8, f3)
    sha256(10, f3)
    sha256(12, f3)
    sha256(14, f3)
    f3.close()

    f4 = open("SHA512hashes.txt","w+")
    sha512(8, f4)
    sha512(10, f4)
    sha512(12, f4)
    sha512(14, f4)
    f4.close()
    
main()