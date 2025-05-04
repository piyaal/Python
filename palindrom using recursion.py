
#palindrom using recursion
'''Step-by-Step Execution:

1. is_palindrome("level")

First and last: 'l' == 'l' → OK

Call is_palindrome("eve")



---

2. is_palindrome("eve")

First and last: 'e' == 'e' → OK

Call is_palindrome("v")



---

3. is_palindrome("v")

Length is 1 → Base case hit

Return True



---

Returning Back:

Step 3 returns True → so Step 2 also returns True

Step 2 returns True → so Step 1 also returns True



---

Final Output:

"level" is a palindrome

What does s[1:-1] mean?

It takes a substring of s starting after the first character and ending before the last character.

Example:

If s = "level":

s[0] = 'l' (first character)

s[-1] = 'l' (last character)

s[1:-1] = 'eve' → the middle part


So:

s = "level"
s[1:-1]  # → "eve"


---

Why is it used in the palindrome function?

You're checking the outer characters (s[0] and s[-1]) first. If they match, you then check if the inner part is also a palindrome — this is done recursively using s[1:-1].


---

Visual Example:

is_palindrom("racecar")
→ s[0] = 'r', s[-1] = 'r' → match
→ call is_palindrom("aceca")

is_palindrom("aceca")
→ s[0] = 'a', s[-1] = 'a' → match
→ call is_palindrom("cec")

...
→ eventually reach 1 character → base case → True'''

def is_palindrom(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrom(s[1:-1])
 


word=input("enter a word :\n")
if is_palindrom(word):
    print(f"{word} is a palindrom")
else :
     print(f"{word} is not a palindrom")
f