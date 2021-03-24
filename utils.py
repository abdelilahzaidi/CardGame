from random import random
colors=["red","green","blue","yellow"]
symbols=["*","?","<",">"]

class Card:
    def __init__(self):
        self.color = colors[round(random()*3)] 
        self.number = round(random()*10)
        self.symbol = symbols[round(random()*3)]
        # print(self.color,self.number,self.symbol)
class Board:
    def __init__(self):
        self.players=[]
        self.active_cards=[]
        self.played_cards=[]
    def add_player(self,player):
        self.players.append(player)
    def add_active_card(self,card):
        if(len(self.active_cards)==6):
            self.played_cards.append(self.active_cards[0])
            self.active_cards.pop(0) 
            self.active_cards.append(card) 
        else:
            self.active_cards.append(card)
    # def add_played_card(self,card):
    #     self.played_cards.append(card)
board = Board()            
class Player:                    
        def __init__(self,name):
            self.name=name
            self.cards=[]
            i=0
            for i in range(0,10):                
                card= Card()
                self.cards.append(card)
                print(name,i+1,"card=",self.cards[i].color,self.cards[i].number,self.cards[i].symbol)
                i+=1
        def play(self):            
            if len(self.cards)==0:
                print(self.name,"have no card anymore.")            
            else:
                card=self.cards[round(random()*(len(self.cards)-1))]
                board.add_active_card(card)
                self.cards.remove(self.cards[round(random()*(len(self.cards)-1))])
                print(self.name,"played the card =",card.color,card.number,card.symbol)            
        def souffle(self):
            print("cards are souffled")
            temp=[]
            i=0
            for i in range(0,100):                
                temp=self.cards[round(random()*(len(self.cards)-1))]# select a card
                self.cards.remove(temp)                # remove it from the self.cards
                self.cards.append(temp)                # add it to self.cards             
                i+=1            
        def print_cards(self):
            for x in self.cards:
                print(x.color,x.number,x.symbol)
