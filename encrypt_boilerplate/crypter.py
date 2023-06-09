import json
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import os

class Cipher:

    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        data = json.dumps(data).encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_CBC)
        return cipher.iv + cipher.encrypt(pad(data, AES.block_size))
    
    def decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, iv=data[:16])
        return json.loads(unpad(cipher.decrypt(data[16:]), AES.block_size))

    def save(self, data, filename):
        with open(filename, 'wb') as f:
            f.write(self.encrypt(data))

    def load(self, filename):
        with open(filename, 'rb') as f:
            return self.decrypt(f.read())


mdict = [{'hello': 'world', 'other': ['data', 'here']}] * 100
mdict = {'pwd': '1234', 'dict': mdict}
cipher = Cipher(os.urandom(16))
cipher.save(mdict, 'data.bin')
print(cipher.load('data.bin'))