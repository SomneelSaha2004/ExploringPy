print("Welcome Tic Tac Toe Revolution!")
print("Player 1 symbol -> X\nPlayer 2 symbol -> O")
board = [[1,2,3],[4,5,6],[7,8,9]]
def guide():
    print("The board positions correspond to numbers as shows")
    printBoard()
def printBoard():
    for l in board:
        print(f"\t{l[0]} | {l[1]} | {l[2]}")
def check(ch,currentPlayer):
     count=0
     i=0
     for i in range(0,3):
        count=0
        for j in range(0,3): 
             if(board[i][j]==ch):
                  count+=1
        if(count==3):
          print(f"Player {currentPlayer} wins!")
          printBoard()
          exit()
     
     for i in range(0,3):
        count=0
        for j in range(0,3): 
             if(board[j][i]==ch):
                  count+=1
        if(count==3):
          print(f"Player {currentPlayer} wins! ")
          printBoard()
          exit()
     
     if(board[0][0]==board[1][1]==board[2][2]==ch or board[0][2]==board[1][1]==board[2][0]==ch):
          print(f"Player {currentPlayer} wins!")
          printBoard()
          exit()
guide()
print("Lets play!\nto print the guide enter g\n to quit enter q\n")
count=0
i=0
while(True):
    if count==9:
        break
    currentPlayer=1 if count%2==0 else 2
    ch='X' if count%2==0 else "O"
    i=input(f"Player {currentPlayer} > ")
    if(not i.isnumeric()):
        print("Invalid Input!")
        continue
    if(i=="q"):
        break
    elif(i=="g"):
        guide()
        continue
    i=int(i)-1
    pos=0
    for j in range(0,3):
        flag=False
        for k in range(0,3):
                if(pos==i):
                     board[j][k]=ch
                     check(ch,currentPlayer)
                     flag=True
                     printBoard()
                     break
                pos+=1
        if(flag):
             break
    count+=1
print("Its a draw!")
    #restart()
   

