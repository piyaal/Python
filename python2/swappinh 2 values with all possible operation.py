#variableb swap with temp

a,b=int(input("enter value of a\n")),int(input("enter a value of b\n"))
temp =a
a=b
b=temp
print(f" value of a is {a} value of b is {b}")


#using two variables

a,b=int(input("enter value of a\n")),int(input("enter a value of b\n"))
a,b=b,a
print(a,b)




#using arithmetic operation

#Here's how you can swap two variables using arithmetic operations (addition and subtraction):

a,b=int(input("enter value of a\n")),int(input("enter a value of b\n"))
a = a + b  # a becomes 15
b = a - b  # b becomes 5 (15 - 10)
a = a - b  # a becomes 10 (15 - 5)

print("a =", a)
print("b =", b)



#Alternatively, you can use multiplication and division if the values are non-zero:

a,b=int(input("enter value of a\n")),int(input("enter a value of b\n"))

a = a * b
b = a // b
a = a // b

print("a =", a)
print("b =", b)


#using x_or

a,b=int(input("enter value of a\n")),int(input("enter a value of b\n"))

a = a^ b
b = a^b
a = a^b

print("a =", a)
print("b =", b)
