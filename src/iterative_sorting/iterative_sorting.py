# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
    #     cur_index = i
    #     smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    for i in range(len(arr)):
        # find the minimum value remaining
        minPos = i    #  0
  
        for j in range(i+1, len(arr)):
          
          if arr[j] < arr[minPos]:

            minPos = j
    
        temp = arr[i]
        arr[i] = arr[minPos]
        arr[minPos] =temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    has_swapped = True
    count =0
    
    while(has_swapped):

        has_swapped = False

        for i in range(len(arr) - 1):
            
            if arr[i] > arr[i+1]:
                count += 1
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                has_swapped=True

    print(f"Array is sorted in {count} swaps.")
    print(f"First Elemenet: {arr[0]}")
    print(f"Last Element: {arr[len(arr)-1]}")
    return


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr


ppp= [8,7,8,6,99,100,1,3,5,85]
print(bubble_sort(ppp))