from UNOcard import UNOcard
from UNOlogic import UNOlogic
import UNOGlobals as ug

deck = []
centerCard = None
playerHand = []
cpuHand = []
gameOver = False

deck = UNOcard.deckBuilder()
playerHand = UNOlogic.drawStartingHand(deck)
cpuHand = UNOlogic.drawStartingHand(deck)
centerCard = UNOlogic.setCenterCard(deck)

#Loop game till someone has no cards in their hand.
while (gameOver == False):
    UNOcard.displayHand(playerHand)
    UNOlogic.displayCenter(centerCard)
    output = UNOlogic.play(deck, centerCard, playerHand, cpuHand)

    if (output[0] != None):
        centerCard = output[0]
    palyerHand = output[1]
    
    cpuOutput = UNOlogic.cpuPlay(deck, centerCard, cpuHand, playerHand)
    if (cpuOutput[0] != None):
        centerCard = cpuOutput[0]
    cpuHand = cpuOutput[1]
    
    #Game win Status Checks
    if(len(cpuHand) == 2):
        print("The Computer only has 2 cards Left!")
    elif(len(cpuHand) == 1):
        print("The Computer only has 1 card Left! They have UNO!")
    
    if(len(playerHand) == 2):
        print("You only have 2 cards Left!")
    elif(len(palyerHand) == 1):
        print("You only have 1 card Left! You have UNO!")

    #replenishes deck if it runs out
    if((len(deck) == 0)):
        deck = UNOcard.deckReset(cpuHand, playerHand)

    #game ender
    if (len(playerHand) == 0 or len(cpuHand) == 0):
        gameOver == True
    

    


   


        
    


