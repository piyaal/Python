#GCD stands for Greatest Common Divisor, also called HCF (Highest Common Factor).
#It's the largest number that divides both numbers exactly (with no remainder).

# numbers 12 and 18: Factors of 12: 1, 2, 3, 4, 6, 12

#Factors of 18: 1, 2, 3, 6, 9, 18
#Common factors: 1, 2, 3, 6

#Greatest common factor: 6
#So, GCD(12, 18) = 6
# Using the built-in math module:

import math
a=int(input("enter a number:\n"))
b=int(input("enter a number:\n"))
gcd=math.gcd(a,b)
print("gcd of",a,"and",b,"is",gcd)



#using euclidean algorithm

a=int(input("enter 1st number:\n"))
b=int(input("enter 2nd number:\n"))
while b!=0:
   a,b=b,a%b
 
   
print("GCD is:",a)


#using for loops

a=int(input("enter 1st number:\n"))
b=int(input("enter 2nd number:\n"))
gcd=1
for i in range(1,min(a,b)+1):
  if a%i==0 and b%i==0:
    gcd=i
print("gcd is:",gcd)
