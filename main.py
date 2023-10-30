from UNOcard import UNOcard
from UNOlogic import UNOlogic
import UNOGlobals as ug
deck = []
centerCard = None
playerHand = []
cpuHand = []

deck = UNOcard.deckBuilder()
playerHand = UNOlogic.drawStartingHand(deck)


UNOcard.displayHand(playerHand)


        
    


#print (UNOlogic.playableCard((UNOcard(ug.GREEN, ug.GENERAL, 7)), (UNOcard(ug.GREEN, ug.GENERAL, 2))))
#print (UNOlogic.playableCard((UNOcard(ug.BLUE, ug.GENERAL, 7)), (UNOcard(ug.GREEN, ug.GENERAL, 7))))
#print (UNOlogic.playableCard((UNOcard(ug.RED, ug.DRAW2, None)), (UNOcard(ug.GREEN, ug.DRAW2, None))))
#print (UNOlogic.playableCard((UNOcard(ug.GREEN, ug.GENERAL, 7)), (UNOcard(ug.NONE, ug.WILD, None))))
#print (UNOlogic.playableCard((UNOcard(ug.GREEN, ug.GENERAL, 7)), (UNOcard(ug.RED, ug.GENERAL, 2))))