import os
import pyaes

def decrypt_file(encrypted_file_path, key, output_file_path):
    with open(encrypted_file_path, 'rb') as file:
        file_data = file.read()

    os.remove(encrypted_file_path)

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt_data = aes.decrypt(file_data)

    with open(output_file_path, 'wb') as new_file:
        new_file.write(decrypt_data)

if __name__ == "__main__":
    key = b"testeransomwares"
    encrypted_file_name = "teste.txt.ransomwaretroll"
    decrypted_file_name = "teste.txt"

    decrypt_file(encrypted_file_name, key, decrypted_file_name)

