def encrypt():
    encrypted_code, code, key = "", input("Enter code to encrypt: "), int(input("Enter the key/number of shifts: "))
    for i in code:
        if i != ' ':
            if i.isupper():
                encrypted_code += chr((ord(i) + key - 65) % 26 + 65)
            else:
                encrypted_code += chr((ord(i) + key - 97) % 26 + 97)
        else:
            encrypted_code += ' '
    return encrypted_code


def decrypt():
    decrypted_code, code, key = "", input("Enter code to decrypt: "), int(input("Enter the key/number of shifts: "))
    for i in code:
        if i != ' ':
            if i.isupper():
                decrypted_code += chr((ord(i) - (key + 65)) % 26 + 65)
            else:
                decrypted_code += chr((ord(i) - (key + 97)) % 26 + 97)
        else:
            decrypted_code += ' '
    return decrypted_code


ch = int(input("Want to use Caesar Cipher?\n1 - Yes\n2 - No\n"))
while ch == 1:
    choice = int(input("What is your need:\n1 - encrypt\n2 - decrypt\n"))
    if choice == 1:
        print("Encrypted code is : ", encrypt())
    elif choice == 2:
        print("Decrypted code is : ", decrypt())
    else:
        print("Enter correct choice")
        continue
    ch = int(input("Want to use Caesar Cipher again?\n1 - Yes\n2 - No\n"))
print("Thank You, Caesar's here, whenever you need him!")
