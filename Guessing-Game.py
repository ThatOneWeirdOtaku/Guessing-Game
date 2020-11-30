import random 
import sys
mn = 0
mx = 15
targetvalue = random.randint(mn, mx)
rounds = int(input("How many rounds do you want?"))

while True:
    print(f"Guess the number! you have {str(rounds)} rounds")
    print(f"The number is inbetween {str(mn)} {str(mx)}")
    guess = input("")
    if guess == targetvalue:
        print("Congradulations you won!")
        break
    else:
        print("That was incorrect dumbass")
        rounds = rounds - 1
    if rounds <= 0:
        print("You lost noo chooiche for you")
        break

