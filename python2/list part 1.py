# list example:
mylist = [1, "a", 3.1416]
print(mylist)
print(len(mylist))


#adding two lists

list=[1,2,3]
list2=[5,"a"]
print(list+list2)

#* is used for repeatition operation

print(list2*3)

#create empty list

#list3=[]
#list4=list()


#list can be indexed and slice  in the same way as string 

#from  user  input
prime=[]
n=int(input("enter how many numbers?"))
for i in range (n):
  num=input("enter prime numbers")
  prime.append(num)
#prime=2,3,5,7,11,13,17

print(prime[1])
print(prime[3:])
print(prime[:3])
print(prime[2:5])
print(prime[::-1])

