class TicTacToe():
    board = [[1,2,3],[4,5,6],[7,8,9]]
    def save(self):
        f.write(f"{self.player1} v {self.player2}")
        with open("games.txt",mode="a+") as f:
            f.write(f"{self.player1} v {self.player2}")
            for l in self.board:
                f.write(f"\t{l[0]} | {l[1]} | {l[2]}\n")
    
    def __init__(self):
        self.player1=input("name of player 1 :")
        self.player2=input("name of player 2 : ")
    def guide(self):
        print("The board positions correspond to numbers as shows")
        self.printBoard()
    def printBoard(self):
        for l in self.board:
            print(f"\t{l[0]} | {l[1]} | {l[2]}")
    def check(self,ch,currentPlayer):
        count=0
        i=0
        for i in range(0,3):
            count=0
            for j in range(0,3): 
                if(self.board[i][j]==ch):
                    count+=1
            if(count==3):
                print(f"Player {currentPlayer} wins!")
                self.printBoard()
                self.save()
                exit()
        
        for i in range(0,3):
            count=0
            for j in range(0,3): 
                if(self.board[j][i]==ch):
                    count+=1
            if(count==3):
                print(f"Player {currentPlayer} wins! ")
                self.printBoard()
                self.save()
                exit()
            
        if(self.board[0][0]==self.board[1][1]==self.board[2][2]==ch or self.board[0][2]==self.board[1][1]==self.board[2][0]==ch):
                print(f"Player {currentPlayer} wins!")
                self.printBoard()
                self.save()
                exit()
    def reset(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        self.play()
    def play(self):
        print("Welcome Tic Tac Toe Revolution!")
        print("Player 1 symbol -> X\nPlayer 2 symbol -> O")
        self.guide()
        print("Lets play!\nto print the guide enter g\n to quit enter q\n")
        count=0
        i=0
        while(True):
            if count==9:
                break
            currentPlayer=1 if count%2==0 else 2
            ch='X' if count%2==0 else "O"
            i=input(f"Player {currentPlayer} > ")
            
            if(i=="q"):
                break
            elif(i=="g"):
                self.guide()
                continue
            if(not i.isnumeric()):
                print("Invalid Input!")
                continue
            i=int(i)-1
            pos=0
            for j in range(0,3):
                f=False
                flag=False
                for k in range(0,3):
                        if(pos==i):
                            # if(self.board[i][j]=="X" or self.board[i][j]=="O"):
                            #     print("That position is already filled!")
                            #     f=True
                            #     break
                            self.board[j][k]=ch
                            self.check(ch,currentPlayer)
                            flag=True
                            self.printBoard()
                            break
                        pos+=1
                if(flag):
                    break
                # if(f):
                #     break
            # if(f):
            #     continue
            # else:
            count+=1
        print("Its a draw!")
        self.save()
game=TicTacToe()
game.play()
        

