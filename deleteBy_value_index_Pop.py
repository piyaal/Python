
food=[ "apple","juice","banana","mango","Grapes","fries","apple","juice","banana","mango","apple"]
price=[5,3,9.60,8,6,4]
#for_remove_one_element_by_value
food.remove("apple")
print(food)
#deleteByIndex
del food[3]
print(food)
#deleteByPOPIndexand PrintDeletedItem
item=food.pop(3)
print(f"remoed item is:{item}")
