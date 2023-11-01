# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

# Show the board to the user.
def display_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 9)

# Check the  move is a valid move.
def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] is None

# Input a move from the player.
def take_turn(board, player):
    while True:
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if is_valid_move(board, row, col):
                board[row][col] = player
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")



# Reminder to check all the tests


if __name__ == '__main__':
    board = make_empty_board()
    player = 'X'
    winner = None

    while winner is None:
        # Show the board to the user.
        display_board(board)
        # Check the move is a valid move.
        # Input a move from the player.
        take_turn(board, player)
        # Check if there is a winner.
        # Update the board.
        winner = get_winner(board)
        # Update who's turn it is.
        player = other_player(player)

    display_board(board)
    print(f"Player {winner} wins!")

