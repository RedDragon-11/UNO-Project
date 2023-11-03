import random
import pygame as pg
import UNOGlobals as ug

class UNOcard:


    def __init__(self, c, s, v, filename):
        self.color = c
        self.special = s
        self.value = v
        self.img = pg.image.load(filename)



    def deckBuilder():
        deck = []

        #Addings Red Cards to the Deck
        for redCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.RED, ug.GENERAL, cardNum, ("small/red_" + str(cardNum) + ".png")))
        for redSkips in range(0,2):
            deck.append(UNOcard(ug.RED, ug.SKIP, None,"small/red_skip.png"))
        for redDrawTwos in range(0,2):
            deck.append(UNOcard(ug.RED, ug.DRAW2, None, "small/red_picker.png"))
        for redReverse in range (0,2):
            deck.append(UNOcard(ug.RED, ug.REVERSE, None, "small/red_reverse.png"))

        #adding Blue Cards to the Deck
        for blueCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.BLUE, ug.GENERAL, cardNum, ("small/blue_" + str(cardNum) + ".png")))
        for blueSkips in range(0,2):
            deck.append(UNOcard(ug.BLUE, ug.SKIP, None, "small/blue_skip.png"))
        for blueDrawTwos in range(0,2):
            deck.append(UNOcard(ug.BLUE, ug.DRAW2, None, "small/blue_picker.png"))
        for blueReverse in range (0,2):
            deck.append(UNOcard(ug.BLUE, ug.REVERSE, None, "small/blue_reverse.png"))

        #adding Green Cards to the Deck
        for greenCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.GREEN, ug.GENERAL, cardNum, ("small/green_" + str(cardNum) + ".png")))
        for greenSkips in range(0,2):
            deck.append(UNOcard(ug.GREEN, ug.SKIP, None, "small/green_skip.png"))
        for greenDrawTwos in range (0,2):
            deck.append(UNOcard(ug.GREEN, ug.DRAW2, None, "small/green_picker.png"))
        for greenReverse in range(0,2):
            deck.append(UNOcard(ug.GREEN, ug.REVERSE, None, "small/green_reverse.png"))

        #adding Yellow Cards to the Deck
        for yellowCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.YELLOW, ug.GENERAL, cardNum, "small/yellow_" + str(cardNum) + ".png"))
        for yellowSkips in range(0,2):
            deck.append(UNOcard(ug.YELLOW, ug.SKIP, None, "small/yellow_skip.png"))
        for yellowDrawTwos in range (0,2):
            deck.append(UNOcard(ug.YELLOW, ug.DRAW2, None, "small/yellow_picker.png"))
        for yellowReverse in range(0,2):
            deck.append(UNOcard(ug.YELLOW, ug.REVERSE, None, "small/yellow_reverse.png"))

        #adding Wild cards to the Deck
        for wildcards in range (0,2):
            deck.append(UNOcard(None, ug.WILD, None, "small/wild_color_changer.png"))
        for wildDrawFours in range (0,2):
            deck.append(UNOcard(None, ug.WILD4, None, "small/wild_pick_four.png"))

        return deck


    def deckReset(hand1, hand2):

        deck = UNOcard.deckBuilder()

        if(len(hand1) != 0):
            for cards in range(0, len(hand1)):
                removeCard = hand1[cards]
                deck.remove(removeCard)
        if(len(hand2) != 0):
            for cards in range(0, len(hand2)):
                deck.remove(hand2[cards])
        print("Deck is being reshuffled...")
        return deck
    
    def setColor(self, color):
        self.color = color 

    def setValue(self, value):
        self.value = value 

    def setSpecial(self, special):
        self.special = special

    def getColor(self):
        return self.color
    
    def getValue(self):
        return self.value
    
    def getSpecial(self):
        return self.special

    def getImage(self):
        return self.img
    
    def removeCard(deck, card):
        deck.remove(card)
    





  