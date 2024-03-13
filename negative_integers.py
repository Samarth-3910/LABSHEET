input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

print("Negative integers in the list are: ")
for num in my_list:
    if num < 0:
        print(num)