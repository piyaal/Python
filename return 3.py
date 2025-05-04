def calculation(a, b, c, d):
    sum_result = a + b + c + d
    sub_result = a - b - c - d
    print("Sum:", sum_result)
    print("Subtraction:", sub_result)
    return  # ends function, does not return 

# Take input from user FIRST
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
d = int(input("Enter value for d: "))

# Call the function
calculation(a, b, c, d)

# Multiplication outside the function
mul = a * b * c * d
print("Multiplication:", mul)