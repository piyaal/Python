dict2={}
print(dict2)
dict1=dict()
print(dict1)

#input
dict3={"x":1, "y":2, "z":3}
#add new key value to dict
dict3["u"]=10
#overwrite
dict3["y"]=20
print(dict3)
#get input value by key
print(dict3["x"])

print(dict3.get("u"))

#return value, a is not a key so return none
print(dict3.get("a"))
# if you want to return a default value and its key is not present then )
print(dict3.get("a",42))
#will cause a key error because w is not a key
#print(dict3["w"])