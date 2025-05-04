'''creation of basic encryption app,
like we will encrypt all letters by a number ,suppose we have a sentence "hello world" we have to encrypt it'''

def crypted(sentence):
 translation=""
 for element in sentence:
     if element in "Aa":
         translation+="1"
     elif element in "Bb":
         translation+="2"
     elif element in "Cc":
         translation+="3"
     elif element in "Dd":
         translation+="4"
     elif element in "Ee":
         translation+="5"
     elif element in "Ff":
         translation+="6"
     elif element in "Gg":
         translation+="7"
     elif element in "Hh":
         translation+="8"
     elif element in "Ii":
         translation+="9"
     elif element in "Jj":
         translation+="10"
     else :
         translation+=element
 return translation
         






print(crypted(input("what do you want to encrypt?")))


print("encryption can be done in easier way,lets do this")
'''Line-by-Line Explanation:

1. Function Definition:

def crypted(sentence):

Purpose: 

Usage:  



2. Initialize Translation String:

translation = ""

Purpose:  



3. Iterate Over Each Character:

for element in sentence:

Purpose:  



4. Check if Character is Alphabetic:

if element.isalpha():

Purpose: 

Note:  



5. Convert Letter to Number:

number = ord(element.lower()) - ord('a') + 1

Purpose: 

Explanation:

element.lower(): Converts the character to lowercase to ensure uniformity.

ord(element.lower()): Gets the ASCII value of the lowercase character.

ord('a'): Gets the ASCII value of 'a' (which is 97).

Subtracting ord('a') from ord(element.lower()) gives a zero-based index (e.g., 'a' → 0, 'b' → 1, ..., 'z' → 25).

Adding 1 adjusts it to a one-based index (e.g., 'a' → 1, 'b' → 2, ..., 'z' → 26).




6. Append Number to Translation:

translation += str(number)

Purpose:  



7. Handle Non-Alphabetic Characters:

else:
    translation += element

Purpose:  



8. Return Encrypted String:

return translation'''
def crypted(sentence):
    translation = ""
    for element in sentence:
        if element.isalpha():
            number = ord(element.lower()) - ord('a') + 1
            translation += str(number)
        else:
            translation += element
    return translation
print(crypted(input("what do you want to encrypt?")))


