from random import shuffle
nameToVal={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Joker":11,"Queen":12,"King":13,"Ace":14}
suits=("Hearts","Diamonds","Spades","Clubs")
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Joker', 'Queen', 'King', 'Ace')
class Card():
    def __init__(self,suit:str,rank:str):
        self.suit=suit
        self.rank=rank
        self.value=nameToVal[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __gt__(self,other):
        return self.value>other.value
    def __lt__(self,other):
        return self.value<other.value
    def __eq__(self,other):
        return self.value==other.value
class Deck():
    def __init__(self):
        self.cards=[]
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(suit,rank))
    def shuffleDeck(self):
        shuffle(self.cards)
    def __len__(self):
        return len(self.cards)
    def deal(self,n:int):
        l=[]
        for i in range(0,n):
            l.append(self.cards.pop())
        return l
# d=Deck()
# d.shuffleDeck()
# d.deal()
# print(len(d.cards))
# for card in d.cards:
#     print(card)
class Player():
    def __init__(self,n:str):
        self.name=n
        self.hand=[]
    def addCard(self,newCards:list):
        if type(newCards)==list:
            self.hand.extend(newCards)
        else:
            self.hand.append(newCards)
    def removeCard(self):
        return self.hand.pop(0)
    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards'
# p=Player("Somneel")
# mycard=Card("Spade","Five")
# p.addCard([mycard,mycard,mycard])
# p.removeCard(2)
# print(p)