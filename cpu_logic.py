import numpy as np                                      # For fast array representation
import random                                           # For non AI computer moves

def calculate_move(available_moves, current_board):
    """
    Method that contains the logic that will control a smart cpu to attack

    Keyword Arguement:
    available_moves -- List structure of moves that are possible for the cpu
    current_board -- Numpy nested-array that represents the current board 
    """
    if 4 in available_moves:
        return 4                                        # If the center is open, cpu_should play in the center
    elif len(available_moves) == 8:
        return available_moves[0]                       # Just pick the top right corner if the center was chosen
                                                        # by the player first
    else:
        # Make sure that the computer can't lose the game
        # Check horizontal win conditions
        if current_board[0][0] == "X" and current_board[0][1] == "X" and 2 in available_moves: return 2
        if current_board[0][0] == "X" and current_board[0][2] == "X" and 1 in available_moves: return 1
        if current_board[0][1] == "X" and current_board[0][2] == "X" and 0 in available_moves: return 0

        if current_board[1][0] == "X" and current_board[1][1] == "X" and 5 in available_moves: return 5
        if current_board[1][0] == "X" and current_board[1][2] == "X" and 4 in available_moves: return 4
        if current_board[1][1] == "X" and current_board[1][2] == "X" and 3 in available_moves: return 3

        if current_board[2][0] == "X" and current_board[2][1] == "X" and 8 in available_moves: return 8
        if current_board[2][0] == "X" and current_board[2][2] == "X" and 7 in available_moves: return 7
        if current_board[2][1] == "X" and current_board[2][2] == "X" and 6 in available_moves: return 6
        # Check vertical win conditions
        if current_board[0][0] == "X" and current_board[1][0] == "X" and 6 in available_moves: return 6
        if current_board[0][0] == "X" and current_board[2][0] == "X" and 3 in available_moves: return 3
        if current_board[1][0] == "X" and current_board[2][0] == "X" and 0 in available_moves: return 0

        if current_board[0][1] == "X" and current_board[1][1] == "X" and 7 in available_moves: return 7
        if current_board[0][1] == "X" and current_board[2][1] == "X" and 4 in available_moves: return 4
        if current_board[1][1] == "X" and current_board[2][1] == "X" and 1 in available_moves: return 1

        if current_board[0][2] == "X" and current_board[1][2] == "X" and 8 in available_moves: return 8
        if current_board[0][2] == "X" and current_board[2][2] == "X" and 5 in available_moves: return 5
        if current_board[1][2] == "X" and current_board[2][2] == "X" and 3 in available_moves: return 3
        # Check diagonal win conditions
        if current_board[0][0] == "X" and current_board[1][1] == "X" and 8 in available_moves: return 8
        if current_board[0][0] == "X" and current_board[2][2] == "X" and 4 in available_moves: return 4
        if current_board[1][1] == "X" and current_board[2][2] == "X" and 0 in available_moves: return 0

        if current_board[2][0] == "X" and current_board[1][1] == "X" and 2 in available_moves: return 2
        if current_board[2][0] == "X" and current_board[0][2] == "X" and 4 in available_moves: return 4
        if current_board[1][1] == "X" and current_board[0][2] == "X" and 6 in available_moves: return 6

        # Win if you can
        # Check horizontal win conditions
        if current_board[0][0] == "O" and current_board[0][1] == "O" and 2 in available_moves: return 2
        if current_board[0][0] == "O" and current_board[0][2] == "O" and 1 in available_moves: return 1
        if current_board[0][1] == "O" and current_board[0][2] == "O" and 0 in available_moves: return 0

        if current_board[1][0] == "O" and current_board[1][1] == "O" and 5 in available_moves: return 5
        if current_board[1][0] == "O" and current_board[1][2] == "O" and 4 in available_moves: return 4
        if current_board[1][1] == "O" and current_board[1][2] == "O" and 3 in available_moves: return 3

        if current_board[2][0] == "O" and current_board[2][1] == "O" and 8 in available_moves: return 8
        if current_board[2][0] == "O" and current_board[2][2] == "O" and 7 in available_moves: return 7
        if current_board[2][1] == "O" and current_board[2][2] == "O" and 6 in available_moves: return 6
        # Check vertical win conditions
        if current_board[0][0] == "O" and current_board[1][0] == "O" and 6 in available_moves: return 6
        if current_board[0][0] == "O" and current_board[2][0] == "O" and 3 in available_moves: return 3
        if current_board[1][0] == "O" and current_board[2][0] == "O" and 0 in available_moves: return 0

        if current_board[0][1] == "O" and current_board[1][1] == "O" and 7 in available_moves: return 7
        if current_board[0][1] == "O" and current_board[2][1] == "O" and 4 in available_moves: return 4
        if current_board[1][1] == "O" and current_board[2][1] == "O" and 1 in available_moves: return 1

        if current_board[0][2] == "O" and current_board[1][2] == "O" and 8 in available_moves: return 8
        if current_board[0][2] == "O" and current_board[2][2] == "O" and 5 in available_moves: return 5
        if current_board[1][2] == "O" and current_board[2][2] == "O" and 3 in available_moves: return 3
        # Check diagonal win conditions
        if current_board[0][0] == "O" and current_board[1][1] == "O" and 8 in available_moves: return 8
        if current_board[0][0] == "O" and current_board[2][2] == "O" and 4 in available_moves: return 4
        if current_board[1][1] == "O" and current_board[2][2] == "O" and 0 in available_moves: return 0

        if current_board[2][0] == "O" and current_board[1][1] == "O" and 2 in available_moves: return 2
        if current_board[2][0] == "O" and current_board[0][2] == "O" and 4 in available_moves: return 4
        if current_board[1][1] == "O" and current_board[0][2] == "O" and 6 in available_moves: return 6
        
        return available_moves[0]

if __name__ == "__main__":
    print("You shouldn't just call this file")