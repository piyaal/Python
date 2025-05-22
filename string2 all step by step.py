
#string
print("abc")
print("abc"*3)#abc*3times
print("i love 'python'!")
print("abc"+"def") #concatination

#new line \n  \t 4use
print("abc\ndef")
print("abc\tdef")
str1="abcdef"
print(str1[1])
#minus for reverse value
print(str1[-1])
print(str1[-2])
#range
str="abcdefgh"
print(str1[1:4])
print(str[2:])
print(str[:3])
#start:stop:range
print(str[::2])
print(str[1:8:2])
#reverse range
print(str[7:1:-2])
print(str[::-1])
print(str.upper())
print(str.lower())
print(str.capitalize())
#replace a letter

strr="bcdefh xyz"

print(strr.replace("c","d"))
#two letter replace
strr=strr.replace("c","x")
strr=strr.replace('d','x')
print(strr)


#replace using Using str.translate() for multiple letter replacements
text = "apple"
trans= str.maketrans({'a': 'x', 'e': 'y'})
text = text.translate(trans)

print(text)  # Output: xpply


#split words

text="i love python"
print(text.split())



#replace muliple letter 


#Using a dictionary for replacement

text = "banana"
replacements = {'a': '1', 'b': '2'} 

# Create translation table
table = str.maketrans(replacements)

# Apply replacements
new_text = text.translate(table)

print(new_text) 

#from user input

text = input("Enter a string: ")
char1 = input("Character to replace: ")
replace1= input("Replace with: ")
char2 = input("Another character to replace: ")
replace2= input("Replace with: ")

# Create translation table from user input
func= str.maketrans({char1: replace1,char2: replace2})
new_text = text.translate(func)

print("Result:", new_text)


#count of occurance in a string 

str=input("enter for counting occurnce")
print(str.count("a"))


#find index of a substring

text=input('substring')
print(text.index('lo'))