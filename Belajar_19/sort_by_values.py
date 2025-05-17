# Sort by Values
sample_dict = {'apple': 5, 'banana': 2, 'cherry': 3, 'date': 4, 'elderberry': 1}
sorted_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1]))

print("Sorted Dictionary by Values:")
for key, value in sorted_dict.items():
    print(f"{key}: {value}")