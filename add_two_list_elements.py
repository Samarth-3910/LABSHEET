input_str1 = input("Enter the first list of elements of list without spaces :")
input_list1 = input_str1.split()
my_list1 = [int(num) for num in input_list1]

input_str2 = input("Enter the second list of elements of list without spaces :")
input_list2 = input_str2.split()
my_list2 = [int(num) for num in input_list2]

sum_list = []
if len(my_list1) != len(my_list2):
    print("List must have same size for element wise addition")
else:
    for i in range(len(my_list1)):
        sum_list.append(my_list1[i] + my_list2[i])
print("Sum of list is :", sum_list)