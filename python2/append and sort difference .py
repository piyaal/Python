#list element can be changed by assigning a new element at a given index
mylist=[1,"a","b",4]
#mylist[4]="c" will be out of range for inserting value beacuse mylist has 0 to 3 value. we have to use append

#sort function doesnt work for two different data types like string and int print(sort(mylslist)) will not work
mylist2=["d","b"]
mylist2.append("c")
print(sorted(mylist2))