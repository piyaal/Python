'''our_pass = "1916"
your_ans = ""
num_of_try = 0
num_of_max_try = 4
max_try = "not reached"

while your_ans != our_pass and max_try != "Reached":
    if num_of_try < num_of_max_try:
        your_ans = input("What is the password? ")
        num_of_try += 1
    else:
        max_try = "Reached"

if max_try == "Reached":
    print("Account blocked")
else:
    print("Access Granted")
Consider the following Python code:

our_pass = "1916"
your_ans = ""
num_of_try = 0
num_of_max_try = 4
max_try = "not reached"

while your_ans != our_pass and max_try != "Reached":
    if num_of_try < num_of_max_try:
        your_ans = input("What is the password? ")
        num_of_try += 1
    else:
        max_try = "Reached"

if max_try == "Reached":
    print("Account blocked")
else:
    print("Access Granted")

If the user enters the following inputs:

Attempt 1: 1234
Attempt 2: 0000
Attempt 3: 1916

What will be the output?

A. Account blocked

B. Access Granted

C. Account blocked followed by Access Granted

D. No output


---

Answer:

B. Access Granted

Explanation:

The user is allowed up to 4 attempts (num_of_max_try = 4).

On the third attempt, the user enters the correct password "1916".

Since the correct password is entered before reaching the maximum number of attempts, the loop exits, and the program prints Access Granted
'''    
    
 
our_pass = "1916"
your_ans = ""
num_of_try = 0
num_of_max_try = 4
max_try = "False"

while your_ans != our_pass and max_try != "True":
    if num_of_try < num_of_max_try:
        your_ans = input("What is the password? ")
        num_of_try += 1
    else:
        max_try = "True"

if max_try == "True":
    print("Account blocked")
else:
    print("Access Granted")
       
       
