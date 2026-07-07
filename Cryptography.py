# ==========================================
# Cryptography Project
# Developed by: Muskan Dalal
# Internship Project
# ==========================================

import base64

encrypted_text = ""

def encrypt_message():
    global encrypted_text

    message = input("\nEnter your message: ")

    encoded = base64.b64encode(message.encode())

    encrypted_text = encoded.decode()

    print("\nEncrypted Message:")
    print(encrypted_text)


def decrypt_message():
    global encrypted_text

    if encrypted_text == "":
        print("\nNo encrypted message found!")
        return

    decoded = base64.b64decode(encrypted_text.encode())

    print("\nDecrypted Message:")
    print(decoded.decode())


def save_message():
    global encrypted_text

    if encrypted_text == "":
        print("\nNothing to save!")
        return

    file = open("encrypted_message.txt", "w")
    file.write(encrypted_text)
    file.close()

    print("\nEncrypted message saved successfully!")


print("=" * 45)
print("     CRYPTOGRAPHY PROJECT")
print("=" * 45)

while True:

    print("\n1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Save Encrypted Message")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        encrypt_message()

    elif choice == "2":
        decrypt_message()

    elif choice == "3":
        save_message()

    elif choice == "4":
        print("\nThank you for using the Cryptography Project.")
        break

    else:
        print("\nInvalid Choice! Try Again.")