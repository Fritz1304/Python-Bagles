import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Welcome to Bagles!
          
          I am thinking of a {}-digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say: That means:
          Pico One digit is correct but in the wrong position.
          Fermi One digit is correct and in the right position.
          Bagels No digit is correct.
          
          
          For example, if the secret number was 248 and your guess was 843, the
          clues would be Fermi Pico.'''.format(NUM_DIGITS))
    
    while True: # Main game loop
        secret_number = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        numGuesses = 1

        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secret_number)
            print(clues)
            numGuesses += 1

            if guess == secret_number:
                break # They're correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_number))

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # Shuffle them into random order.
    # Get the first NUM_DIGITS digits in the list for the secret number:
    secret_number = ''

    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number
    
def getClues(guess, secret_number):
    """Returns a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secret_number:
        return 'You got it!'
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secret_number:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
            return 'Bagels' # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()            # Make a single string from the list of string clues.
        return ' '.join(clues)
        
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

