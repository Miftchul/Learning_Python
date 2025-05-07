def is_monotonic(arr):
    """
    Check if the array is monotonic (either entirely non-increasing or non-decreasing).
    
    :param arr: List of integers
    :return: True if the array is monotonic, False otherwise
    """
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

# Test the function with an example
arr1 = [1, 2, 2, 3]  # Example of a monotonic increasing array
arr2 = [3, 2, 1]  # Example of a monotonic decreasing array
arr3 = [1, 3, 2, 4]  # Example of a non-monotonic array

print(f"Array 1: {arr1} is monotonic: {is_monotonic(arr1)}")  # Check if arr1 is monotonic
print(f"Array 2: {arr2} is monotonic: {is_monotonic(arr2)}")  # Check if arr2 is monotonic
print(f"Array 3: {arr3} is monotonic: {is_monotonic(arr3)}")  # Check if arr3 is monotonic