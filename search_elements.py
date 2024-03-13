input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

search_element = int(input("Enter the element which is to searched : "))

found = False

for item in my_list:
    if item == search_element:
        found = True
        break

if found:
    print("Element", search_element, "found in my list.")
    print("1")
else:
    print("Element", search_element, " not found in my list.")
    print("0")
