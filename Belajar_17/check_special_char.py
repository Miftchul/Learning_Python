import re

def check_special_char(in_str):
    # Define a regular expression pattern to match special characters
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    # Use re.search to find a match in the input string
    return bool(re.search(pattern, in_str))

# Input a string
input_string = input("Enter a string: ")

# Check if the string contains any special characters
if check_special_char(input_string):
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
