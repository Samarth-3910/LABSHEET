input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

squared_array = [x**2 for x in my_list]
print("Square of array are : ",squared_array)