from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict([('b', 2), ('a', 1), ('c', 3), ('d', 4), ('e', 5)])

# Item to be added
new_items = ('a', 1)

# Create a new ordered dictionary with the new item at the beginning
new_ordered_dict = OrderedDict([new_items])

# Merge the new OrderedDict with the existing one
new_ordered_dict.update(ordered_dict)

# Print the updated OrderedDict
print("Updated OrderedDict:", new_ordered_dict)

