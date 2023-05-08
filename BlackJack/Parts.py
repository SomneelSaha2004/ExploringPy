from random import shuffle
nameToVal={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Joker":10,"Queen":10,"King":10}
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Joker', 'Queen', 'King', 'Ace')
suits=("Spades","Hearts","Clubs","Diamonds")
class Card():
    def __init__(self,rank:str,suit:str):
        self.rank=rank
        self.suit=suit
        #self.isFaceUp=isFaceUp
        if rank=="Ace":
            self.value=1
        else:
            self.value=nameToVal[rank]
    def __add__(self,other:"Card"):
        return self.value+other.value
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    # def flip(self):
    #     self.isFaceUp=not self.isFaceUp
class Deck():
    def __init__(self):
        self.cards=[]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank,suit))
    def shuffleDeck(self):
        shuffle(self.cards)
    def deal(self,n:int,s:int=0,isDealer:bool=False):
        if(isDealer):
            l=list()
            for i in range(0,n):
                card=self.cards.pop(0)
                if card.rank=="Ace":
                        if s +11> 21:
                            card.value=1
                        else :
                            card.value=11
                s+=card.value
                l.append(card)
            return l

        l=list()
        for i in range(0,n):
            card=self.cards.pop(0)
            if card.rank=="Ace":
                    print("You have been dealt an Ace!")
                    val=int(input(f"would you like the Ace's value be 11 or 1?"))
                    card.value=int(val)
            l.append(card)
        return l
class Player():
    def __init__(self,name:str,balance:float):
        self.hand=[]
        self.name=name
        self.balance=balance
    def addCards(self,l:list):
        self.hand.extend(l)
    def bet(self,amt:float)->bool:
        if(self.balance-amt<0):
            print(f"{self.name}'s account balance is currently : {self.balance} cannot make this bet!")
            return False
        self.balance-=amt
        return True
        print(f"{self.name} places a bet of {amt}")
    def clearHand(self):
        self.hand=[]
