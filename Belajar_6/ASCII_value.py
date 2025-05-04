# ASCII value:
#  ASCII, or American Standard Code for Information Interchange, is a character encoding
#  standard that uses numeric values to represent characters. Each ASCII character is
#  assigned a unique 7-bit or 8-bit binary number, allowing computers to exchange information
#  and display text in a consistent way. The ASCII values range from 0 to 127 (for 7-bit ASCII)
#  or 0 to 255 (for 8-bit ASCII), with each value corresponding to a specific character, such as
#  letters, digits, punctuation marks, and control characters.

char = str(input("Enter a character: "))
print("The ASCII value of '" + char + "' is", ord(char))