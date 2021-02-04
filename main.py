from core.window_handler import run_window
from core.fingerprint import userCheck
import base64
import os

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet


def create_file(filename):
    try:
        createFile = open(filename, "x")
        os.system( "attrib +h passwords.txt" )
        createFile.close()
    except:
        pass
    
    
if __name__ == "__main__":  
    filename = "passwords.txt"
    create_file(filename)
    if fingerId := userCheck():

        salt = b"A_Salt"
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend(),
        )
        with open(filename, "r+b") as openFile:
            encryptedData = openFile.read()
        key = base64.urlsafe_b64encode(kdf.derive(fingerId.encode()))
        fer = Fernet(key)
        encryptedData = fer.decrypt(encryptedData) if encryptedData else encryptedData
        run_window(fer, filename , encryptedData.decode())