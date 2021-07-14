# This is a sample Python script.

import random

from RSA_keygen import RSAkeygen
from RSA_signature import RSAsignature
from RSA_encryption import RSAencryption


class RSA(RSAsignature):

    RSA_settings = {
        "Key length": 30,  # bits
        "Block size": 6,   # bytes
        "Encoding": 'ascii',
    }

    def generate_new_key(self):
        crypto = RSAkeygen(self.RSA_settings)
        output = crypto.generate_key()
        del crypto
        return output

    def test(self, message, public_key, private_key):
        crypto = RSAencryption(self.RSA_settings)
        output = crypto.test(message, public_key, private_key)
        del crypto
        return output

    def encrypt_message(self, message, public_key):
        crypto = RSAencryption(self.RSA_settings)
        output = crypto.encrypt(message, public_key)
        del crypto
        return output

    def decrypt_message(self, message, private_key):
        crypto = RSAencryption(self.RSA_settings)
        output = crypto.decrypt(message, private_key)
        del crypto
        return output

    def generate_signature(self):
        return RSAsignature.sign(self)

    def authenticate_signature(self):
        return RSAsignature.authenticate(self)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # todo test procedure
    rsa = RSA()
    print(rsa.generate_key())
