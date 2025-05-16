# Using dictionary unpacking

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Merge dict2 into dict1 using dictionary unpacking
merged_dict = {**dict1, **dict2}

# Pritn the merged dictionary
print("Merged dictionary:", merged_dict)