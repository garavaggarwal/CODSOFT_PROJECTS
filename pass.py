import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    if length < 8:
        print("The requested password length is less than 8.")
        use_default_length = input("Would you like to use the default length of 8? (yes/no): ").lower()
        if use_default_length != 'yes':
            return "Password length must be at least 8."
        length = 8

    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "No characters selected for password generation."

    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    password += [random.choice(characters) for _ in range(length - len(password))]
    
    random.shuffle(password)
    
    return ''.join(password)

def main():
    print("Welcome to the Enhanced Password Generator!")
    
    length = int(input("Enter the desired password length (minimum 8): "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    password = generate_password(length, include_uppercase, include_digits, include_special)
    print(f"Generated password: {password}")

main()



