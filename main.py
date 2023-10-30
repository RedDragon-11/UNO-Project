from UNOcard import UNOcard
from UNOlogic import UNOlogic
import UNOGlobals as ug

deck = []
centerCard = None
playerHand = []
cpuHand = []
gameOver = False
cpuSkipped = False
playerSkipped = False

deck = UNOcard.deckBuilder()
playerHand = UNOlogic.drawStartingHand(deck)
cpuHand = UNOlogic.drawStartingHand(deck)
centerCard = UNOlogic.setCenterCard(deck)


#Loop game till someone has no cards in their hand.
while (gameOver == False):
    UNOcard.displayHand(playerHand)
    UNOlogic.displayCenter(centerCard)

    #output formated as [newCenter, newHand]
    #This section gets the results of what the player plays, makes it the center card and removes the card from the player's hand
    #the if statements check if the player drew a card, if they did just set the new hand. if they didn't check to see if the card that was played was a draw 2 or draw 4
    #Realistically, I could have made that a function but I got lazy. Same for the cpu section.
    if(playerSkipped == False):
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
            #In 1v1 Uno, a reverse is effectively a skip since it makes the turn order come back to you. At Least that my understand. 
            #Its either an effect skip or a card that has no effect. I opted in for it being another form of a skip
            elif(UNOcard.getSpecial(newCenter) == ug.SKIP or UNOcard.getSpecial(newCenter) == ug.REVERSE): 
                    print("The Computer's turn has been skipped!")
                    cpuSkipped == True
        palyerHand = newHand
    elif(playerSkipped == True):
        playerSkipped == False

    
   
    #output formated as [newCenter, newHand]
    #This section gets the results of what the cpu plays, makes it the center card and removes the card from the cpus's hand
    if(cpuSkipped == False):
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
            elif(UNOcard.getSpecial(newCenter) == ug.SKIP or UNOcard.getSpecial(newCenter) == ug.REVERSE): 
                    print("Your turn has been skipped!")
                    playerSkipped = True
        cpuHand = newHand
    elif(cpuSkipped == True):
        cpuSkipped = False

      
    
    
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
    

    


   


        
    


