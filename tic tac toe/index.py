def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-|-|-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-|-|-")
    print(board[6] + "|" + board[7] + "|" + board[8])def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    game_still_going = True
    print("Welcome to Tic Tac Toe!")

    while game_still_going:
        print_board(board)
      position = input("Choose a position from 1-9: ")

        valid_position = False
        while not valid_position:
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
       position = input("Invalid input. Choose a position from 1-9: ")
            position = int(position) - 1
            if board[position] == " ":
                valid_position = True
            else:
                print("That position is already taken. Choose a different position.")

        board[position] = current_player
        if current_player == "X":
            current_player = "O"
                    else:
            current_player = "X"

        if check_if_game_over(board):
            print_board(board)
            print("Game over! " + check_if_game_over(board) + " wins!")
            game_still_going = False
                      elif check_if_tie(board):
            print_board(board)
            print("Game over! It's a tie!")
            game_still_going = False

def check_if_game_over(board):
    if check_rows(board) or check_columns(board) or check_diagonals(board):
        return True
                       else:
                   return False

def check_rows(board):
    if board[0] == board[1] == board[2] != " " or board[3] == board[4] == board[5] != " " or board[6] == board[7] == board[8] != " ":
        return True
    else:
        return False

def check_columns(board):
    if board[0] == board[3] == board[6] != " " or board[1] == board[4] == board[7] != " " or board[2] == board[5] == board[8] != " ":
                return True
    else:
        return False

def check_diagonals(board):
    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
                    return True
    else:
        return False

def check_if_tie(board):
    if " " not in board:
        return True
                          else:
        return False

play_game()
