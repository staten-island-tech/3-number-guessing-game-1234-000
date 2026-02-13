import random 
number = ["1","2","3","4","5","6","7","8","9","10"]
guess = random.choice(number)


Guess_history = []


user1 = ""
while user1 != int(guess):
    user1 = int(input("Guess the Number:"))
    Guess_history.append(user1)
    if user1 == int(guess):
        print("The Number is", guess)
        for Guess_history in Guess_history:
            print("Your Wrong Guesses",Guess_history)
    else: 
        print("Wrong")
        if int(guess) > int(5):
            print("Number is greater than 5")
        else:
            print("Number is less than 5")