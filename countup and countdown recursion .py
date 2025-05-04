#count up and countdown numbers 
#countdown 5,4,3,2,1,blast off
#countup 1,2,3,4 up to target
def countdown(n):
 if n==0:
  print("blast off")
 else:
   print(n)
   return countdown(n-1)
num=int(input("enter a number:\n"))
countdown(num)

def countup(current,target):
 if current>target :
   return
 else:
   print(current)
   return countup(current+1,target)
num2=int(input("enter a number"))
countup(1,num2)