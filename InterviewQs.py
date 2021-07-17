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

