def calculation(a, b, c, d):
    print("Sum:", a + b + c + d)
    print("Subtraction:", a - b - c - d)
    
    return  # Function exits here, so nothing after this line runs
    
    print("Multiplication:", a * b * c * d)  # This will NOT run

# Call the function
calculation(1, 2, 3, 4)