#input list of dictonnaries (key:value)
n=int(input("enter how many items?"))
data=[]
for i in range (n):
   key=input("enter key value\n")
   value=input("enter value\n")
   data.append({key:value})
print(data)