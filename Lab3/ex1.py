# Name: Cassiddy Ginoza
# Date: Jan. 27, 2026

from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key) 
#cipher suite is an object

encoded_text = cipher_suite.encrypt(b"This is a really secret message.")
print(f"Encoded text: {encoded_text}")
#b is a bite string - used when you want raw data

decoded_text = cipher_suite.decrypt(encoded_text)
print(f"Decoded text: {decoded_text.decode('utf-8')}")