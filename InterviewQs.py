# Interview Questions (Data Structures and Algorithms) 

# Check if Number is a Palindrome

num = int(input("Enter a number:"))
temp  = num
reverse = 0
while (num > 0):
    dig = num%10
    reverse = reverse*10 + dig
    num = num//10
if (temp == reverse):
    print ("Number is a palindrome!")
else:
    print ("Number is NOT a palindrome")

# Check if String is a Palindrome

