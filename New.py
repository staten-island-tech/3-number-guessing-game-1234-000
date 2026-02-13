import random 
number = ["1","2","3","4","5","6","7","8","9","10"]
guess = random.choice(number)
user = input("Guess The Number: ")

user1 = []
while user1 != guess:
    input("Try again: ")
    