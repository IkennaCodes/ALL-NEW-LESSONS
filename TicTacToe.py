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
