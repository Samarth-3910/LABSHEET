num = int(input(" Enter the number of terms for Perfect Number: "))
b = 0
for i in range(1, num):
    if num % i == 0:
        result = b + i

if result == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
