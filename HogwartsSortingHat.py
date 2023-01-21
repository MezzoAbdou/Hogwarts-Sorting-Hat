def game():
    def response1():
        print("Let's get the sorting Hat!")   

    #welcome statement
    print("Welcome to Hogwarts!")
    
    

    
    #User input to enter process
    question = input("Would you like to know which Hogwarts house you belong to? Type yes or no... ")

##    #compare answers, and continue process
    if question.lower() == "yes":
           response1()
    if question.lower() == "no":
          print("Well you are not magical anyway")
          quit()
    if question.lower() != ("no" or "yes") :
          print("I said yes or no! Try again!")
          game()   
   
##
##    #question 2
##    condition = input("Are you nice? y or n ") 
##    if condition.lower() == "y":
##        print("Hufflepuff!")
##    if condition.lower() == "n": 
##        print("Slytherin")
game()
      
