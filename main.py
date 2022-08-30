#To get access to the random module
import random

#Defining main funtion
def main():
    """start a periodic table guessing game"""
    print("guess the element")

    element = [
       "hydrogen",
        "helium",
        "lithium",
        "berryllium",
        "boron",
        "carbon",
        "nitrogen",
        "oxygen",
        "flourine",
        "neon",
        ]

#generate random data from element variable
    x = random.choice(element)
    guess = None

#With the while loop we can execute a set of statements as long as a condition is true
    while x != guess:

        guess = str(input("What element am I thinking of? "))

#used to execute both the true part and the false part of a given condition       
        if x == guess:
            print("You guessed it right. Congratulation!".format(guess))
            break
        else:
            print("You guessed it wrong.Please try again next time!".format(guess))
            if x == "hydrogen":
                print("The atomic radium for this element is 120 pm.")
            elif x == "helium":
                print("The atomic radium for this element is 140 pm.")
            elif x == "lithium":
                print("The atomic radium for this element is 182 pm.")
            elif x == "berryllium":
                print("The atomic radium for this element is 154 pm.")
            elif x == "boron":
                print("The atomic radium for this element is 192 pm.")
            elif x == "carbon":
                print("The atomic radium for this element is 170 pm.")
            elif x == "nitrogen":
                print("The atomic radium for this element is 155 pm.")
            elif x == "oxygen":
                print("The atomic radium for this element is 152 pm.")
            elif x == "flourine":
                print("The atomic radium for this element is 135 pm.")
            elif x == "neon":
                print("The atomic radium for this element is 154 pm.")
main()