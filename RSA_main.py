# This is a sample Python script.

import random

from RSA_keygen import RSAkeygen
from RSA_signature import RSAsignature
from RSA_encryption import RSAencryption


class RSA(RSAsignature, RSAencryption, RSAkeygen):

    def generate_new_key(self):
        return RSAkeygen.generate_key(self)

    def encrypt_message(self, text, public_key):
        return RSAencryption.encrypt(self, text, public_key)

    def decrypt_message(self, text, private_key):
        return RSAencryption.decrypt(self, text, private_key)

    def generate_signature(self):
        return RSAsignature.sign(self)

    def authenticate_signature(self):
        return RSAsignature.authenticate(self)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # todo test procedure
    rsa = RSA()
    print(rsa.generate_key())
