#list can be changed 
mylist=[1,"a","b",2,1]
mylist[3]="c"
print(mylist)

#append adds an element at the last of the list
mylist.append("d")
print(mylist)

#extend adds multiple elements at a time 
mylist.extend([3,4,"e",1,"f","g"])
print(mylist)

#insert use for inserting element at a given position
mylist.insert(0,"x")
print(mylist)


#pop function rem9ve the last element of list
mylist.pop()
print(mylist)


#remove use for removing the first element {
mylist.remove("e")
print(mylist)


#count the number of element occurs in a list 

list2=[1,2,1,3]
mylist=mylist+list2
print(mylist)
print(mylist.count(1))

#index use fr return the first occurance of a number
print(mylist.index(3))


#reverse a string


let=[1,2,3,"a","b","d"]
let.reverse()
print(let)