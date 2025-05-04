variable="apple"
food=["apple","juice","banana","mango","Grapes","fries"]
price=[5.55,3.28,9.60,8,6,4]
print(food)
food.insert(2,"rice")
food.extend(price)
print(food)
print(food.index("juice"))
print ("one item from list")
print(food[2])
print("from one item to last items like 3rd index to last")
print(food[3:])