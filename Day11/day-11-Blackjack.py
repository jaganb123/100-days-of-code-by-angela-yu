from Blackjack_Functions import DrawCard,ManipulateCards,Score
from art import logo
from random import choice

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

ContinuePlay = input("Do you want to play BlackJack ? yes/no : ")
if ContinuePlay == "yes":
    ContinuePlay = True
else:
    ContinuePlay = False
while ContinuePlay:
    print(logo)
    PlayerCard = [DrawCard(), DrawCard()]
    DrawerCard = [DrawCard(), DrawCard()]
    PlayerHand = Score(PlayerCard)
    DrawerHand = Score(DrawerCard)
    if DrawerHand == 0 :
        ContinuePlay = False
        print('Oops, Drawer has BlackJack. You lose !!!')
    elif PlayerHand == 0:
        ContinuePlay = False
        print('Hola, You got BlackJack. You Win !!!')
    MaskCard = []
    MaskCard.extend(DrawerCard)
    MaskCard[-1] = 'X'
    PlayerGame = True
    DrawerGame = False
    while PlayerGame:
        PlayerHand = Score(PlayerCard)
        print(f"Drawers card is {MaskCard}\nYour card is {PlayerCard}, your total is '{PlayerHand}'\n")
        if PlayerHand == 0:
            print('Hola, You got BlackJack. You Win !!!')
            PlayerGame = False
            continue
        PlayerChoice = input("Do you want to 'hit' or 'draw ? ")
        if PlayerChoice == "hit" :
            DrawerGame = True
            PlayerGame = False
        elif PlayerChoice == "draw" :
            PlayerCard.append(DrawCard())
    while DrawerGame:
        DrawerHand = Score(DrawerCard)
        if DrawerHand == 0:
            DrawerGame = False
            DrawerHand = 21
            continue
        elif DrawerHand < 16:
            DrawerCard.append(DrawCard())
        elif DrawerHand < 21 :
            if "draw" == choice(['hit', 'draw']):
                DrawerCard.append(DrawCard())
                DrawerHand = Score(DrawerCard)
                print(f"Drawer card is {DrawerCard} and his total is {DrawerHand}...")
            else:
                DrawerGame = False
                continue
        else:
            DrawerGame = False
            continue
        DrawerHand = Score(DrawerCard)
        print(f"Drawer card is {DrawerCard} and his total is {DrawerHand}...")
    if DrawerHand > PlayerHand and DrawerHand < 21 and PlayerHand < 21 :
        print(f"Player stake : {PlayerHand}\nDrawer stake : {DrawerHand}\nDrawer wins !!!")
    elif DrawerHand < PlayerHand and DrawerHand < 21 and PlayerHand < 21:
        print(f"Player stake : {PlayerHand}\nDrawer stake : {DrawerHand}\nPlayer wins !!!")
    else:
        print(f"It's a draw")
    ContinuePlay = input("Do you want to play BlackJack ? yes/no : ")
    if ContinuePlay == "yes":
        ContinuePlay = True
    else:
        ContinuePlay = False
