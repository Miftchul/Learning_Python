from collections import OrderedDict

def check_order(string, references):
    # Create an OrderedDict from the references
    string_dict = OrderedDict.fromkeys(string)
    references_dict = OrderedDict.fromkeys(references)
    
    # Check if the keys of string_dict are in the same order as references_dict
    return string_dict == references_dict

# Input String
input_string = "Hello World"
references_string = "Helo Wrd"

# Check if the order of characters in input_string matches references_string
if check_order(input_string, references_string):
    print("The order of characters in the input string matches the references string.")
else:
    print("The order of characters in the input string does not match the references string.")