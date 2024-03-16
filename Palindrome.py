num = int(input("Enter the number to check if it is an Palindrome number: "))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if num == rev:
    print("Palindrome Number")
else:
    print("Not an Palindrome Number")
