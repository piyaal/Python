#input from key board
dict={}
key=input("enter key value")
value=input("enter value")
dict[key]=value
print(dict)
#Input multiple key-value pairs using a loop

my_dict = {}
n = int(input("How many items do you want to add? "))

for i in range(n):
    key = input(f"Enter key {i+1}: ")
    value = input(f"Enter value for '{key}': ")
    my_dict[key] = value

print("Final dictionary:", my_dict)
