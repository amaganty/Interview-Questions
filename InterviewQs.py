# Interview Questions (Algorithms) 

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

#Check if String is a Palindrome

string=input("Enter a string:")
if (string==string[::-1]):
    print ("This is a Palindrome!")
else:
    print ("This is not a Palindrome")
