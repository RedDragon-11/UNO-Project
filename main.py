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
reverseText = font.render("The Turns have been Reversed!", False, 'White')
drawTwoText = font.render("You +2'd The Computer!", False, 'White')
drawFourText = font.render("You +4'd The Computer!", False, 'White')
cpuSkipText = font.render("You've Been Skipped!", False, 'White')
cpuDrawTwoText = font.render("You've Been +2'd!", False, 'White')
cpuDrawFourText = font.render("You've Been +4'd!", False, 'White')
wrongCardText = font.render("Please Choose a different card.", False, 'White')


#Starting Variables
index = 0
selected = 0
playerCount = 4 
deck = UNOcard.deckBuilder()
centerCard = UNOlogic.setCenterCard(deck)
playerHand = UNOlogic.drawStartingHand(deck)
cpuHand = UNOlogic.drawStartingHand(deck)
reverse = False
if playerCount == 3:
    cpuHand2 = UNOlogic.drawStartingHand(deck)
elif playerCount == 4:
    cpuHand2 = UNOlogic.drawStartingHand(deck)
    cpuHand3 = UNOlogic.drawStartingHand(deck)
#cpu 1 vs player
cpuRevenge = 0

#cpu 2 doing something to 1
twoVsOneRevenge = 0

#cpu 2 doing something to 3
TwoVsThreeRevenge = 0

#cpu 3 doing something to 2
ThreeVsTwoRevenge = 0

#cpu 1 doing something against 2
OneVsTwoRevenge = 0

#cpu3 vs player
cpu3Revenge = 0


turn = 0
skip = 0
winCondition = 0
colorChoice = None
wildPlaced = False
wild4Placed = False




#Loop game till someone has no cards in their hand.
while True:
    selected = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if skip == 0:    
            if event.type == pg.KEYDOWN:
                if winCondition == 1:
                    pg.quit()
                    exit() 
                if event.key == pg.K_w:
                    print("W")
                    if(index < len(playerHand)):
                            screen.fill((39, 119, 20))
                            selected = index
                            if (UNOlogic.playableCard(centerCard, playerHand[selected]) == True):
                                print(ug.cardColor[UNOcard.getColor(playerHand[selected])] + " " + str(UNOcard.getValue(playerHand[selected])) + " " + ug.cardSpecials[UNOcard.getSpecial(playerHand[selected])])
                                index = 0
                                if(UNOcard.getSpecial(playerHand[selected]) == ug.WILD):
                                    prompt = font.render("Choose Color. 1 = Red. 2 = Blue. 3 = Green. 4 = Yellow", False, 'White')
                                    instruct = font.render("(Press on keyboard)", False, 'White')
                                    screen.blit(prompt, (200, 200))
                                    screen.blit(instruct, (200, 230))
                                    wildPlaced = True
                                    #print("PROBLEM WILD")

                                elif(UNOcard.getSpecial(playerHand[selected]) == ug.WILD4):
                                    screen.blit(drawFourText, (800, 170))
                                    prompt = font.render("Choose Color. 1 = Red. 2 = Blue. 3 = Green. 4 = Yellow", False, 'White')
                                    instruct = font.render("(Press on keyboard)", False, 'White')
                                    screen.blit(prompt, (200, 200))
                                    screen.blit(instruct, (200, 230))
                                    wild4Placed = True
                                    skip = 1
                                    if reverse == False:
                                        cpuRevenge += 25
                                        for val in range(0,4):
                                            cpuHand = UNOlogic.draw(deck, cpuHand)
                                    else:
                                        cpu3Revenge += 25
                                        for val in range(0,4):
                                            cpuHand3 = UNOlogic.draw(deck, cpuHand3)                                    
                                else:
                                    turn += 1
                            else:
                                screen.blit(wrongCardText, (800,200))
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
                    if reverse == False:
                        turn += 2
                    else:
                        turn -= 2

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
                    turn += 1      

                elif (colorChoice == 2 and wild4Placed == True):
                    centerCard = UNOcard(2, ug.WILD4, None, "small/2_w4.png")
                    wild4Placed = False
                    turn += 1      

                elif (colorChoice == 3 and wild4Placed == True):
                    centerCard = UNOcard(3, ug.WILD4, None, "small/3_w4.png")
                    wild4Placed = False
                    turn += 1      

                elif (colorChoice == 4 and wild4Placed == True):
                    centerCard = UNOcard(4, ug.WILD4, None, "small/4_w4.png")
                    wild4Placed = False
                    turn += 1      

        else:
            turn += 2
            skip = 0

                

        silhouette = pg.Rect(index * 100, 400, 136, 192)
        if (index <= 9):
            if skip == 1:
                pg.draw.rect(screen, 'Red', silhouette)
            else: 
                pg.draw.rect(screen, 'Purple', silhouette)
        else:
            silhouette = pg.Rect((index-10) * 100, 600, 136, 192)
            if skip  == 1:
                pg.draw.rect(screen, 'Red', silhouette)
            else: 
                pg.draw.rect(screen, 'Purple', silhouette)
        screen.blit(centerCardText, (1130, 400))
        screen.blit(UNOcard.getImage(centerCard), (1200, 450))
        screen.blit(handText, (300, 300))
        for cards in range(0, len(playerHand)):
            if (cards <= 9):
                screen.blit(UNOcard.getImage(playerHand[cards]), (100 * cards, 400))
            if (cards >= 10):
                screen.blit(UNOcard.getImage(playerHand[cards]), (100 * (cards-10), 600))

    
    if(turn <= playerCount and turn >= 0):
        if turn == 1:
            if skip == 0:
                print(str(selected) + " " + str(len(playerHand)))
                newCenter = playerHand[selected]
                screen.fill((39, 119, 20), ((len(playerHand)-1)*100,400,136,192))

                if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                    screen.blit(drawTwoText, (800, 200))
                    skip = 1
                    if reverse == False:
                        turn += 1
                        cpuRevenge += .15
                        for val in range(0,2):
                            cpuHand = UNOlogic.draw(deck, cpuHand)
                    else:
                        turn -= 2
                        cpu3Revenge += .15
                        for val in range(0,2):
                            cpuHand3 = UNOlogic.draw(deck, cpuHand3)

                    #print("PROBLEM DRAW 2")
                    for val in range(0,2):
                        cpuHand = UNOlogic.draw(deck, cpuHand)

                elif(UNOcard.getSpecial(newCenter) == ug.SKIP):
                        screen.blit(skipText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            cpuRevenge += 15
                        else:
                            turn -= 2
                            cpu3Revenge += 15
                        #print("PROBLEM SKIP")

                elif(UNOcard.getSpecial(newCenter) == ug.REVERSE):
                        if reverse == False:
                            screen.blit(reverseText, (800,200))
                            reverse = True
                            turn -= 2
                            cpuRevenge += 10
                            print(str(turn))
                        elif reverse == True:
                            screen.blit(reverseText, (800,200))
                            reverse = False
                            turn += 1
                            cpu3Revenge += 10
                            print(str(turn))
                        print("Resolving Reverse")

                else: 
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 2
                        #print("PROBLEM PLAYED NORMAL")
                playerHand.remove(playerHand[selected])
                centerCard = newCenter
            else: 
                skip = 0
                if reverse == False:
                    turn += 1
                else:
                    turn -= 2
            print("It is now turn" + str(turn))
                
            
        
        elif turn == 2:
            print("Its Computer #1's Turn!")
            if(skip == 0):
                counterMax = 0
                chosenCard = None
                temp = 0
                print("My hand is " + str(len(cpuHand)) + " Cards Long.")
                for value in range(0, len(cpuHand)):
                    if (UNOlogic.playableCard(centerCard, cpuHand[value])) == True:
                        print(ug.cardColor[UNOcard.getColor(cpuHand[value])] + " " + str(UNOcard.getValue(cpuHand[value])))
                        if reverse == False:
                            temp = UNOlogic.handOptimizer(cpuHand[value], cpuHand, twoVsOneRevenge, centerCard)
                            if temp[1] > counterMax:
                                chosenCard = temp[0]
                                counterMax = temp[1]
                        else: 
                            temp = UNOlogic.handOptimizer(cpuHand[value], cpuHand, cpuRevenge, centerCard)
                            if temp[1] > counterMax:
                                chosenCard = temp[0]
                                counterMax = temp[1]                            
                    
                output = UNOlogic.cpuPlay(deck, centerCard, cpuHand, chosenCard, turn)
                newCenter = output[0]
                newHand = output[1]

                if newCenter != None:
                    centerCard = newCenter
                    if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                        screen.blit(cpuDrawTwoText, (800, 150))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            OneVsTwoRevenge += 15
                        else:
                            turn -= 2
                        for val in range(0,2):
                            playerHand = UNOlogic.draw(deck, playerHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                        screen.blit(cpuDrawFourText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            OneVsTwoRevenge += 25
                        else:
                            turn -= 2
                        for val in range(0, 4):
                            playerHand = UNOlogic.draw(deck, playerHand)
                    
                    elif(UNOcard.getSpecial(newCenter) == ug.SKIP):
                        screen.blit(skipText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            OneVsTwoRevenge += 15
                        else:
                            turn -= 2
                        #print("PROBLEM SKIP")

                    elif(UNOcard.getSpecial(newCenter) == ug.REVERSE):
                        print("Resolving Reverse")
                        if reverse == False:
                            screen.blit(reverseText, (800,200))
                            reverse = True
                            turn -= 2
                            OneVsTwoRevenge += 10
                            print("It is now turn" + str(turn))
                        elif reverse == True:
                            screen.blit(reverseText, (800,200))
                            reverse = False
                            turn += 1
                            print("It is now turn" + str(turn))
                        
                    elif(UNOcard.getValue(newCenter) != None): 
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 2

                else:
                    cpuHand = newHand
                    if reverse == False:
                        turn += 1
                    else:
                        turn -= 2
            else: 
                print("Computer #1 is Skipped!")
                skip = 0
                if reverse == False:
                    turn += 1
                else:
                    turn -= 2
                print("Turn Status: " + str(turn))
            print("It is now turn" + str(turn))

        elif turn == 3:
            print("Its Computer #2's Turn!")
            if(skip == 0):
                counterMax = 0
                chosenCard = None
                temp = 0
                print("My hand is " + str(len(cpuHand2)) + " Cards Long.")
                for value2 in range(0, len(cpuHand2)):
                    if (UNOlogic.playableCard(centerCard, cpuHand2[value2])) == True:
                        print(ug.cardColor[UNOcard.getColor(cpuHand2[value2])] + " " + str(UNOcard.getValue(cpuHand2[value2])))
                        if reverse == False:
                            temp = UNOlogic.handOptimizer(cpuHand2[value2], cpuHand2, ThreeVsTwoRevenge, centerCard)
                            if temp[1] > counterMax:
                                chosenCard = temp[0]
                                counterMax = temp[1]
                        else: 
                            temp = UNOlogic.handOptimizer(cpuHand2[value2], cpuHand2, twoVsOneRevenge, centerCard)
                            if temp[1] > counterMax:
                                chosenCard = temp[0]
                                counterMax = temp[1]            
                    
                output = UNOlogic.cpuPlay(deck, centerCard, cpuHand2, chosenCard, turn)
                newCenter = output[0]
                newHand = output[1]

                if newCenter != None:
                    centerCard = newCenter
                    if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                        screen.blit(cpuDrawTwoText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            TwoVsThreeRevenge += 15
                        else:
                            turn -= 1
                            twoVsOneRevenge += 15
                        for val in range(0,2):
                            playerHand = UNOlogic.draw(deck, playerHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                        screen.blit(cpuDrawFourText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            TwoVsThreeRevenge += 25
                        else:
                            turn -= 1
                            twoVsOneRevenge += 25
                        for val in range(0, 4):
                            playerHand = UNOlogic.draw(deck, playerHand)
                        
                    elif(UNOcard.getSpecial(newCenter) == ug.REVERSE):
                        print("Resolving Reverse")
                        if reverse == False:
                            screen.blit(reverseText, (800,200))
                            reverse = True
                            turn -= 1
                            print("Turn should now be CPU 1")
                            TwoVsThreeRevenge += 10
                            print("It is now turn" + str(turn))
                        elif reverse == True:
                            screen.blit(reverseText, (800,200))
                            reverse = False
                            turn += 1
                            twoVsOneRevenge += 10
                            print(str(turn))
                        

                    elif(UNOcard.getSpecial(newCenter) == ug.SKIP):
                        screen.blit(cpuSkipText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                            TwoVsThreeRevenge += 15
                        else:
                            turn -= 1
                            twoVsOneRevenge += 15

                    elif(UNOcard.getValue(newCenter) != None): 
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 1
                else:
                    cpuHand2 = newHand
                    if reverse == False:
                        turn += 1
                    else:
                        turn -= 1


            else: 
                print("Computer #2 is Skipped!")
                skip = 0
                if reverse == False:
                    turn += 1
                else:
                    turn -= 1
                print("Turn Status: " + str(turn))
            print("It is now turn " + str(turn))

        elif turn == 4:
            print("Its Computer #3's Turn!")
            if(skip == 0):
                counterMax = 0
                topCard = None
                temp = 0
                print("My hand is " + str(len(cpuHand3)) + " Cards Long.")
                for value3 in range(0, len(cpuHand3)):
                    if (UNOlogic.playableCard(centerCard, cpuHand3[value3])) == True:
                        chosenCard = cpuHand3[value3] 
                        print(ug.cardColor[UNOcard.getColor(chosenCard)] + " " + str(UNOcard.getValue(chosenCard)))
                        if reverse == False:
                            temp = UNOlogic.handOptimizer(chosenCard, cpuHand3, cpu3Revenge, centerCard)
                            if temp[1] > counterMax:
                                topCard = temp[0]
                                counterMax = temp[1]
                        else: 
                            temp = UNOlogic.handOptimizer(chosenCard, cpuHand3, TwoVsThreeRevenge, centerCard)
                            if temp[1] > counterMax:
                                topCard = temp[0]
                                counterMax = temp[1]            
                    
                output = UNOlogic.cpuPlay(deck, centerCard, cpuHand3, topCard, turn)
                newCenter = output[0] 
                newHand = output[1]

                if newCenter != None:
                    centerCard = newCenter
                    if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                        screen.blit(cpuDrawTwoText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 1
                            ThreeVsTwoRevenge += 15
                        for val in range(0,2):
                            playerHand = UNOlogic.draw(deck, playerHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                        screen.blit(cpuDrawFourText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 1
                            ThreeVsTwoRevenge += 25
                        for val in range(0, 4):
                            playerHand = UNOlogic.draw(deck, playerHand)

                    elif(UNOcard.getSpecial(newCenter) == ug.REVERSE):
                        if reverse == False:
                            screen.blit(reverseText, (800,200))
                            reverse = True
                            turn -= 2
                            print(str(turn))
                        elif reverse == True:
                            screen.blit(reverseText, (800,200))
                            reverse = False
                            turn += 1
                            ThreeVsTwoRevenge += 15
                            print(str(turn))
                        print("Resolving Reverse")
                    
                    elif(UNOcard.getSpecial(newCenter) == ug.SKIP):
                        screen.blit(cpuSkipText, (800, 200))
                        skip = 1
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 1
                            ThreeVsTwoRevenge += 15

                    elif(UNOcard.getValue(newCenter) != None): 
                        if reverse == False:
                            turn += 1
                        else:
                            turn -= 1

                else:
                    cpuHand3 = newHand
                    if reverse == False:
                        turn += 1
                    else:
                        turn -= 1


            else: 
                print("Computer #3 is Skipped!")
                skip = 0
                if reverse == False:
                    turn += 1
                else:
                    turn -= 1
                print("Turn Status: " + str(turn))
            print("It is now turn" + str(turn))
    else:
        print(str(turn))
        print("resetting turns")
        if reverse == False:
            turn = 0
            print("Players Turn")
        elif reverse == True:
            turn = playerCount
            print("CPUs Turn")
        
    
    if len(playerHand) == 0 or playerHand == None:
        winText = font2.render("YOU WIN!", False, 'White')
        screen.blit(winText, (800, 100))
        winCondition = 1
    elif len(cpuHand) == 0 or cpuHand == None:
        winText = font2.render("THE COMPUTER WINS!", False, 'White')
        screen.blit(winText, (800, 100))
        winCondition = 1
    
    elif playerCount == 3:
        if len(cpuHand2) == 0 or cpuHand2 == None:
            winText = font2.render("THE COMPUTER 2 WINS!", False, 'White')
            screen.blit(winText, (800, 100))
            winCondition = 1

    elif playerCount == 4:
        if len(cpuHand3) == 0 or cpuHand3 == None:
            winText = font2.render("THE COMPUTER 3 WINS!", False, 'White')
            screen.blit(winText, (800, 100))
            winCondition = 1

    if len(deck) == 0 or deck == None:
        deck = UNOcard.deckBuilder()

    pg.display.update()
    clock.tick(9999)
