# Sort By Keys
sample_dict = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 5}

sorted_dict = dict(sorted(sample_dict.items()))

print("Sorted Dictionary by Keys:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")