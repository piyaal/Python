
#Recursion is a programming technique where a function calls itself to solve a problem
# Recursion is when a function solves a problem by calling a smaller version of itself until it reaches a base case, then returns the result.
#Two key parts of recursion:

#1. Base case – the simplest case, where recursion stops.
#2. Recursive call – the function calls itself with a smaller input.


#factorial of a number

n=int(input("enter a number:\n"))
factorial=1
if n<0:
  print("cant find factorial of a negative number")
else:
    for i in range(1,n+1):
      factorial*=i
    print("factorial of ",n, "is",factorial)
  
  
 #factorial using recursion
def facto(n):
   if n<0 :
    print("cant find factorial of negative number")
    return 0
   elif n==0 or n==1 :
     return 1
   else :
     return n*facto(n-1)
n=int(input("enter a number:\n"))
fact=facto(n)
print(f"factorial of {n} is",fact)
