r1 = input()
r2 = input()
r3 = input()

board = [list(r1), list(r2), list(r3)]

if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Jebb")

elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("Jebb")

elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("Jebb")
    
elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Jebb")

elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Jebb")

elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Jebb")

elif (board[0][0] == 'O' and 
    board[1][1] == 'O' and 
    board[2][2] == 'O'):
    print("Jebb")
        
elif (board[0][2] == 'O' and 
    board[1][1] == 'O' and 
    board[2][0] == 'O'):
    print("Jebb")

else:
    print("Neibb")


