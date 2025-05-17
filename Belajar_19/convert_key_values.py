key_value_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]

# Initializing an empty dictionary
flat_dict = {}

# Iterating through the list of tuples
for key, value in key_value_list:
    # Adding each key-value pair to the dictionary
    flat_dict[key] = value
    
# Printing the resulting dictionary
print("Flat Dictionary:", flat_dict)