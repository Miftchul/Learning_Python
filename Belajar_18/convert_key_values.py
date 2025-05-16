key_values_list = [('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]

# Initialize an empty dictionary
float_dict = {}

# Iterate through the list of tuples
for key, value in key_values_list:
    # Add each key-value pair to the dictionary
    float_dict[key] = value
    
# Print the resulting dictionary
print("Dictionary from key-value pairs:", float_dict)