for i in range(5):  
    num = int(input("Enter any number: "))
    if num >1000:
        print("Number is greater than 1000")
    elif num > 100:
        print("Number is greater than 100")
    elif num > 10:
        print("Number is greater than 10")
    elif num > 0:
        print("Number is greater than 0")
    elif num == 0:
        print("Number is equal to 0")
    else:
        print("Number is negative")
''' Using a while loop with a fixed counter

This gives the same result as the for loop, but uses while.

count = 0
times = 5  # change this number as needed'''

while count < times:
    num = int(input("Enter any number: "))
    if num > 1000:
        print("Number is greater than 1000")
    elif num > 100:
        print("Number is greater than 100")
    elif num > 10:
        print("Number is greater than 10")
    elif num > 0:
        print("Number is greater than 0")
    elif num == 0:
        print("Number is equal to 0")
    else:
        print("Number is negative")
    count += 1


#. Using an infinite loop with user choice

#This lets the user decide when to stop testing.

while True:
    num = int(input("Enter any number: "))
    if num > 1000:
        print("Number is greater than 1000")
    elif num > 100:
        print("Number is greater than 100")
    elif num > 10:
        print("Number is greater than 10")
    elif num > 0:
        print("Number is greater than 0")
    elif num == 0:
        print("Number is equal to 0")
    else:
        print("Number is negative")
    
    again = input("Do you want to try again? (y/n): ")
    if again.lower() != 'y':
        break


