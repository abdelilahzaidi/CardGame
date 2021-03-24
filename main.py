import utils

print("game is started...")
player_Frank=utils.Player("Frank")
player_David=utils.Player("David")
player_Mariam=utils.Player("Mariam")
player_Sara=utils.Player("Sara")
print("All players have 10 cards...........")
more_card= True
i=0
while more_card:
    i+=1
    print(i,". turn------------------------")
    if len(player_Mariam.cards)==0: 
        more_card =False
    else:
        player_Mariam.play()
    if len(player_David.cards)==0: 
        more_card =False
    else:
        player_David.play()
    if len(player_Frank.cards)==0: 
        more_card =False
    else:
        player_Frank.play()
    if len(player_Sara.cards)==0: 
        more_card =False
    else:
        player_Sara.play()
    if more_card ==False:
        break
    print("--- active cards ----")
    for k in range(0,len(utils.board.active_cards)):
        print(utils.board.active_cards[k].color,utils.board.active_cards[k].number,utils.board.active_cards[k].symbol)
    print("--- played cards History----")
    for k in range(0,len(utils.board.played_cards)):
        print(utils.board.played_cards[k].color,utils.board.played_cards[k].number,utils.board.played_cards[k].symbol)
    pass
print("game is finished...")
