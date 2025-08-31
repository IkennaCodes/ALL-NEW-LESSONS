#Creating the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)

#Functions to check for winner
def check_winner(board,index = 0):
    if index == 3:
        return None
    #row
    if board[index][0] == board[index][2] != " ":
        return board [index][0]
    
    #column
    if board [0][index] == board [1][index] == board [2][index] != " ":
        return check_winner(board,index +1)
    
def check_diagonal(board):
    #Left to right
    if board [0][0] == board [1][1] == board[2][2] != " ":
        return board [1][1]
    
    #Right to left
    if board [0][2] == board [1][1] == board [2][0]!=" ":
        return board [0][2]
    
    #Function to check if full
def is_full(board):
    return all(cell != " " for row in board for cell in row)
    
def play_game():
    board = [[" "for _ in range(3)] for _ in range (3)]
    current_player = "X"

    while True:
            print_board(board)
            print("it is {}'s turn".format(current_player))

            try:
                row = int(input("Enter the row (0-2):"))
                col = int(input("Enter the row (0-2):"))
                if not (0 < row <= 2 and 0 <= col <=2):
                    print("Invalid Input! Row and Column must be between 0 and 2 only")
                continue

            except ValueError:
                print("Please enter a valid integer!")

            if board [row][col] == " ":
                board [row][col] = current_player
            else:
                print("Cell is already occupied")
                continue

            winner = check_winner(board) or check_diagonal(board)
            if winner:
                print_board(board)
                print("{} wins.".format(winner))
                break

            if is_full(board):
                print_board(board)
                print("Game is a DRAW!")
                break

            current_player = "0" if current_player == "X" else "X"

play_game()
