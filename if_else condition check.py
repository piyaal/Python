name1 = input("What's your name:\n")
name1_money = float(input("How much money?\n"))

name2 = input("What's your name\n")
name2_money = float(input("How much money?\n"))

name3 = input("What's your name\n")
name3_money = float(input("How much money?\n"))

if name1_money > name2_money and name1_money > name3_money:
    print(f"{name1} has the most money.")
elif name2_money > name1_money and name2_money > name3_money:
    print(f"{name2} has the most money.")
elif name3_money > name1_money and name3_money > name2_money:
    print(f"{name3} has the most money.")
else:
    print("There's a tie!")