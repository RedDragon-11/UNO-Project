import random
import inspect
import UNOGlobals as ug

class UNOcard:

    def __init__(self, c, s, v):
        self.color = c
        self.special = s
        self.value = v

    def deckBuilder():
        deck = []

        #Addings Red Cards to the Deck
        for redCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.RED, ug.GENERAL, cardNum))
        for redSkips in range(0,2):
            deck.append(UNOcard(ug.RED, ug.SKIP, None))    
        for redDrawTwos in range(0,2):
            deck.append(UNOcard(ug.RED, ug.DRAW2, None)) 
        for redReverse in range (0,2):
            deck.append(UNOcard(ug.RED, ug.REVERSE, None))

        #adding Blue Cards to the Deck
        for blueCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.BLUE, ug.GENERAL, cardNum))
        for blueSkips in range(0,2):
            deck.append(UNOcard(ug.BLUE, ug.SKIP, None))    
        for blueDrawTwos in range(0,2):
            deck.append(UNOcard(ug.BLUE, ug.DRAW2, None)) 
        for blueReverse in range (0,2):
            deck.append(UNOcard(ug.BLUE, ug.REVERSE, None)) 
                   
        #adding Green Cards to the Deck
        for greenCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.GREEN, ug.GENERAL, cardNum))
        for greenSkips in range(0,2):
            deck.append(UNOcard(ug.GREEN, ug.SKIP, None))
        for greenDrawTwos in range (0,2):
            deck.append(UNOcard(ug.GREEN, ug.DRAW2, None))
        for greenReverse in range(0,2):
            deck.append(UNOcard(ug.GREEN, ug.REVERSE, None))

        #adding Yellow Cards to the Deck
        for yellowCards in range(0,2):
            for cardNum in range(0,10):
                deck.append(UNOcard(ug.YELLOW, ug.GENERAL, cardNum))
        for yellowSkips in range(0,2):
            deck.append(UNOcard(ug.YELLOW, ug.SKIP, None))
        for yellowDrawTwos in range (0,2):
            deck.append(UNOcard(ug.YELLOW, ug.DRAW2, None))
        for yellowReverse in range(0,2):
            deck.append(UNOcard(ug.YELLOW, ug.REVERSE, None))
        
        #adding Wild cards to the Deck
        for wildcards in range (0,2):
            deck.append(UNOcard(None, ug.WILD, None))
        for wildDrawFours in range (0,2):
            deck.append(UNOcard(None, ug.WILD4, None))

        return deck
    
    def deckReset(hand1, hand2):
        deck = UNOcard.deckBuilder()
        for cards in range(0, len(hand1)):
            deck.remove(hand1[cards])
        for cards in range(0, len(hand2)):
            deck.remove(hand2[cards])
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
    
    def removeCard(deck, card):
        deck.remove(card)
    
    def displayHand(hand):
        print("Your Current Hand: ")
        for x in range(0,len(hand)):
            #If the color is nothing. Display Special form Dictionary
            if (UNOcard.getColor(hand[x]) == None):
                print (str(x+1) + ". " + ug.cardSpecials[UNOcard.getSpecial(hand[x])])

            #if value is nothing. Display color form Dictionary + Special from Dictionary
            elif (UNOcard.getValue(hand[x]) == None):
                print (str(x+1) + ". " + ug.cardColor[UNOcard.getColor(hand[x])] + " " +  ug.cardSpecials[UNOcard.getSpecial(hand[x])])
                
            #otherwise, display Color form Dictionary + Number
            else:
                print (str(x+1) + ". " + ug.cardColor[UNOcard.getColor(hand[x])] + " " + str(UNOcard.getValue(hand[x])))




  