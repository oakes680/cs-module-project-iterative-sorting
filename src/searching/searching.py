def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
            
    return -1



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if target == arr[middle]:
            return middle
        else:
            if target < arr[middle]:
                right = middle - 1
            else:
                left = middle +1
 

    return -1  # not found
