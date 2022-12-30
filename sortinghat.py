def game():

    print("Welcome to Hogwarts!")

question = input("Would you like to know which Hogwarts house you belong to? Type yes or no... ")

if question.lower() == "no":
    print("Well you are not magical anyway")
    quit()
if question.lower() != "no" or "yes" :
    print("I said yes or no!")
    game()
    
print("Let's get the sorting Hat!")    

condition = input("Are you nice? y or n ")
if condition.lower() == "y":
 print("Hufflepuff!")
if condition.lower() == "n": 
 print("Slytherin") 