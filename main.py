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
cpuHand = (UNOlogic.drawStartingHand(deck)) 
centerCard = UNOlogic.setCenterCard(deck)


#Loop game till someone has no cards in their hand.
while (gameOver == False):
    UNOcard.displayHand(playerHand)
    UNOcard.displayHand(cpuHand)
    UNOlogic.displayCenter(centerCard)
    output = UNOlogic.play(deck, centerCard, playerHand, cpuHand)
    newCenter = output[0]
    newHand = output[1]

    if (newCenter != None):
        centerCard = newCenter
        if(UNOcard.getSpecial(newCenter) ==  ug.DRAW2):
            print("You've +2'd the Computer!")
            for num in range(0,2):
                cpuHand = UNOlogic.draw(deck, cpuHand)
        elif(UNOcard.getSpecial(newCenter) ==  ug.WILD4):
            print("You've +4'd the Computer!!")
            for num in range(0,4):
                cpuHand = UNOlogic.draw(deck, cpuHand)        
    
    palyerHand = newHand

    
    cpuOutput = UNOlogic.cpuPlay(deck, centerCard, cpuHand, playerHand)
    newCenter = cpuOutput[0]
    newHand = cpuOutput[1]

    if (newCenter != None):
        centerCard = newCenter
        if(UNOcard.getSpecial(newCenter) ==  ug.DRAW2):
            print("You've Been +2'd!")
            for num in range(0,2):
                playerHand = UNOlogic.draw(deck, playerHand)
        elif(UNOcard.getSpecial(newCenter) ==  ug.WILD4):
            print("You've Been +4'd!!")
            for num in range(0,4):
                playerHand = UNOlogic.draw(deck, playerHand)     
      
    cpuHand = newHand
    
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
        if(playerHand == 0):
            print("You win!")
        elif(cpuHand == 0):
            print("The Computer Won!")
        gameOver == True
    

    


   


        
    


