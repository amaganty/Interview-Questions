# Sorting Algorithms


#INSERTION SORT
# Best Case: O(n), Worst case: O(n^2)

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
 
 
# Driver code 
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
    
    
#BUBBLE SORT
# Best case: O(n), Worst case: O(n^2)

def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n-1):
    # range(n) also work but outer loop will repeat one time more than needed.
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
  
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
  
bubbleSort(arr)
  
print ("Sorted array is:")
for i in range(len(arr)):
    print ("% d" % arr[i])
    
   
#MERGE SORT
# Best case: O(nlogn), Worst case: O(nlogn)

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Driver Code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)

 
# SELECTION SORT
# Best case: O(n^2), Worst case: O(n^2)

import sys
A = [64, 25, 12, 22, 11]
 
# Traverse through all array elements
for i in range(len(A)):
     
    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j
             
    # Swap the found minimum element with
    # the first element       
    A[i], A[min_idx] = A[min_idx], A[i]
 
# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]),
    

# QUICK SORT
# Best case: O(nlogn), Worst case: O(n^2)

 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
