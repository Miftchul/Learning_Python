# Divide and Conquer Example: Merge Sort
# This program demonstrates the divide and conquer approach using the Merge Sort algorithm.
# The array is divided into halves, sorted recursively, and then merged.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def main():
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)

if __name__ == "__main__":
    main()