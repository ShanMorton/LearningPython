import random
guess = int(input("What number would you like to guess between 1 and 100.\n"))

print(f"Your guess is {guess} \n")

correct_guess = random.randint(1,100)
guess_count = 1

while guess != correct_guess:
    guess_count +=1
    if guess > correct_guess:
        print(" Guess again but lower! \n")
    else:
        print(" Guess again but higher! \n")
    guess = int(input("What number would you like to guess now?? \n"))
else:
    print(f"You guessed the corret number {correct_guess}! \n Well done! \n")
    print(f"It took you {guess_count} times to get the correct number! \n")
    
