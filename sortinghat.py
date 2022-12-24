print("Welcome to Hogwarts!")

question = input("Would you like to know which Hogwarts house you belong to? ")

if question.lower() != "yes":
    print("Well you are not magical anyway")
    quit()
    
print("Let's get the sorting Hat!")    

condition = input("Are you nice? y or n ")
if condition.lower() == "y":
 print("Hufflepuff!")
if condition.lower() == "n": 
 print("Slytherin") 