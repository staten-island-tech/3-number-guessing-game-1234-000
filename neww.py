import random 
number = ["1","2","3","4","5","6","7","8","9","10"]
guess = random.choice(number)


incorrect = []


user1 = ""
while user1 != int(guess):
    user1 = int(input("Guess the Number:"))
    incorrect.append(user1)
    if user1 == int(guess):
        print("The Number is", guess)
        for incorrect in incorrect:
            print(incorrect)
    else: 
        print("Wrong")
        if int(guess) > int(5):
            print("Number is greater than 5")
        else:
            print("Number is less than 5")