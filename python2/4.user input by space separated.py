#single line input for space separated 
n=input("enter number by space separated")
number=n.split()
print(number)
s=input("enter char by space separated")
str=s.split()
print(str)

s2=input("enter word by space separated")
str2=s2.split()
print(str2)

str3=list(map(int,input("enter numbers by space").split()))
print(f"str3 is {str3}")