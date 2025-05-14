def remove_char(input_str, i ):
    # Check if the index is valid
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The remaining unchange.")
        return input_str
    
    # Remove the character at the specified index
    result_str = input_str[:i] + input_str[i+1:]
    
    return result_str

# Input String
input_str = "hello world"
i = 7 # Index of the character to remove

# Remove the character at index i
new_str = remove_char(input_str, i)

print(f"Original string: {input_str}")
print(f"String after removing character at index {i}: {new_str}")