#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the Tic Tac Toe board.

    Args:
        board (list): A 2D list representing the board.

    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner on the Tic Tac Toe board.

    Args:
        board (list): A 2D list representing the board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_board_full(board):
    """
    Checks if the board is full with no empty spaces left.

    Args:
        board (list): A 2D list representing the board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play a game of Tic Tac Toe.

    Args:
        None

    Returns:
        None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter a row and column between 0 and 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except IndexError:
            print("Invalid input. Please enter a row and column between 0 and 2.")

tic_tac_toe()
