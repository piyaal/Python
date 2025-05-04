#print colors from a list

colors=["blue","red","orange","black"]
for x in colors:
    print(x)

    
 #print lettee in a string           
for l in "green" :
    print(l)   
    
    
#break statement    
colors2=["blue","red","orange","black", "green"]
for x in colors2:
    print(x)
    if x=="orange":    
       break
 #print 0 to range-1      
 # Print 0 to range-1      
for number in range(7):
    print(number)
   
# Print from specific range to low to high-1
for n in range(20, 30):
    print(n)
    

#sum  of 5 numbers
 # Sum of 5 numbers
total = 0
for i in range(5):
    num = int(input("Enter a number:\n"))
    total += num
print("Sum of 5 numbers is:", total)