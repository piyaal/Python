#Here's a simple example to count how many times an item appears in a list:

#Using .count() Method (Built-in)

my_list = [1, 2, 3, 2, 4, 2, 5]
item_to_count = 2

count = my_list.count(item_to_count)
print(f"{item_to_count} appears {count} times.")

#Output:

#2 appears 3 times.


#With User Input Example:

my_list = []

n = int(input("Enter number of elements: "))
for i in range(n):
    my_list.append(input(f"Enter element {i+1}: "))

item_to_count = input("Enter item to count: ")
print(f"{item_to_count} appears {my_list.count(item_to_count)} times.")