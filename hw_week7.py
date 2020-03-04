import random
def hw_week7(secret_number):
    import random
    guessesTaken = 0
    while guessesTaken < 6:
        print('Take a guess.') 
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < secret_number:
            print('Your guess is too low.') 
        if guess > secret_number:
            print('Your guess is too high.')
        if guess == secret_number:
            break
    if guess == secret_number:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')

if __name__ == '__main__':
    hw_week7(15)
