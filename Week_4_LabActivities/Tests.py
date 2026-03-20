import timeit
import random

def linear_search(array, target):

    for i in range(len(array)):
        if array[i] == target:
            return i
        
    return -1


# BINARY SEARCH
def binary_search(array, target):

    # Initialize 'pointers'
    left = 0
    right = len(array) - 1 # Account for indexing to get the right most element index
    mid = int((left + right)/2)

    while left <= right:
        if array[mid] == target: # If target is found 
            return mid
        elif target > array[mid]:
            left = mid + 1 # We already checked the mid element, so we shift the index by 1 for the next search.
        elif target < array[mid]:
            right = mid - 1

        mid = int((left + right)/2) # Recalculate mid

    return -1

# BUBBLE SORT
def bubble_sort(arr):
    # Get the length of the input list
    n = len(arr)

    # Traverse through all elements in the list
    for i in range(n):

        # Flag to optimize the algorithm
        # If no swaps are performed in an iteration, the list is already sorted, and we can stop early
        swapped = False

        # Last i elements are already in place, so we don't need to compare them again
        for j in range(0, n - i - 1):

            # Compare adjacent elements
            if arr[j] > arr[j + 1]:

                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                # Set the swapped flag to True to indicate that a swap occurred in this iteration
                swapped = True

        # If no two elements were swapped in the inner loop, the list is sorted, and we can exit early
        if not swapped:
            break

    return arr

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

# Insertion sort with linear search 