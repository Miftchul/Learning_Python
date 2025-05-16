import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Ensure password contains at least one lowercase, uppercase, digit, and symbol
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices
    if length > 4:
        chars += random.choices(
            string.ascii_letters + string.digits + string.punctuation,
            k=length - 4
        )

    random.shuffle(chars)
    return ''.join(chars)

if __name__ == "__main__":
    try:
        length = int(input("Masukkan panjang password (minimal 4): "))
        password = generate_password(length)
        print("Password acak Anda:", password)
    except ValueError as e:
        print("Error:", e)