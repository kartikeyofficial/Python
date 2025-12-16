import random

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1."

    alphabetic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
    numeric = [0,1,2,3,4,5,6,7,8,9]
    special_symbols = ['@','#','$','&','*','_']

    # Combine all character sets
    all_characters = alphabetic + numeric + special_symbols

    # Ensure the password contains at least one of each type
    password = [
        random.choice(alphabetic),
        random.choice(numeric),
        random.choice(special_symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 3)

    # Shuffle the created password list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Get user input for password length
try:
    length = int(input("Enter the desired password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
