num = int(input("Enter the number to check if it is an Armstrong number: "))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev += digit ** 3
    temp //= 10
if num == rev:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
    