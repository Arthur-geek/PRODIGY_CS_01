def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Traverse the text depending on the sift
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Ignore character if it is not a letter and leave it as it is
        else:
            result += char
    
    return result

def main():
    print("## Welcome to the Caesar Cipher Program ##")
    
    while True:
        choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? (E/D): ").lower()
        
        if choice in ['e', 'd']:
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            
            if choice == 'e':
                encrypted_text = caesar_cipher(text, shift, mode='encrypt')
                print(f"Encrypted Message: {encrypted_text}")
            else:
                decrypted_text = caesar_cipher(text, shift, mode='decrypt')
                print(f"Decrypted Message: {decrypted_text}")
        
        another = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if another != 'yes':
            break

    print("**Thank you for using the Caesar Cipher Program. Goodbye!**")

if __name__ == "__main__":
    main()
