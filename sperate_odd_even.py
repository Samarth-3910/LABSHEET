input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

even_numbers = []
odd_numbers = []

for num in my_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers are : ", even_numbers)
print("Odd numbers are : ", odd_numbers)