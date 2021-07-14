# This is a sample Python script.

from RSA_main import RSA

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rsa = RSA()

    # key_n, key_e, key_d = rsa.generate_new_key()
    #
    # public_key = (key_n, key_e)
    # private_key = (key_n, key_d)

    public_key = (548428634215493197, 13404209533689397)
    private_key = (548428634215493197, 136138334080255533)
    msg = "This is a non-complex message. Really"

    # enc = rsa.encrypt_message(msg, public_key)
    # dec = rsa.decrypt_message(msg, private_key)

    endec = rsa.test(msg, public_key, private_key)

    print("Keys (public, private): ", public_key, private_key)
    # print("Message: ", msg)
    # # print("Encrypted: ", enc)
    # # print("Decrypted: ", dec)
    # print("Encrypted -> Decrypted: ", endec)