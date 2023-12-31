# Initialize the board
board = [" " for _ in range(9)]
import random

def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Function to check if a player has won
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to make a move for the AI player (computer)
def ai_move(board, ai_player):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    if empty_cells:
        return random.choice(empty_cells)
    return None

# Ask for the player's name
player_name = input("Enter your name: ")

# Main game loop
player_turn = "X"
ai_player = "O"
turns = 0

while turns < 9:
    display_board(board)
    
    if player_turn == "X":
        print(f"{player_name}'s turn. Enter a position (0-8): ")
        position = int(input())
    else:
        print("AI's turn...")
        position = ai_move(board, ai_player)
    
    if board[position] == " ":
        board[position] = player_turn
        turns += 1

        if check_win(board, player_turn):
            display_board(board)
            if player_turn == "X":
                print(f"{player_name} wins!")
            else:
                print("AI wins!")
            break

        player_turn = "O" if player_turn == "X" else "X"
    else:
        print("That position is already filled. Try again.")

# Check for a draw
if turns == 9:
    display_board(board)
    print("It's a draw!")

# Ask to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
    board = [" " for _ in range(9)]
    player_turn = "X"
    turns = 0
    print("Game restarted.")
else:
    print("Thanks for playing!")