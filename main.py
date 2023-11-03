from UNOcard import UNOcard
from UNOlogic import UNOlogic
import UNOGlobals as ug
import pygame as pg
from UNOdisplay import UNOdisplay
global screen
pg.init()


window = screen_width, screen_height = 1600, 900
screen = pg.display.set_mode(window)
screen.fill('black')
clock = pg.time.Clock()

#Starting Variables
deck = UNOcard.deckBuilder()
centerCard = UNOlogic.setCenterCard(deck)
playerHand = UNOlogic.drawStartingHand(deck)
cpuHand = UNOlogic.drawStartingHand(deck)
gameOver = False
skipped = False

#Loop game till someone has no cards in their hand.
while (gameOver == False):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
            break
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                quit()
                break


    #output formated as [newCenter, newHand]
    #This section gets the results of what the player plays, makes it the center card and removes the card from the player's hand
    #the if statements check if the player drew a card, if they did just set the new hand. if they didn't check to see if the card that was played was a draw 2, draw 4 , etc...
    #Realistically, I could have made that a function but I got lazy. Same for the cpu section.
    if(skipped == False):
        UNOdisplay.draw_hand_visble(playerHand, centerCard, screen)
        output = UNOlogic.play(deck, centerCard, playerHand, cpuHand)
        newCenter = output[0]
        newHand = output[1]
        if (newCenter != None):
            centerCard = newCenter
            if(UNOcard.getSpecial(newCenter) ==  ug.DRAW2):
                print("You've +2'd the Computer!")
                for num in range(2):
                    cpuHand = UNOlogic.draw(deck, cpuHand)
                print("The Computer now has: " + str(len(cpuHand)) + " Cards.")
            elif(UNOcard.getSpecial(newCenter) ==  ug.WILD4):
                print("You've +4'd the Computer!!")
                for num in range(4):
                    cpuHand = UNOlogic.draw(deck, cpuHand)  
                print("The Computer now has: " + str(len(cpuHand)) + " Cards.")
            #In 1v1 Uno, a reverse is effectively a skip since it makes the turn order come back to you. At Least thats my understanding. 
            #Its either an effect skip or a card that has no effect. I opted in for it being another form of a skip
            elif(UNOcard.getSpecial(newCenter) == ug.SKIP or UNOcard.getSpecial(newCenter) == ug.REVERSE): 
                print("The Computer's turn has been skipped!")
                skipped = True
        palyerHand = newHand
    else:
        skipped = False
    
    
    if(len(playerHand) == 0 or playerHand == None):
        print("You win!")
        quit()
        break
    
   
    #output formated as [newCenter, newHand]
    #This section gets the results of what the cpu plays, makes it the center card and removes the card from the cpus's hand
    if(skipped == False):
        cpuOutput = UNOlogic.cpuPlay(deck, centerCard, cpuHand, playerHand)
        newCenter = cpuOutput[0]
        newHand = cpuOutput[1]
        if (newCenter != None):
            centerCard = newCenter
            if(UNOcard.getSpecial(newCenter) ==  ug.DRAW2):
                print("You've Been +2'd!")
                for num in range(2):
                    playerHand = UNOlogic.draw(deck, playerHand)
            elif(UNOcard.getSpecial(newCenter) ==  ug.WILD4):
                print("You've Been +4'd!!")
                for num in range(4):
                    playerHand = UNOlogic.draw(deck, playerHand) 
            elif(UNOcard.getSpecial(newCenter) == ug.SKIP or UNOcard.getSpecial(newCenter) == ug.REVERSE): 
                print("Your turn has been skipped!")
                skipped = True
        cpuHand = newHand
    else:
        skipped = False

    if(len(cpuHand) == 0 or cpuHand == None):
      print("The Computer Wins!")
      break
    
    
    #Game win Status Checks
    if(len(cpuHand) == 2):
        print("The Computer only has 2 cards Left!")
    if(len(cpuHand) == 1):
        print("The Computer only has 1 card Left! They have UNO!")
    
    if(len(playerHand) == 2):
        print("You only have 2 cards Left!")
    if(len(playerHand) == 1):
        print("You only have 1 card Left! You have UNO!")

    #Replenishes deck if it runs out
    if((len(deck) == 0)):
        deck = UNOcard.deckReset(cpuHand, playerHand)
    clock.tick(60)

userInput = input("Would you want to play again?(y/n)")

if(userInput.lower() == 'y'):
    input("Then you'll need to close and reopen the file. I was planning on using recursion to loop the game but got lazy. I am sorry. Press enter to close window.")
elif(userInput.lower() == 'n'):
    input("Press enter to close window.")
else:
    input("I didn't quite catch that... I guess... Press enter to close window.")


    


   


        
    


