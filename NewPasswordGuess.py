# Programmer: Audrey Cooper & AJ Funk
# Purpose: To write a program that guesses a 3 digit password.
# Written for Jane's Science Fair Project 2019.

# import random to use the random function
'''
the random function allows us to tell the computer to guess a random number
the random function is actually "pseudorandom" which is not a true random number,
at least to the computer. To us humans it seems pretty random.
'''
import random

# instantiate setPassword function
'''
This function will set the password, perform input validation, and then
return the set password. 
'''
def setPassword():
    # use a while loop to keep the loop running until the user breaks it. 
    while True:
        # use a try except block for user input validation
        try:
            # prompt and collect user input
            code = input("Please enter a 3 digit password: ")
            # use an if statement to ensure password meets all conditions
            '''
            This statement states that if the length of the password is 3,
            the code is greater or equal than 0, and less than 1000, the code
            meets all requirements and the program can continue. Otherwise,
            an exception is thrown and the input will be taken again.
            '''
            if (len(code) == 3 and int(code) >= 0 and int(code) < 1000):
                return code
            else:
                # if code doesn't meet requirements, invalid message
                print("That was not a valid password. Please try again.")
        except:
            # if code doesn't meet requirements, throw an exception (error)
            print("That was not a valid password. Please try again.")

'''
Note: If you want, you can make an input validation function and call it instead
of printing that the password was invalid. This way you can practice calling
functions in the correct places!
'''

# instantiate guessPassword function
'''
This function *randomly* guesses from all of the possible passwords and counts
the number of attempts that it took. Then, it returns the guessed password
and the number of attempts it took.
'''
def guessPassword(givenInfo):
    # instantiate numAttempt - the number of guessing attempts
    '''
    This number is set equal to 0 and will be incremented (add 1) each time this
    loop performs one iteration. Once the password is guessed, this variable
    will be equal to the number of attempts it took to guess the password.
    '''
    numAttempt = 0
    # instantiate array codeList
    '''
    This is an array, or a list of all the passwords the computer is going to try
    to guess. Right now it is empty, but as the computer iterates through each
    number, it will append and delete each number as necessary until the numbers
    in the array match the given password.
    '''
    codeList = []

    # use a for loop to iterate through the elements of the array
    # there are 3 for loops - 1 for each digit of the password
    # each iteration, it adds a 3 digit number to the possible combinations list
    for x in range(10):
        for y in range(10):
            for z in range(10):
                codeList.append(str(x) + str(y) + str(z))

    # use a while loop to keep the loop operating as long as a condition is met
    # this loop will be broken as soon as the given condition is no longer met
    while True:
        '''
        This operation instantiates variable choice and sets it equal to a
        random choice from the codeList (the list of possible combinations)
        '''
        choice = random.choice(codeList)
        # this operation removes the incorrect guesses from the list 
        codeList.remove(choice)
        '''
        For each iteration of this process, the variable numAttempt is
        incremented (add 1 to it) so that we know the number of attempts
        that it took.
        '''
        # this operation is just coding shorthand for numAttempt = numAttempt + 1
        numAttempt += 1
        '''
        Here, we use an if statement to compare the choice to the given
        password. If they are equal, the password and the number of attempts
        taken are returned.
        '''
        if choice == givenInfo:
            return choice, str(numAttempt)

# main program
'''
In the main program, we format our program by calling the functions from above
in an appropriate order to solve our problem.
'''
# saves variable 'password' as input given from the user
password = setPassword()
'''
Saves the guessed password and number of attempts from the
function to guess it with only giving it the actual password.
'''
guessWord, attempts = guessPassword(password)
# prints the guessed password (not the real one to show they are the same)
print("The password is: " + guessWord)
# Prints the number of attempts it took to guess the real password
print("The number of attempts to guess it is: " + attempts)

