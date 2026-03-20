# Takes ciphertext and a shift key, returns the decrypted text
def decrypt(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isalpha():
            # Check if letter is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Shift the letter backwards and wrap around using % 26
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            result += decrypted_char
        else:
            # Keep spaces, numbers, and symbols unchanged
            result += char

    return result

# Takes plaintext and a shift key, returns the encrypted text
def encrypt(plaintext, shift):
    result = ""

    for char in plaintext:
        if char.isalpha():
            # Check if letter is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Shift the letter forward and wrap around using % 26
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted_char
        else:
            # Keep spaces, numbers, and symbols unchanged
            result += char

    return result

# Tries all 26 possible shifts and prints each result
# Useful when you don't know the shift key
def brute_force(ciphertext):
    print("\n--- Brute Force: Trying All 26 Shifts ---")
    for shift in range(1, 27):
        attempt = decrypt(ciphertext, shift)
        print(f"  Shift {shift:2}: {attempt}")

# Just a welcome message when the program starts
def banner():
    print("=" * 45)
    print("Cipher Decoder - Caesar Cipher Tool")
    print("=" * 45)

# This is where the program starts and handles user input
def main():
    banner()

    print("\nWhat do you want to do?")
    print(" 1. Encrypt a message")
    print(" 2. Decrypt a message")
    print(" 3. Brute force a ciphertext (unknown key)")

    choice = input("\nEnter choice (1/2/3): ").strip()

    if choice == "1":
        # Encrypt mode
        plaintext = input("Enter your message: ")
        shift = int(input("Enter shift key (1-25): "))
        encrypted = encrypt(plaintext, shift)
        print(f"\n Original : {plaintext}")
        print(f" Encrypted: {encrypted}")
        print(f" Shift Key: {shift}")

    elif choice == "2":
        # Decrypt mode
        ciphertext = input("Enter ciphertext: ")
        shift = int(input("Enter shift key (1-25): "))
        decrypted = decrypt(ciphertext, shift)
        print(f"\n Ciphertext: {ciphertext}")
        print(f" Decrypted : {decrypted}")
        print(f" Shift Key : {shift}")

    elif choice == "3":
        # Brute force mode — try all 26 shifts
        ciphertext = input("Enter ciphertext: ")
        brute_force(ciphertext)
        print("\n Look through the results and find the one that makes sense!")

    else:
        print("\n Invalid choice. Please run the program again.")

    print("\n" + "=" * 45)
    print("Thanks for using Cipher-Decoder Script!")
    print("=" * 45)

if __name__ == "__main__":
    main()