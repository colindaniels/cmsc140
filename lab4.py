# Colin Daniels, Adam Bruce, Annika Urness, Cristian Tallarico
# Typing and general outline of code.

battleBoard = {
    "A": [".", ".", "."],
    "B": [".", ".", "."],
    "C": [".", ".", "."],
}

def print_board(board):
    print('Current Board\n')
    print("     A    B    C")
    for i in range(len(board.values())):
        print(str(i+1) + "    " + board["A"][i] + "    " +  board["B"][i] + "    " + board["C"][i])


def play_battleship(board):
    print('Welcome to Battleship!')
    coords = input('Player 1, select a column and row for your battleship\n')
    col, row = coords.split(',')
    row = int(row) - 1
    print_board(board)

    guesses = 0

    while True:
        guesses += 1
        guess_coords = input('Player 2, select a column and row for your guess\n')
        guess_col, guess_row = guess_coords.split(',')

        guess_row = int(guess_row)-1

        if (col, row) == (guess_col, guess_row):
            print('You Won!')
            board[guess_col][guess_row] = 'X'
            break
        else:
            print('Sorry, nothing there.')
            board[guess_col][guess_row] = '!'
        print_board(board)

    print_board(board)
    print(f'Score: {guesses} Guesses')


play_battleship(battleBoard)
