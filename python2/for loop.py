#disply number which are divided by 4 & 5 in 1 to 100
i=1
while(i<=100):
  if(i%4==0 and i%5==0):
    print(i,end=" ")
  i+=1
  
  
#count of digits in a number
num=int(input("enter a number"))
c=0
while(num>0):
 c+=1
 num//=10
 
print(c)

#factorial of a num

num=int(input("enter a number:\n"))
fact=1
for i in range (1,num+1):
    fact*=i
print(fact)