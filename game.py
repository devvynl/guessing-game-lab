"""A number-guessing game."""

# Put your code here

from random import randint

tries = 0
number = randint(1, 100)

print("Howdy, what's your name?")
name = input('>')
print(f"Hi {name}, I'm thinking of a number between 1 and 100")
print("Try to guess my number")

while True:
    guess = int(input("What is your guess?"))

    # if guess < 1 and guess > 100:
    if guess != number:
        if guess < number:
            print("your guess is too low, try again")
            tries = tries + 1
        if guess > number:
            print("your guess is too high, try again")
            tries = tries + 1
    else: 
        tries = tries + 1
        print(f"Well done, {name}! you found my number in {tries} tries!")
        break 

    # tries = tries + 1
    
# random_number = random_number.random()

# while True: 
#     user_guess = input('>')
#     random_number = random_number.random(range(1,100))
#     if user_guess != random_number:
#         if user_guess > random_number:
#             print("your guess is too high, try again") 
#         if user_guess < random_number:
#             print("your guess is too low, try again")
#     else:
#         print(f"Well done, {name}! you found my number!")

