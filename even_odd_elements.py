input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

even_count = 0
odd_count = 0

for num in my_list:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

absolute_difference = abs(even_count-odd_count)
print("Absolute difference between even and odd count is :", absolute_difference)