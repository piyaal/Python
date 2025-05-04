
#Retrieve value by key input


my_dict = {
    "name": "charlie",
    "age": 25,
    "city": "New York"
}

key = input("Enter the key you want to access (name/age/city): ")
print("Value:", my_dict.get(key, "Key not found"))


#Add key-value pair using input

my_dict = {}

key = input("Enter key: ")
value = input("Enter value: ")
my_dict[key] = value
key= input("Enter key: ")
value= input("Enter value: ")
my_dict[key] = value

key = input("Enter key: ")
value = input("Enter value: ")
my_dict[key] = value
key= input("Enter key: ")
value= input("Enter value: ")
my_dict[key] = value


print("Updated dictionary:", my_dict)

key=input("enter key u want to search\n")
print("value:",my_dict.get(key,"error not founy any key with your input"))