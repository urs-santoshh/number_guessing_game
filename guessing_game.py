#welcome to numbers guessing game

import random
import math

choice = input("Do you want to play the game(Yes/No) :").capitalize()

if choice == "Yes" or choice =="Y":
    l_limit = int(input("Enter the lower limit :"))
    u_limit = int(input("Enter the upper limit :"))
    random_no = random.randint(l_limit,u_limit)
    tries = round(math.log(u_limit - l_limit + 1, 2))
    print(f"You have {tries} tries")
    play = 0

    while play < tries:
        try:
            play +=1
            guess = int(input("Enter your guess :"))
            if guess > random_no:
                print("Your guess is greater then the actual no")
            elif guess < random_no:
                print("Your guess is smaller then the actual no")
            elif guess == random_no:
                print(f"Congratulations! you have guessed correctly in {play} tries ")
                break
            else:
                raise Exception
        except:
            print("Invalid Input")
            break
    if play == tries:
        print("You couldnot guess the no ")
        print(f"The no is {random_no}")
else:
    print("Next time maybe")
