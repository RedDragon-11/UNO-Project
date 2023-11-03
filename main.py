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
index = 0

#Starting Variables
deck = UNOcard.deckBuilder()
centerCard = UNOlogic.setCenterCard(deck)
playerHand = UNOlogic.drawStartingHand(deck)
cpuHand = UNOlogic.drawStartingHand(deck)
skipped = False
turn = 0
cpuTurn = 0

#Loop game till someone has no cards in their hand.
while True:
    selected = 0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                print("W")
                if(index < len(playerHand)):
                    selected = index
                    print(str(UNOcard.getColor(playerHand[selected])) + " " + str(UNOcard.getValue(playerHand[selected])) + " " + str(UNOcard.getSpecial(playerHand[selected])))
                    index = 0
                    turn = 1
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
                cpuTurn = 1


        screen.blit(centerCardText, (1130, 400))
        screen.blit(UNOcard.getImage(centerCard), (1200, 450))
        screen.blit(handText, (300, 300))
        for cards in range(0, len(playerHand)):
            if (cards <= 10):
                screen.blit(UNOcard.getImage(playerHand[cards]), (100 * cards, 400))
            if (cards > 10):
                screen.blit(UNOcard.getImage(playerHand[cards]), (100 * (cards-10), 580))




    if turn == 1:
        if (UNOlogic.playableCard(centerCard, playerHand[selected]) == True):
            screen.fill((39, 119, 20))
            newCenter = playerHand[selected]
            if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                screen.blit(drawTwoText, (800, 200))
                for val in range(0,2):
                    cpuHand = UNOlogic.draw(deck, cpuHand)
            elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                screen.blit(drawFourText, (800, 200))
                for val in range(0, 4):
                    cpuHand = UNOlogic.draw(deck, cpuHand)
            elif(UNOcard.getSpecial(newCenter) == ug.SKIP or UNOcard.getSpecial(newCenter) == ug.REVERSE):
                screen.blit(skipText, (800, 200))
                cpuTurn = 0
            else:
                cpuTurn = 1
            playerHand.remove(playerHand[selected])
            centerCard = newCenter
            UNOlogic.displayHand(playerHand)
            turn = 0
    elif cpuTurn == 1:
        cpuTurn = 0
        output = UNOlogic.cpuPlay(deck, centerCard, cpuHand)
        newCenter = output[0]
        newHand = output[1]
        if newCenter != None:
            centerCard = newCenter
            if (UNOcard.getSpecial(newCenter) == ug.DRAW2):
                screen.blit(cpuDrawTwoText, (800, 200))
                for val in range(0,2):
                    playerHand = UNOlogic.draw(deck, playerHand)
            elif(UNOcard.getSpecial(newCenter) == ug.WILD4):
                screen.blit(cpuDrawFourText, (800, 200))
                for val in range(0, 4):
                    playerHand = UNOlogic.draw(deck, playerHand)
            elif(UNOcard.getSpecial(newCenter) == ug.SKIP or UNOcard.getSpecial(newCenter) == ug.REVERSE):
                screen.blit(cpuSkipText, (800, 200))
                cpuTurn = 1

        cpuHand = newHand


    if len(playerHand) == 0 or playerHand == None:
        winText = font2.render("YOU WIN!", False, 'White')
        screen.blit(winText, (800, 100))
    elif len(cpuHand) == 0 or cpuHand == None:
        winText = font2.render("THE COMPUTER WINS!", False, 'White')
        screen.blit(winText, (800, 100))

    pg.display.update()
    clock.tick(120)
