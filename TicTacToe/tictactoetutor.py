 #Starts here
# init vars
# init board
board = [' ' for x in range(10)]


# The board layout
def board_layout(board):

    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

    print('-----------')

    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

    print('-----------')

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])



# Defines human move, move will be player input
def human_move():
    run = True
    while run:
        move = input('Place your X, select 1-9 ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if free(move):
                    run = False
                    letter('X', move)
                else:
                    print('Position taken!')
            else:
                print('Number out of range!')
        except:
            print('Only type numbers!')
# Letter and position is the label
def letter(letter, pos):
    board[pos] = letter

# Defines the AI move, the move will be random choice
def ai_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winner(boardCopy, let):
                move = i
                return move

    open_corners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)

    if len(open_corners) > 0:
        move = random_choice(open_corners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    open_sides = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            open_sides.append(i)

    if len(open_sides) > 0:
        move = random_choice(open_sides)

    return move

# All possible ways to win
def winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
            bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                   bo[2] == le and bo[5] == le and bo[8] == le) or (
                   bo[3] == le and bo[6] == le and bo[9] == le) or (
                   bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


# Defines how random choice works
def random_choice(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# If position is ' ', it's free
def free(pos):
    return board[pos] == ' '

# If there is 0 ' ' positions, board is full
def full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# Asks the player if they want to start by asking for an input
def start_game():
    answer = input('\nStart the game? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        # board = [' ' for x in range(10)]
        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
    else:
        print("Leaving imulation, have a nice day!")


# Asks the player if they want to play again by asking for an input
def play_again():
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        # board = [' ' for x in range(10)]
        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
        main()
    else:
        print("Leaving Simulation, have a nice day!")


def main():
    # Prints an introduction, rules and an example board to help the user understand position numbers
    print('Welcome to Human vs AI Tic Tac Toe')
    print('\nRules: Pick 1-9 to try and get three X in a line')
    print('\nBoard: ')

    print(''  '1 | 2 ' '| 3')
    print('' '4 | 5 ' '| 6')
    print('' '7 | 8 '  '| 9')

    start_game()

    print('\nGame Starts!')
    print('AI goes first.\n\n')

    # While the board still has a place to move
    while not (full(board)):

        # If Human 'x' has not won, the let AI move.
        if not (winner(board, 'X')):
            # Get Move from AI
            move = ai_move()
            # Evaluate AI move
            if move == 0:
                # Board is full after AI moved
                print('Tied game!')
            else:
                # Put AI 'o' move on the board
                letter('O', move)
                print('AI placed an O on', move, ':')
                board_layout(board)
        else:
            # Human 'X' has already won! AI does not get a move.
            print('Human wins the game!')
            break
            # If AI 'o' has not won, then let human move
        if not (winner(board, 'O')):
            # Get human move here
            human_move()
            # Print out board after human has moved.
            board_layout(board)
        else:
            # AI 'o' has won the game, game over!
            print('AI wins the game!')
            break
    # If board is full and no there is no winner, game is a tie
    if full(board):
        print('Tied game!')
    # Runs play again function which asks player if they want to play again
    play_again()


# Program starts here
# Go to main game loop
main()