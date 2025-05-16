# simple Dictionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

# Initialize an empty set to store unique values
total_sum = 0

# Iterate through the values of the dictionary
for i in my_dict.values():
    # Add each value to the set
    total_sum += i
    
# Print the unique values
print("Total sum of values in the dictionary:", total_sum)