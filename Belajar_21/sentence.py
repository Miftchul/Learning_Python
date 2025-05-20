# Write a program that accepts a sentence and calculate the number of letters and
#  digits. Suppose the following input is supplied to the program:
#  hello world! 123
#  Then, the output should be:
#  LETTERS 10
#  DIGITS 3

# Accept a sentence as input
sentence = input("Enter a sentence: ")
# Initialize counters for letters and digits
letter_count = 0
digit_count = 0

# Iterate through each character in the sentence
for char in sentence:
    # Check if the character is a letter
    if char.isalpha():
        letter_count += 1
    # Check if the character is a digit
    elif char.isdigit():
        digit_count += 1
# Print the counts of letters and digits
print("LETTERS", letter_count)
print("DIGITS", digit_count)
