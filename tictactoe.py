def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):  # Check diagonals
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def get_player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1-3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_player_input(players[current_player])
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            print_board(board)
            
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
            elif is_full(board):
                print("It's a draw!")
                break
            else:
                current_player = 1 - current_player  # Switch player
        else:
            print("That spot is already taken. Try again.")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
