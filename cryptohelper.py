from cryptography.fernet import Fernet
from os.path import exists


class CryptoHelper:
    def __init__(self):
        self.filename = ""
        self.key_name = ""

    def create_key(self):
        key = Fernet.generate_key()
        with open(self.key_name, "wb") as key_file:
            key_file.write(key)

    def encrypt_file(self):
        with open(self.key_name, "r") as keyfile:
            key = Fernet(keyfile.read())

        with open(self.filename, "rb") as file:
            file_data = file.read()
            encrypted_data = key.encrypt(file_data)

        with open(self.filename, "wb") as file:
            file.write(encrypted_data)

    def decrypt_file(self):
        with open(self.key_name, "r") as keyfile:
            key = Fernet(keyfile.read())
        with open(self.filename, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = key.decrypt(encrypted_data)
        with open(self.filename, 'wb') as file:
            file.write(decrypted_data)

    def file_and_key_chooser(self, method):
        while True:
            self.filename = input("Enter filename >> ")
            if exists("./" + self.filename):
                self.key_name = input("Enter key name >> ")
                if exists("./" + self.key_name):
                    method()
                    break
                else:
                    print("Error! Key not found.")
            else:
                print("Error! File not found.")

    def start_user_interface(self):
        print("1. Create unique key for your passwords.\n"
              "2. Encrypt file using your key\n"
              "3. Decrypt file using your key")
        while True:
            option = input("Choose an option [1-3] >> ")
            if option == "1":
                self.key_name = input("Enter key name >> ")
                self.create_key()
                print("Key successfully created!")
                break
            elif option == "2":
                self.file_and_key_chooser(self.encrypt_file)
                print("File " + self.filename + " successfully encrypted!")
                break
            elif option == "3":
                self.file_and_key_chooser(self.decrypt_file)
                print("File " + self.filename + " successfully decrypted!")
            else:
                print("Invalid value!")


helper = CryptoHelper()
helper.start_user_interface()
