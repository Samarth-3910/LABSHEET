input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

cubed_array = [x**3 for x in my_list]
print("Cube of array are : ", cubed_array)
