n = int(input("Enter number of elements for the list:\n"))
numbers = [int(input(f"Enter number {i+1}:\n")) for i in range(n)]

print(f"Minimum number in list is {min(numbers)}, maximum number is {max(numbers)}")
print(sorted(numbers))