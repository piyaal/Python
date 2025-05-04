#What is the Fibonacci sequence?

#Each number is the sum of the two previous numbers:

#0, 1, 1, 2, 3, 5, 8, 13, 21, ...

#fibonacci with recursion

def fibonacci(n):
  if n<=0:
    return 0
  elif n==1:
   return 1
  else :
   return fibonacci(n-1)+fibonacci(n-2)


num=int(input("enter how many fibonacci number you want:\n"))
for i in range(num):
   print(fibonacci(i),end=" ")