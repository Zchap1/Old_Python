print ("\tWelcome to 'guess my numer'!")
print ("\n I'm thinking of a number between 1 and 1000.")
print ("Try to guess it in as few attempts as possible.\n")

# set the initial values
import random
the_number = random.randint(1, 1000)
#guess = int(input("take a guess: "))
guess = 0
tries = 0
#guessing loops5
while guess != the_number:
     guess = int(input("take a guess: "))
     tries += 1
     if guess > the_number:
        print ("lower...")
     else:
        print ("higher...")
        

print (" You guessed it! The number was",the_number)
print ("And it only took you ",tries, "tries.")
input("\n\n\tPress the enter key to exit.")
