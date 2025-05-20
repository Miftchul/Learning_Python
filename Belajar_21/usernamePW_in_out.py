# A website requires the users to input username and password to register. Write a
#  program to check the validity of password input by users. Following are the criteria
#  for checking the password:
#  1. At least 1 letter between [a-z]
#  2. At least 1 number between [0-9]
#  1. At least 1 letter between [A-Z]
#  3. At least 1 character from [$#@]
#  4. Minimum length of transaction password: 6
#  5. Maximum length of transaction password: 12
#  Your program should accept a sequence of comma separated passwords and will
#  check them according to the above criteria. Passwords that match the criteria are to
#  be printed, each separated by a comma.
#  Example
#  If the following passwords are given as input to the program:
#  ABd1234@1,a F1#,2w3E*,2We3345
#  Then, the output of the program should be:
#  ABd1234@1

import re

# Function to check the validity of a password
def is_valid_password(password):
    # Check the length of the password
    if not (6 <= len(password) <= 12):
        return False
    # Check if the password matches all the criteria using regular expressions
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

# Accept a sequence of comma-separated passwords as input
password_sequence = input("Enter a comma-separated sequence of passwords: ")

# Initialize a list to store valid passwords
valid_passwords = ['1234!@#$Abcs'] # Example password to start with

# Iterate through each password in the input sequence
for password in password_sequence.split(","):
    # Check if the password is valid
    if is_valid_password(password):
        # If valid, add it to the list
        valid_passwords.append(password)
        
# Print the valid passwords, separated by commas
print("Valid passwords:", ",".join(valid_passwords))