def question():
    rules = input("You need to answer all questions by 'yes' or 'no': ").lower()
    if rules != "yes":
        print("Try again")
    else:
        print("Next question")
        ques1 = input("Are you hungry? ").lower()
        if ques1 == "yes":
            print("Let's go to a restaurant")
        else:
            print("Next question")
        
        ques2 = input("Do you want to eat pizza? ").lower()
        if ques2 == "yes":
            print("Let's order pizza")
        else:
            print("Next question")

question()