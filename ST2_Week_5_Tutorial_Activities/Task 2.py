import random
import timeit

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        left_split = array[:len(array)//2] # Integer division
        right_split = array[len(array)//2:]

        left = merge_sort(left_split)
        right = merge_sort(right_split)        

        return merge(left, right)

        
def merge(left, right):
    merged = []

    left_pointer = 0
    right_pointer = 0

    merging = True

    while merging:

        left_element = left[left_pointer]
        right_element = right[right_pointer]

        if left_element < right_element:
            merged.append(left_element)
            left_pointer += 1
        elif right_element < left_element:
            merged.append(right_element)
            right_pointer += 1
        elif right_element == left_element: # Equal items
            merged.append(right_element)
            merged.append(left_element)
            left_pointer += 1
            right_pointer += 1

        if left_pointer >= len(left): # Reached end of left list
            merged.extend(right[right_pointer:])
            merging = False
        elif right_pointer >= len(right): # Reached end of right list
            merged.extend(left[left_pointer:])
            merging = False

    return merged

# ALGORITHMS FOR TESTING MERGE SORT AGAINST INSERTION SORT FOR BENCHMARKING

# INSERTION SORT
def insertion_sort(arr):

    # Traverse through all elements in the list, starting from the second element (index 1)
    for i in range(1, len(arr)):

        # Store the current element to be compared and inserted into the sorted part of the list
        current_element = arr[i]

        # Move elements of the sorted part of the list that are greater than the current element
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element into its correct position in the sorted part of the list
        arr[j + 1] = current_element

    return arr


#Testing MERGE SORT with INSERTION SORT

# Generate a large random list
large_random_list = [random.randint(1, 1000) for _ in range(100)]

# Compare times
insertion_time = timeit.timeit(lambda: insertion_sort(large_random_list[:]), number=10)
merge_time = timeit.timeit(lambda: merge_sort(large_random_list[:]), number=10)

print(f"Insertion Sort took: {insertion_time:.6f} seconds")
print(f"Merge Sort took: {merge_time:.6f} seconds")



# Merge and insertion sort test cases
sizes = [100, 1000, 5000]

for size in sizes:
    test_list = [random.randint(1, 1000) for _ in range(size)]

    insertion_time = timeit.timeit(lambda: insertion_sort(test_list[:]), number=10)
    merge_time = timeit.timeit(lambda: merge_sort(test_list[:]), number=10)

    print(f"\nSize: {size}")
    print(f"Insertion Sort: {insertion_time:.6f} seconds")
    print(f"Merge Sort: {merge_time:.6f} seconds")