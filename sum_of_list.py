#                                             LAB SHEET - 5
# 1) Sum of list

input_str = input("Enter the elements of list separated by spaces : ")

input_list = input_str.split()

my_list = [int(num) for num in input_list]

list_sum = 0

for num in my_list:
    list_sum += num

print("Sum of list is : ", list_sum)