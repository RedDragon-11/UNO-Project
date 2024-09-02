import pygame.display

from UNOcard import UNOcard
from UNOlogic import UNOlogic
import UNOGlobals as ug
import pygame as pg
pg.init()

window = screen_width, screen_height = 1600, 900
screen = pg.display.set_mode(window)
pg.display.set_caption("UNO!")
screen.fill((39, 119, 20))
clock = pg.time.Clock()

font = pg.font.Font(None, 40)
font2 = pg.font.Font(None, 56)

centerCardText = font.render('Current Center Card', False, 'White')
handText = font.render('Your Hand', False, 'White')
skipText = font.render("You Skipped The Computer!", False, 'White')
drawTwoText = font.render("You +2'd The Computer!", False, 'White')
drawFourText = font.render("You +4'd The Computer!", False, 'White')
cpuSkipText = font.render("You've Been Skipped!", False, 'White')
cpuDrawTwoText = font.render("You've Been +2'd!", False, 'White')
cpuDrawFourText = font.render("You've Been +4'd!", False, 'White')

#Starting Variables
index = 0
selected = 0
playerCount = 2 
deck = UNOcard.deckBuilder()
centerCard = UNOlogic.setCenterCard(deck)
playerHand = UNOlogic.drawStartingHand(deck)
cpuHand = UNOlogic.drawStartingHand(deck)
if playerCount == 3:
    cpuHand2 = UNOlogic.drawStartingHand(deck)
if playerCount == 4:
    cpuHand3 = UNOlogic.drawStartingHand(deck)
skipped = False
turn = 0
skip = 0
winCondition = 0
colorChoice = None
wildPlaced = False
wild4Placed = False




print(turn)
#Loop game till someone has no cards in their hand.
while True:
    selected = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if winCondition == 1:
                pg.quit()
                exit() 
            if event.key == pg.K_w:
                print("W")
                if(index < len(playerHand)):
                    if skip == 0:
                        selected = index
                        print(ug.cardColor[UNOcard.getColor(playerHand[selected])] + " " + str(UNOcard.getValue(playerHand[selected])) + " " + ug.cardSpecials[UNOcard.getSpecial(playerHand[selected])])
                        index = 0
                        turn += 1
                    else:
                        turn += 1
                    
                else:
                    index = 0
            if event.key == pg.K_a:
                screen.fill((39, 119, 20))
                print("A")
                if index > 0:
                    index -= 1
                print("Index: " + str(index))
            if event.key == pg.K_d:
                screen.fill((39, 119, 20))
                print("D")
                if (index < len(playerHand)-1):
                    index += 1
                print("Index: " + str(index))
            if event.key == pg.K_s:
                screen.fill((39, 119, 20))
                print("S")
                playerHand = UNOlogic.draw(deck, playerHand)
                index = 0
                turn += 1
            if event.key == pg.K_1:
                colorChoice = 1
            if event.key == pg.K_2:
                colorChoice = 2
            if event.key == pg.K_3:
                colorChoice = 3
            if event.key == pg.K_4:
                colorChoice = 4
            if (colorChoice == 1 and wildPlaced == True):
                centerCard = UNOcard(1, ug.WILD, None, "small/1_w.png")
                wildPlaced = False
                turn += 1
            elif (colorChoice == 2 and wildPlaced == True):
                centerCard = UNOcard(2, ug.WILD, None, "small/2_w.png")
                wildPlaced = False
                turn += 1
            elif (colorChoice == 3 and wildPlaced == True):
                centerCard = UNOcard(3, ug.WILD, None, "small/3_w.png")
                wildPlaced = False
                turn += 1
            elif (colorChoice == 4 and wildPlaced == True):
                centerCard = UNOcard(4, ug.WILD, None, "small/4_w.png")
                wildPlaced = False
                turn += 1
            elif (colorChoice == 1 and wild4Placed == True):
                centerCard = UNOcard(1, ug.WILD4, None, "small/1_w4.png")
                wild4Placed = False
                
            elif (colorChoice == 2 and wild4Placed == True):
                centerCard = UNOcard(2, ug.WILD4, None, "small/2_w4.png")
                wild4Placed = False
              
            elif (colorChoice == 3 and wild4Placed == True):
                centerCard = UNOcard(3, ug.WILD4, None, "small/3_w4.png")
                wild4Placed = False
                
            elif (colorChoice == 4 and wild4Placed == True):
                centerCard = UNOcard(4, ug.WILD4, None, "small/4_w4.png")
                wild4Placed = False
                

        silhouette = pg.Rect(index * 100, 400, 136, 192)
        if (index <= 9):
            pg.draw.rect(screen, 'Purple', silhouette)
        else:
            silhouette = pg.Rect((index-10) * 100, 600, 136, 192)
            pg.draw.rect(screen, 'Purple', silhouette)
        screen.blit(centerCardText, (1130, 400))
        screen.blit(UNOcard.getImage(centerCard), (1200, 450))
        screen.blit(handText, (300, 300))
        for cards in range(0, len(playerHand)):
            if (cards <= 9):
                screen.blit(UNOcard.getImage(playerHand[cards]), (100 * cards, 400))
            if (cards >= 10):
                screen.blit(UNOcard.getImage(playerHand[cards]), (100 * (cards-10), 600))


    ## Need fix up CPU turn orders. Currently not going to work with Reverses or Skips.
    if(turn <= playerCount):
        if turn == 1:
            if skip == 0:
                if (UNOlogic.playableCard(centerCard, playerHand[selected]) == True):
                    newCenter = playerHand[selected]
                    screen.fill((39, 119, 20), ((len(playerHand)-1)*100,400,136,192))
                    if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                        screen.blit(drawTwoText, (800, 200))
                        skip = 1
                        turn += 1
                        #print("PROBLEM DRAW 2")
                        for val in range(0,2):
                            cpuHand = UNOlogic.draw(deck, cpuHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                        screen.blit(drawFourText, (800, 170))
                        prompt = font.render("Choose Color. 1 = Red. 2 = Blue. 3 = Green. 4 = Yellow", False, 'White')
                        instruct = font.render("(Press on keyboard)", False, 'White')
                        screen.blit(prompt, (200, 200))
                        screen.blit(instruct, (200, 230))
                        wild4Placed = True
                        skip = 1
                        turn += 1
                        #print("PROBLEM WILD 4")
                        for val in range(0, 4):
                            cpuHand = UNOlogic.draw(deck, cpuHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.WILD):
                        prompt = font.render("Choose Color. 1 = Red. 2 = Blue. 3 = Green. 4 = Yellow", False, 'White')
                        instruct = font.render("(Press on keyboard)", False, 'White')
                        screen.blit(prompt, (200, 200))
                        screen.blit(instruct, (200, 230))
                        wildPlaced = True
                        turn += 1
                        #print("PROBLEM WILD")

                    elif(UNOcard.getSpecial(newCenter) == ug.SKIP):
                        screen.blit(skipText, (800, 200))
                        skip = 1
                        turn += 1 
                        #print("PROBLEM SKIP")

                    else: 
                        turn += 1
                        #print("PROBLEM PLAYED NORMAL")
                    playerHand.remove(playerHand[selected])
                    centerCard = newCenter
            else: 
                skip = 0
                turn +=1
                #print("PROBLEM RESOLVE SKIP")
            
        
        elif turn == 2:
            print("Its Computer #1's Turn!")
            if(skip == 0):
                output = UNOlogic.cpuPlay(deck, centerCard, cpuHand, turn)
                newCenter = output[0]
                newHand = output[1]

                if newCenter != None:
                    centerCard = newCenter
                    turn += 1
                    if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                        screen.blit(cpuDrawTwoText, (800, 200))
                        skip = 1
                        turn += 1
                        for val in range(0,2):
                            playerHand = UNOlogic.draw(deck, playerHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                        screen.blit(cpuDrawFourText, (800, 200))
                        skip = 1
                        turn += 1
                        for val in range(0, 4):
                            playerHand = UNOlogic.draw(deck, playerHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.SKIP):
                        screen.blit(cpuSkipText, (800, 200))
                        skip = 1
                        turn += 1
                else:
                    cpuHand = newHand
                    turn += 1


            else: 
                print("Computer #1 is Skipped!")
                skip = 0
                turn += 1
                print("Turn Status: " + str(turn))

    else:
        print("resetting turns to Turn 1")
        turn = 0
        
    
    if len(playerHand) == 0 or playerHand == None:
        winText = font2.render("YOU WIN!", False, 'White')
        screen.blit(winText, (800, 100))
        winCondition = 1
    elif len(cpuHand) == 0 or cpuHand == None:
        winText = font2.render("THE COMPUTER WINS!", False, 'White')
        screen.blit(winText, (800, 100))
        winCondition = 1
    #elif len(cpuHand2) == 0 or cpuHand2 == None:
       # winText = font2.render("THE COMPUTER 2 WINS!", False, 'White')
       # screen.blit(winText, (800, 100))
       # winCondition = 1
    #elif len(cpuHand3) == 0 or cpuHand3 == None:
       # winText = font2.render("THE COMPUTER 3 WINS!", False, 'White')
       # screen.blit(winText, (800, 100))
       # winCondition = 1

    if len(deck) == 0 or deck == None:
        deck = UNOcard.deckBuilder()

    pg.display.update()
    clock.tick(9999)
