def find_words(words, k):
    # Create a list to store the indices of the occurrences of 'world'
    result = []
    
    # Iterate through the list of words
    for i in words:
        # Check if the word is 'world'
        if i in words:
            # Check if the length of the word is greater than k
            if len(i)> k:
                # Append the index of the word to the result list
                result.append(i)
            
    return result

# Example usage
word_list = ["hello", "world", "python", "world", "code"]
k = 2
long_words = find_words(word_list, k)

print(f"Words longer than {k} characters: {long_words}")