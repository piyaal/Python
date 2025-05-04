'''we will create today a testing combination of 3 meals,3 drinks, 3 dessert ,we will see all the possible combination that can exists with these'''

meal=["pizza","burger","chicken"]
drink=["water","juice","cola"]
dessert=["cake","ice cream","chips"]
for m in meal:
   for d in drink:
      for ds in dessert:
          print(f"i will've {m} as a meal ,{d} as a drink and {ds} as a dessert")d
          
          

print("using itertools product")
#Alternative Approach Using itertools.product:

 

from itertools import product

meal = ["pizza", "burger", "chicken"]
drink = ["water", "juice", "cola"]
dessert = ["cake", "ice cream", "chips"]

for m, d, ds in product(meal, drink, dessert):
    print(f"I will have {m} as a meal, {d} as a drink, and {ds} as a dessert.")

         
