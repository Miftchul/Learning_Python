# Brute Force Example
# This file demonstrates solving problems using the brute force approach.
# Brute force involves trying all possible solutions to find the correct one.

import itertools

def brute_force(target, characters):
    for length in range(1, len(target) + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt = ''.join(attempt)
            print(f"Trying: {attempt}")
            if attempt == target:
                print(f"Password found: {attempt}")
                return attempt
    print("Password not found.")
    return None

if __name__ == "__main__":
    target_password = "abc"
    character_set = "abcdefghijklmnopqrstuvwxyz"
    brute_force(target_password, character_set)