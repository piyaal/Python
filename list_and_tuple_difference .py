#difference between tuple and list
# List example
my_list = [1, 2, 3,4]
my_list[0] = 20  # This is allowed
my_list.append(10)
my_list.insert(5,33)
print("List:", my_list)  # Output: [20, 2, 3, 4,10]

# Tuple example
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise TypeError
print("Tuple:", my_tuple)  # Output: (1, 2, 3)