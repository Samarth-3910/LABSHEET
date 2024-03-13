input_str = input("Enter the list of elements without spaces : ")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

B = int(input("Enter a number which is to be added to the list : "))

result_array = []

for num in my_list:
    result_array.append(num + B)
print("Result Array :", result_array)