# This group of code runs a game where the user has to guess a number randomly generated from 1 to 100. If the user
# guesses the right number, or if the number is too small or too large, the program will detect and indicate the user
# the nature of their answer (if it's too low or too high). This code follows a very basic principle of functional
# programming where there is a separation of duty to each function, to make sure that each function is doing as
# simple of a task as possible. The engine will bundle all the functions together, and it will first generate the
# random number by invoking the randint function from 1 to 100. Then it will ask for the input from the user,
# before validating if the type of the input is correct, or if the input falls in the correct range or not. The while
# loop will ask and revalidate the input if it is false. Then the check_guess() function will be invoked, and it will
# take two parameters which is the user's guess, and the answer. Inside the check_guess, it will assess if the input
# is lower, higher, or just right, then it will display the correct answer. At last, the play_again() function will
# be invoked, and if Y is entered, then it will return True. If True is returned, then the While Loop will run again

import random


def engine():
    while True:
        random_number = random.randint(1, 100)                            # Generate the random number
        user_guess = input("Enter a number from 1 to 100: ")              # Ask for the input from the user
        while not validate_input(user_guess):                             # Validate the input of the user
            user_guess = input("Enter a number from 1 to 100: ")          # If it's invalid, keep asking for the input
        check_guess(user_guess, random_number)                            # Check the input of the user if it's correct
        if play_again() is False:                                         # Ask the user if they want to play again
            break                                                         # Break out of the while loop if no


def validate_input(guess):
    try:
        guess = int(guess)                                 # Use a Try statement to see if the input can be an int
        if 1 <= guess <= 100:                              # Check if the guess falls between 1 and 100
            return True                                    # Return True if the input is valid
    except:                                                # Catch the exception if the user's guess can't become an int
        pass
    print("Invalid Input")                                 # If the input is invalid, print that it's invalid
    return False                                           # Return False if it's invalid


def check_guess(guess, random_number):
    if int(guess) == random_number:                         # If the guess is the same as the random number
        print("You got the right number!")                  # Print that the user is correct!
    elif int(guess) < random_number:                        # If the guess is smaller than the random_number
        print("Your number is smaller than the answer!")    # Print that the guess is smaller than the random_Number
    else:                                                   # The else signifies that the guess is bigger than the 
        print("Your number is greater than the answer!")    # random_number 
    print("The Answer is: " + str(random_number))           # Print the correct answer


def play_again():
    choice = input("Play Again? (Y/N): ")                   # Ask the user if they want to play again
    if choice.upper() == "Y":                               # If the choice is "Y", return True
        return True
    else:                                                   # Anything else is False
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    engine()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
