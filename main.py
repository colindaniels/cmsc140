from random import randrange

game_history = []

def run_game():
    number = randrange(1, 101)
    number_of_guesses = 0
    while True:
        guess = int(input('Guess the number between 1 and 100\n'))

        number_of_guesses += 1

        if guess > number:
            print('Too high')
        elif guess < number:
            print('Too low')
        elif guess == number:
            print(f'YOU WON! THE NUMBER WAS {number}')
            game_history.append(number_of_guesses)
            break
    if prompt_play_again():
        return run_game()
    else:
        print('EXITING')
        return


def prompt_play_again():
    play_again = input('Would you like to play again? [ y or n ]\n')
    if play_again == 'y':
        return True
    elif play_again == 'n':
        return False
    else:
        print('**Invalid Input**')
        return prompt_play_again()


run_game()