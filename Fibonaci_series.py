#fibonnaci
#factorial
#armstrong
#sorting
#prime no
#even no
#perfect no
#niven no
#buzz number

num_terms = int(input("Enter the number of terms for Fibonacci series: "))

a = 0
b = 1

print("Fibonacci Series up to", num_terms, "terms:")
print(a, end=" ")

for i in range(num_terms - 1):
    print(b, end=" ")
    a, b = b, a + b