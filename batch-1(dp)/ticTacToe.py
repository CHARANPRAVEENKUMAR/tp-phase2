board=[[""]*3 for i in range(3)]
def show_board(board):
    for i in board:
        for j in i:
            if j=="":
                print("|","  ",end="")
            else:
                print("|","",j,end="")
        print("")
show_board(board)
def check_win(board,person1,person2):
    #check row win
    for i in board:
        if i.count("x")==3:
            # print("won")
            return person1
        elif i.count("o")==3:
            # print("won")
            return person2
    #check column win
    for i in range(2):
        # print(board[i][0]==board[i][1]==board[i][2]=="o",board[i][0],board[i][1],board[i][2])
        if board[0][i]==board[1][i]==board[2][i]=="x":
            # print("won")
            return person1
        elif board[0][i]==board[1][i]==board[2][i]=="o":
            # print("won")
            return person2
    #check diagonal win
    if board[0][0]==board[1][1]==board[2][2]=="x":
        return person1
    elif board[0][0]==board[1][1]==board[2][2]=="o":
        return person2
    elif board[0][2]==board[1][1]==board[2][0]=="x":
        return person1
    elif board[0][2]==board[1][1]==board[2][0]=="o":
        return person2
    return "draw"
def check_full(board):
    ans=True
    for i in range(3):
        for j in range(3):
            if board[i][j]=="":
                ans=False
                break
    return ans
def start_game(board):
    person1=input("Enter person1 name: ")
    person2=input("Enter person2 name: ")
    while True:
        print("current board: ")
        show_board(board)
        print(f"{person1} it's your turn \nEnter the row and column number to place x")
        while True:
            print(f"{person1} enter the row : ",end="")
            row=int(input())
            print(f"{person1} enter the column: ",end="")
            col=int(input())
            if board[row-1][col-1] !="":
                print(f"choose another cell {person1}")
            else:
                board[row-1][col-1]="x"
                break
        check=check_win(board,person1,person2)
        if check==person1:
            print(f"{person1} won the game")
            show_board(board)
            break
        isFull=check_full(board)
        if isFull:
            print("game is draw")
            break
        print("current board: ")
        show_board(board)
        print(f"{person2} it's your turn \nEnter the row and column number to place o")
        while True:
            print(f"{person2} enter the row : ",end="")
            row=int(input())
            print(f"{person2} enter the column: ",end="")
            col=int(input())
            if board[row-1][col-1] !="":
                print(f"choose another cell {person2}")
            else:
                board[row-1][col-1]="o"
                break 
        check=check_win(board,person1,person2)
        if check==person2:
            print(f"{person2} won the game")
            show_board(board)
            break
start_game(board)
# board=[["x","o","x"],["","o",""],["","o",""]]
