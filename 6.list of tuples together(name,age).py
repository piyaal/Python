#input a list of tuples(name,age)
n=int(input("enter number of people:\n"))
people=[]
for i in range(n):
    name=input("enter name:\n")
    age=input("enter age:\n")
    people.append((name,age))
print(people)