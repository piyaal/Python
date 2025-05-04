#Decrypted message from encryption
print("if the encrypted sentence is space separated like 8 5 12 12 15 ,what will be the decrypted value?")

def decrypt(encrypted_sentence):
    # Split the encrypted sentence into numbers
    numbers = encrypted_sentence.split()
    decrypted = ""
    for num in numbers:
        if num.isdigit():
            # Convert number back to corresponding letter
            decrypted += chr(int(num) + ord('a') - 1)
        else:
            decrypted += num
    return decrypted

# Example usage
encrypted_input = input("Enter the encrypted message (numbers separated by spaces): ")
print("Decrypted message:", decrypt(encrypted_input))