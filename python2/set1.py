myset={1,2,4,3}
print(myset)
myset2=set([1,2,3,6,5])
print(myset2)
print(1 in myset)
print(7 in myset2)
s1=set()
print(s1)#returns an empty set
#add operation
a={1,2,3}
a.add(4)
print(a)

#copy a set
a={5,6,7}
b=a.copy()
print(b)

#difference
c={5,7,6,8,9}
d={3,4,5,6}
print(c.difference(d))


#discard

a={1,2,3,4}
b={3,4,5,6}
a.discard(2)
print(a)


#intersection
c=a.intersection(b)
print(c)
