from cryptography.fernet import Fernet


class Encryption:
    # Creating a Key using symmetric equation
    def create_key(self):
        key = Fernet.generate_key()
        return key

    # Writing Key
    def write_key(self, key, key_name):
        with open(key_name, "wb") as mykey:
            mykey.write(key)

    # Loading key
    def load_key(self, key_name):
        with open(key_name, "rb") as mykey:
            key = mykey.read()
        return key

    # Function that encrypts files
    def encrypt_file(self, key, original_file, encrypted_file):

        f = Fernet(key)

        with open(original_file, "rb") as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(encrypted_file, "wb") as file:
            file.write(encrypted)

    # Function that decrypts files
    def decrypt_file(self, key, encrypted_file, decrypted_file):

        f = Fernet(key)

        with open(encrypted_file, "rb") as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(decrypted_file, "wb") as file:
            file.write(decrypted)


encryptor = Encryption()

mykey = encryptor.create_key()

encryptor.write_key(mykey, "mykey.key")

loaded_key = encryptor.load_key("mykey.key")

encryptor.encrypt_file(loaded_key, "pasta.txt", "enc_pasta.txt")

encryptor.decrypt_file(loaded_key, "enc_pasta.txt", "dec_pasta.txt")
