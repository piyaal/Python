#difference between sort and sorted
num=[2,10,3,26,5]
print(sorted(num))
#it returns a sorted list but doesnt modify the existing list ,thats y the num list remain unchainged
num2=[1,5,4,2,10]
num2.sort()
print(num2)

#reverse a list using sort function

#print(num2.sort(reverse=True))
'''list.sort() vs sorted()

list.sort() modifies the list in-place and returns None.

sorted() creates and returns a new sorted list without changing the original.



---

Why does print(num2.sort(reverse=True)) return None?

Because .sort() does not return the sorted list — it modifies the list directly and returns None. So when you do:

print(num2.sort(reverse=True))

You're printing the return value of .sort(), which is None. so the correct form is:
 
'''
num2.sort(reverse=True)
print(num2)
#or if we dont want to modify the list then we can use the sorted function like:
print(sorted(num, reverse=True))

'''
Here's a quick comparison table between sort() and sorted() in Python:

Example:

nums = [3, 1, 4, 1, 5]

# Using sort()
nums.sort()
print("Using sort():", nums)  # Modifies nums

# Using sorted()
nums2 = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums2)
print("Original nums2:", nums2)       # Unchanged
print("Using sorted():", sorted_nums) # New list'''
