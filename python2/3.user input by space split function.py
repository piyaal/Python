n = int(input("Enter how many numbers: "))
numbers = list(map(int, input(f"Enter {n} numbers separated by space: ").split()))

# Optional: Check if user entered exactly n numbers
if len(numbers) != n:
    print(f"Error: You entered {len(numbers)} numbers instead of {n}.")
else:
    print("Numbers:", numbers)