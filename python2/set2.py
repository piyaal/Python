#disjoint
a={1,2,3}
b={4,5,6} 
print(a.isdisjoint(b))
#superset
c={1,3}
d={5,6,7,8,9}
print(a.issuperset(b))
print(a.issuperset(c))
print(d.pop())#randomly delete elements from set
#union
print(c.union(d))
