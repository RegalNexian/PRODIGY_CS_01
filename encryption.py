def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char == ' ':
            encrypted_text += char
        elif char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += chr((ord(char) + shift) % 256)
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char == ' ':
            decrypted_text += char
        elif char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += chr((ord(char) - shift) % 256)
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = encrypt(text, shift)
        print("Encrypted message:", result)
    elif choice == 'd':
        result = decrypt(text, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
