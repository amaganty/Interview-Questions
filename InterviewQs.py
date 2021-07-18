# Interview Questions (Algorithms) 

# # Check if Number is a Palindrome

# num = int(input("Enter a number:"))
# temp  = num
# reverse = 0
# while (num > 0):
#     dig = num%10
#     reverse = reverse*10 + dig
#     num = num//10
# if (temp == reverse):
#     print ("Number is a palindrome!")
# else:
#     print ("Number is NOT a palindrome")

# #Check if String is a Palindrome

# string=input("Enter a string:")
# if (string==string[::-1]):
#     print ("This is a Palindrome!")
# else:
#     print ("This is not a Palindrome")


# Reverse an Integer and check for overflows

# def reverse(x):
#     if x > 0: #for positives
#          a = int (str(x)[::-1])
#     if x <= 0: #for negatives
#         a = -1 * int(str(x*-1)[::-1])
        
#     # to handle the overflow
#     mina = -2**31
#     maxa = 2**31 - 1
#     if a not in range(mina, maxa):
#         return 0
#     else :
#         return a 
# print(reverse(123))


# ARRAY MANIPULATION AND SUM

# Given an array arr[] of N integers and an integer S. 
# The task is to find an element K in the array such that if all the elements from the array > K are made equal to K,
#then the sum of all the elements of the resultant array becomes equal to S.
# If it is not possible to find such an element then print -1 .

# Examples: 
# Input: M = 15, arr[] = {12, 3, 6, 7, 8} 
# Output: 3 
# Resultant array = {3, 3, 3, 3, 3} 
# Sum of the array elements = 15 = S
# Input: M = 5, arr[] = {1, 3, 2, 5, 8} 
# Output: 1 


# Python3 implementation of the approach
 
# Function to return the required element
def getElement(a, n, S) :
     
    # Sort the array
    a.sort();
 
    sum = 0;
 
    for i in range(n) :
         
        # If current element
        # satisfies the condition
        if (sum + (a[i] * (n - i)) == S) :
            return a[i];
             
        sum += a[i];
 
    # No element found
    return -1;
 
# Driver Code
if __name__ == "__main__" :
     
    S = 5;
    a = [ 1, 3, 2, 5, 8 ];
    n = len(a) ;
 
    print(getElement(a, n, S)) ;

