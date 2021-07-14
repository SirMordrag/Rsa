# This is a sample Python script.



class RSAencryption:

    def __init__(self, settings):
        self.settings = settings.copy()

    def encrypt(self, message, public_key):
        blocks = self.split_message_into_blocks(message)
        blocks = self.encrypt_blocks(blocks, public_key)
        return self.construct_message(blocks)

    def test(self, message, public_key, private_key):
        print(message)
        blocks = self.split_message_into_blocks(message)
        print(blocks)
        blocks = self.encrypt_blocks(blocks, public_key)
        print(blocks)
        blocks = self.decrypt_blocks(blocks, private_key)
        print(blocks)
        message = self.join_blocks_into_message(blocks)
        print(message)
        return message

    def decrypt(self, message, private_key):
        blocks = self.deconstruct_message(message)
        blocks = self.decrypt_blocks(blocks, private_key)
        return self.join_blocks_into_message(blocks)

    def split_message_into_blocks(self, message):
        encoding = self.settings["Encoding"]
        block_size = int(self.settings["Block size"])
        message_blocks = []

        # convert the message to bytes
        message = message.encode(encoding)

        # from 0 to end with a step of block_size; ptr_block points to a start of the current block
        for ptr_block in range(0, len(message), block_size):
            temp = 0
            for index in range(ptr_block, min(len(message), ptr_block + block_size)):
                temp <<= 8
                temp += message[index]
            message_blocks.append(temp)

        return message_blocks

    def join_blocks_into_message(self, message_blocks):
        block_size = int(self.settings["Block size"])
        message = []

        for block in message_blocks:
            block_content = []
            for index in range(0, block_size):
                temp = block - ((block >> 8) << 8)
                block >>= 8
                block_content.insert(0, chr(temp))
                if block == 0:
                    break
            message.extend(block_content)

        return ''.join(message)

    def encrypt_blocks(self, message_blocks, public_key):
        encrypted_blocks = []
        key_n, key_e = public_key

        for block in message_blocks:
            temp = pow(block, key_e, key_n)
            encrypted_blocks.append(temp)

        return encrypted_blocks

    def decrypt_blocks(self, encrypted_blocks, private_key):
        decrypted_blocks = []
        key_n, key_d = private_key

        for block in encrypted_blocks:
            temp = pow(block, key_d, key_n)
            decrypted_blocks.append(temp)

        return decrypted_blocks

    def construct_message(self, encrypted_blocks):
        encoding = self.settings["Encoding"]
        block_size = self.settings["Block size"]
        key_length = self.settings["Key length"]

        encrypted_message = str(block_size) + '_' + str(key_length) + '_' + encoding + '_'

        for block in encrypted_blocks:
            encrypted_message += str(block)
            encrypted_message += ','

        return encrypted_message

    def deconstruct_message(self, encrypted_message):
        encoding = self.settings["Encoding"]
        block_size = self.settings["Block size"]
        key_length = self.settings["Key length"]

        #  todo
        encrypted_blocks = str(block_size) + '_' + str(key_length) + '_' + encoding + '_'

        return encrypted_blocks
