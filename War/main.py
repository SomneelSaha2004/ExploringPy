from Parts import Player,Deck,Card
def play():
    f=open("gameHistory.txt",mode="a+")
    p1=Player(input("Enter Player 1's name : "))
    p2=Player(input("Enter Player 2's name : "))
    d=Deck()
    d.shuffleDeck()
    p1.addCard(d.deal(26))
    p2.addCard(d.deal(26))
    f.write("\n\nLet's Play!\n\n")
    while True:
        if len(p1.hand)==0:
            f.write("Player 1 has 0 cards, Player 2 wins!")
            break
        elif len(p2.hand)==0:
            f.write("Player 2 has 0 cards, Player 1 wins!")
            break
        pc1=p1.removeCard()
        pc2=p2.removeCard()
        f.write("Battle !\n\n")
        f.write(f"{p1.name}'s {pc1}\tvs\t{p2.name}'s  {pc2}\n\n")
        if pc1>pc2:
            l=[pc1,pc2]
            p1.addCard(l)
            f.write(f"{p1.name} wins!")
        elif pc2>pc1:
            l=[pc2,pc1]
            p2.addCard(l)
            f.write(f"{p2.name} wins!")
        elif pc1==pc2:
            war=True
            l1=[]
            l2=[]
            while war:
                f.write("WAR!\n\n")
                f.write("Both players must draw 3 cards")
                
                for i in range(0,3):
                    l1.append(p1.removeCard())
                    l2.append(p2.removeCard())
                pc1=l1[-1]
                pc2=l2[-1]
                f.write("Battle!")
                f.write(f"{p1.name}'s {pc1}\tvs\t{p2.name}'s  {pc2}\n\n")
                if pc1>pc2:
                    l1.extend(l2)
                    p1.addCard(l1)
                    f.write(f"{p1.name} wins!")
                    break
                if pc1<pc2:
                    l2.extend(l1)
                    p2.addCard(l2)
                    f.write(f"{p1.name} wins!")
                    break
                if pc1==pc2:
                    war=True
                    continue
if __name__=="__main__":
    yes=True
    while yes:
        play()
        yes=True if input("Continue[y/n]?")=="y" else False
