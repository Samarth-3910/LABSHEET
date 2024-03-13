input_str = input("Enter the list of elements of list without spaces :")
input_list = input_str.split()
my_list = [int(num) for num in input_list]

reversed_list = []
for num in range(len(my_list)):#kitne bar loop chalani hai uske liye range ka use karenge aur phir append se aur pop se
                               # reverse kar denge apne list ko
    reversed_list.append(my_list.pop())
print("Reversed List : ", reversed_list)