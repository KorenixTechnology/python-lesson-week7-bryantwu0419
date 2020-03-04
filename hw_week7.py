import random

def hw_week7(secret_number):
    import random
    guessesTaken = 0
    number = random.randint(1, 20)
    print('Take a guess.') 
    while guessesTaken < 6:
        guess = input()
        guess = int(guess)
        guessesTaken = guessesTaken + 1
        if guess < number:
            print('Your guess is too low.') 
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job! You guessed my number in ' + guessesTaken + ' guesses!')
    if guess != number:
       number = str(number)
       print('Nope. The number I was thinking of was ' + number)


if __name__ == '__main__':
    hw_week7(random.randint(1, 100))
