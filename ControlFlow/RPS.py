from random import shuffle,randint
print("Welcome to Rock,Paper Scissor Revolution!")
l=["R","S","P"]
print("Rock --> R\tPaper --> P\tScissors --> S")
print("print history --> p\tquit --> q")
score={"player":0,"computer":0}
while(True):
    player=input("--> ")
    if player=="p":
        with open("history.txt") as f:
            print(f.read())
            continue
    if player=="q":
        print(f"Thanks for playing!\nFinal Score\nYou : {score['player']}\tComputer :{score['computer']}")
        break
    shuffle(l)
    computer=l[randint(0,2)]
    output=""
    match player:
        case 'R':
            match computer:
                case 'R':
                    output=f"Computer throws {computer}\n Its a draw!"
                    print(output)
                case 'S':
                    output=f"Computer throws {computer}\n You win!"
                    print(f"Computer throws {computer}\n You win!")
                    score["player"]+=1
                case 'P':
                    output=f"Computer throws {computer}\n Computer wins!"
                    print(f"Computer throws {computer}\n Computer wins!")
                    score["computer"]+=1
        case 'P':
            match computer:
                case 'P':
                    output=f"Computer throws {computer}\n Its a draw!"
                    print(output)
                case 'R':
                    output=f"Computer throws {computer}\n You win!"
                    print(f"Computer throws {computer}\n You win!")
                    score["player"]+=1
                case 'S':
                    output=f"Computer throws {computer}\n Computer wins!"
                    print(f"Computer throws {computer}\n Computer wins!")
                    score["computer"]+=1
        case 'S':
            match computer:
                case 'S':
                    output=f"Computer throws {computer}\n Its a draw!"
                    print(output)
                case 'P':
                    output=f"Computer throws {computer}\n You win!"
                    print(f"Computer throws {computer}\n You win!")
                    score["player"]+=1
                case 'R':
                    output=f"Computer throws {computer}\n Computer wins!"
                    print(f"Computer throws {computer}\n Computer wins!")
                    score["computer"]+=1
        case _:
            print("Please enter valid input!")
        
    with open("history.txt",mode="a+") as f:
        f.write(f"You threw {player}\n{output}")


