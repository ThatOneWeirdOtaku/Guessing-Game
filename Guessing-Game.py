import random
import time

MN = 0
MX = 15
TARGETVALUE = random.randint(MN, MX)
ROUNDS = int(input("How many rounds do you want? "))

while True:

    print(f"Guess the number! You have {str(ROUNDS)} rounds left ")
    print(f"The number is inbetween {str(MN)} {str(MX)}")
    GUESS = input("")

    if str(GUESS) == str(TARGETVALUE):
        print("Congradulations you won!")
        time.sleep(2)
        break
    else:
        print("That was incorrect, dumbass")
        ROUNDS -= 1
    if ROUNDS <= 0:
        print("You lost, no chooiche for you")
        time.sleep(2)
        break

