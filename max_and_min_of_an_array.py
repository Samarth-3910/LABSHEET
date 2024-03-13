input_str = input("Enter the list of elments of list without spaces : ")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

max_values = my_list[0]
min_values = my_list[0]

for num in my_list:
    if num > max_values:
        max_values = num
    if num < min_values:
        min_values = num
print("Min value is :", min_values)
print("Max Values is :", max_values)