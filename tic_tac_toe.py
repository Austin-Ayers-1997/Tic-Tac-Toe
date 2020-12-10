import numpy as np                                      # For fast array representation
import random                                           # For non AI computer moves
import cpu_logic as ai                                  # For AI computer moves if selected
import sys                                              # To get arguement on whether to use random enemy movement or AI enemy movement

# Written by Austin Ayers using the PEP 257 standard for doucmentation

def instructions():
    """
    Method that will provide instructions to the person playing the game
    """
    print("Welcome to Austin's Tic-Tac-Toe!")
    print("    You selected mode "  + sys.argv[1])
    print("Here is how to play this game:")
    print("Human players are always X, and you will always go first (so you should never lose)")
    print("The squares on the board are numbered as shown below")
    instructional_board = np.array([["0", "1", "2"],
                                    ["3", "4", "5"],
                                    ["6", "7", "8"]])   # Create instructional Tic-Tac-Toe board
    print(instructional_board)
    print("Each turn you will be told to select a square to place an X in, and you will select a square by inputting a number")
    print("Open squares will be marked with their number")
    print("Play until you win, lose or the game is a draw")

def get_clear_board():
    """
    Method that returns a clear Tic-Tac-Toe board for a new game
    """
    return np.array([["0", "1", "2"],
                     ["3", "4", "5"],
                     ["6", "7", "8"]])                  # Create a clean board for the game

def computer_play_random(available_moves):
    """
    Method that returns an integer value that indicates where the computer will put an O

    Keyword Arguements:
    available_moves -- List of integers that determines where computer can move

    Returns: 
    move -- Integer representing the move that computer should make
    """
    num_moves = len(available_moves)
    index = random.randrange(0, num_moves, 1)
    return available_moves[index]

def get_player_win(board):
    """
    Method to see if the player has won the game

    Returns:
    win -- Boolean that says if the player has won (True is a win)
    """
    # Check horizontal chances to win
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X": return True
    if board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X": return True
    if board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X": return True
    # Check vertical chances to win
    if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X": return True
    if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X": return True
    if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X": return True
    # Check diagonal chances to win
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X": return True
    if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X": return True
    return False

def get_cpu_win(board):
    """
    Method to see if the cpu has won the game

    Returns:
    win -- Boolean that says if the cpu has won (True is a win)
    """
    # Check horizontal chances to win
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O": return True
    if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O": return True
    if board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O": return True
    # Check vertical chances to win
    if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O": return True
    if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O": return True
    if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O": return True
    # Check diagonal chances to win
    if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O": return True
    if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O": return True
    return False

def play_game(mode):
    """
    Main method for this file, will allow the game to be played from the console

    Keyword Arguements:
    mode -- Boolean arguement for whether AI enemy movement should be enabled. 0 is off, 1 is on
    """
    instructions()
    game_board = get_clear_board()                      # Get a new gameboard for the game
    valid_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]           # Create list of valid moves
    game_over = 0                                       # Boolean to see if the game is over
    turn_counter = 0                                    # Counts whose turn it is, 0 and even numbers for player and odd for computer
    while game_over < 1:
        if turn_counter % 2 == 0:
            print(game_board)
            move = int(input("Position to Place X :"))  # Ask player for input
            if move in valid_moves:
                row = move / 3                          # Get the row to place the X at
                col = move % 3                          # Get the col to place the X at
                game_board[row][col] = "X"              # Place the X in the array
                turn_counter = turn_counter + 1         # Go to the next turn and let the computer play
                valid_moves.remove(move)                # Remove the new move from the valid moves
            else:
                print("You entered an invalid move")    # Tell the player they made an invalid move
        elif int(mode) == 1:
            move = ai.calculate_move(valid_moves, game_board)    # Get computer move in the game
            row = move / 3                              # Get the row to place the O at
            col = move % 3                              # Get the col to place the O at
            game_board[row][col] = "O"                  # Place the O in the array
            turn_counter = turn_counter + 1             # Go to the next turn and let the player play
            valid_moves.remove(move)                    # Remove the new move from the valid moves 
        else:
            move = computer_play_random(valid_moves)    # Get computer move in the game
            row = move / 3                              # Get the row to place the O at
            col = move % 3                              # Get the col to place the O at
            game_board[row][col] = "O"                  # Place the O in the array
            turn_counter = turn_counter + 1             # Go to the next turn and let the player play
            valid_moves.remove(move)                    # Remove the new move from the valid moves 
        
        player_wins = get_player_win(game_board)
        cpu_wins = get_cpu_win(game_board)

        if player_wins:                                 # Print that you won and end the game
            print(game_board)
            print("You have won the game, congratulations!")
            game_over = 1
            new_game = input("Do you want to play again? (0 for no, 1 for yes): ")
            if int(new_game) == 1:
                play_game(mode)

        if cpu_wins:                                    # Print that you lost and end the game
            print(game_board)
            print("You have lost the game, you suck!")
            game_over = 1
            new_game = input("Do you want to play again? (0 for no, 1 for yes): ")
            if int(new_game) == 1:
                play_game(mode)

        if len(valid_moves) == 0:                       # See if the game is out of moves to be made (a draw)
            print("The game is a draw, better luck next time")
            game_over = 1
            new_game = input("Do you want to play again? (0 for no, 1 for yes): ")
            if int(new_game) == 1:
                play_game(mode)

if __name__ == "__main__":
    play_game(sys.argv[1])