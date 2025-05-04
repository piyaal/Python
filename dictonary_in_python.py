#dictonary in python.
#A dictionary in Python is an unordered collection of key-value pairs. It allows you to store and retrieve data using keys instead of numeric indexes (like lists or tuples).

#Key Features:

#Mutable: You can add, update, or remove key-value pairs.

#Unordered (before Python 3.7): The items are not stored in any particular order. Since Python 3.7, insertion order is preserved.

#Keys must be unique and immutable (e.g., strings, numbers, tuples).

colors={
 "B":"blue",
 "R":"red",
 "o":"Orange"

}
print(colors.get("B","error,not found"))
my_dict = {
    "name": "charlie",
    "age": 25,
    "city": "Dhaka"
}
print(my_dict["name"])  # Output: charlie
#Adding/Updating Values:

my_dict["age"] = 26        # Update value
my_dict["country"] = "Bangladesh" # Add new key-value pair


#Deleting a Key:

del my_dict["city"]
print(my_dict["country"])
