from Parts import Player,Deck,Card
def play():
    print("Welcome to BlackJack Buzz!")
    p=Player(input("Enter player's name : "),float(input("Enter player's starting balance : ")))
    d=Deck()
    d.shuffleDeck()
    print("Lets Play!")
    dealer=[]
    consent=True
    while consent:
        f=False
        p.clearHand()
        dealer=[]
        bet=float(input(f"{p.name} place your bet : "))
        if(not p.bet(bet)):
            continue
        print("Dealer deals ")
        p.addCards(d.deal(2))
        dealer.extend(d.deal(2,isDealer=True))
        dealerSum=sum([card.value for card in dealer])
        playerSum=sum([card.value for card in p.hand])
        print(f"{p.name}'s cards are ")
        for card in p.hand:
            print(f"{card}\t",end="")
        print()
        if playerSum>21:
                    print("BUST!")
                    print(f"{p.name} you lose {bet}")
                    continue
        elif playerSum==21:
                    print(f"{p.name} you win {bet*2}!")
                    p.balance+=bet*2
                    continue
        #print(playerSum)
        print("Dealer's Cards ")
        for i in range(0,len(dealer)-1):
            print(f"{dealer[i]}\t",end="")
        print()
        #print(dealerSum)
        while True:
            decision=input(f"\n{p.name} Hit or Stay [h/s]?").lower()
            if decision=="h":
                p.addCards(d.deal(1))
                card=p.hand[-1]
                print(f"The card that has been dealt is {card}\n")
                
                playerSum=sum([card.value for card in p.hand])
                if playerSum>21:
                    print("BUST!")
                    print(f"{p.name} you lose {bet}")
                    break
                elif playerSum==21:
                    print(f"{p.name} you win {bet*2}!")
                    p.balance+=bet*2
                    break
                print(f"{p.name} your hand is ")
                for card in p.hand:
                    print(f"{card}\t",end="")
            if decision=="s":
                print("\n\nDealer's Turn")
                while True:
                    print(f"\nThe dealer's hand is ")
                    for i in range(0,len(dealer)):
                        print(f"{dealer[i]}\t",end="")
                    dealerSum=sum([card.value for card in dealer])
                    #print(dealerSum,playerSum)
                    if dealerSum >21:
                        print(f"\nBUST!\n{p.name} wins {bet*2}")
                        f=True
                        p.balance+=bet*2
                        break
                    if dealerSum>playerSum and dealerSum<=21:
                        print(f"\nDealer wins!\n{p.name} loses {bet}")
                        f=True
                        break
                    card=d.deal(1,dealerSum,True)[0]
                    print("Dealer Hits!")
                    print(f"Card dealt is {card}")
                    dealer.append(card)
            if(f):
                break
        consent=True if input("Continue[y/n]?").lower()=="y" else False
    print(f"{p.name} your current balance = {p.balance}")

if __name__=="__main__":
    play()