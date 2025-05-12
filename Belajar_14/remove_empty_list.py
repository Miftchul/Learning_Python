# Sample list of even numbers
list_of_list = [[], [1, 2], [], [3, 4], [], [5, 6], []]

# Using list comprehension to remove empty lists
filtered_list = [i for i in list_of_list if i]

# Print the filtered list
print("List after removing empty lists:", filtered_list)