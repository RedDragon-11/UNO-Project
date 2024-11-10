from UNOcard import UNOcard
import UNOGlobals as ug
import random
import pygame as pg


class UNOlogic:
    
    def playableCard(centerCard, playedCard):
        #Checks playedCard Color to centerCard.
        if(UNOcard.getColor(centerCard) == UNOcard.getColor(playedCard)):
            return True
        
        #As long as playedCard value or centerCard value aren't a special card. Check if values match
        elif(UNOcard.getValue(centerCard) != None and UNOcard.getValue(playedCard) != None):
             if(UNOcard.getValue(centerCard) == UNOcard.getValue(playedCard)):
                return True
             elif(UNOcard.getValue(centerCard) != UNOcard.getValue(playedCard)):
                return False
             
        #Checks if two cards are the same speical
        elif(UNOcard.getSpecial(centerCard) == UNOcard.getSpecial(playedCard)):
            return True
        
        #Checks if card is wildcard
        elif(UNOcard.getSpecial(playedCard) == ug.WILD or UNOcard.getSpecial(playedCard) == ug.WILD4):
            return True
        
        #default
        else:
            return False
           
    def handOptimizer(cardCandidate, hand, revenge, centerCard):
        counter = 0
        if revenge >= 35:
            if random.randint(0,100) <= revenge:
                print("Revenge Activated.")
                for cards in range(0,len(hand)):
                    if UNOcard.getSpecial(hand[cards]) == ug.SKIP or ug.DRAW2 or ug.REVERSE:
                        if UNOlogic.playableCard(centerCard, hand[cards]) == True:
                            counter = 20
                            outputRevenge = [cardCandidate, counter]
                            return outputRevenge

        for cards in range(0, len(hand)):
            if UNOlogic.playableCard(cardCandidate, hand[cards]) == True:
                counter += 1
                print(ug.cardColor[UNOcard.getColor(cardCandidate)] + " " + str(UNOcard.getValue(cardCandidate)) + " " + str(UNOcard.getSpecial(cardCandidate)) + " can play " + str(counter) + " cards.")
                output = [cardCandidate, counter]
        return output

    
    
                 
    def drawStartingHand(deck):
        hand = []
        for val in range(0,7):
                card = random.choice(deck)
                UNOcard.removeCard(deck, card)
                hand.append(card)
        return hand
    
    #play function for human player
    #def play(centerCard, playerHand):
    #    a = 1
    
    def cpuPlay(deck, centerCard, cpuHand, chosenCard, playerPosition):
        if(chosenCard != None):
            drawCard = False
            #if the card selected is a wildcard
            if(UNOcard.getColor(chosenCard) == None):
                cpuHand.remove(chosenCard)
                card = UNOlogic.cpuSetWildCard(cpuHand, chosenCard)
                output = [card, cpuHand]
                return output
            else:
                centerCard = chosenCard
                cpuHand.remove(chosenCard)
                output = [centerCard, cpuHand]
                UNOlogic.displayCard(centerCard)
                return output
        else: drawCard = True

        if(drawCard == True):
            output = [None, UNOlogic.draw(deck, cpuHand)]
            print("Computer #" + str(playerPosition - 1) + " Has Drawn a Card!")
            return output

    def draw(deck, hand):
            card = random.choice(deck)
            UNOcard.removeCard(deck, card)
            hand.append(card)
            return hand

    def cpuSetWildCard(cpuHand, card):
        red = 0
        blue = 0
        green = 0
        yellow = 0
        highest = 0
        list = []

        #counts the highest amount of colors in hand.
        for cards in range(0, len(cpuHand)):
            
            if ((UNOcard.getColor(cpuHand[cards]) == ug.RED)):
                red += 1
            elif ((UNOcard.getColor(cpuHand[cards]) == ug.BLUE)):
                blue += 1
            elif ((UNOcard.getColor(cpuHand[cards]) == ug.GREEN)):
                green += 1
            elif ((UNOcard.getColor(cpuHand[cards]) == ug.YELLOW)):
                yellow += 1
            else:
                red += 1
                blue += 1
                green += 1
                yellow += 1
        
 
        list.append(red)
        list.append(blue)
        list.append(green)
        list.append(yellow)
        for var in range(0,4):
            if (list[var] > highest):
                 color = (var + 1)

        print("The Computer has set the color to " + ug.cardColor[color] + "!")
        if(UNOcard.getSpecial(card) == ug.WILD):
            card = UNOcard(color, ug.WILD, None, "small/" + str(color) + "_w.png")
            return card
        elif(UNOcard.getSpecial(card) == ug.WILD4):
            card = UNOcard(color, ug.WILD4, None, ("small/" + str(color) + "_w4.png"))
            return card            

    def setCenterCard(deck):
        card = random.choice(deck)
        if(UNOcard.getColor(card) != None):
            UNOcard.removeCard(deck, card)
            return card
        else:
           return UNOlogic.setCenterCard(deck)
    
    def displayCenter(card):
        print("Current Card: ")
        #If the color is nothing. Display Special form Dictionary
        if (UNOcard.getColor(card) == None):
            print (ug.cardSpecials[UNOcard.getSpecial(card)])

        #if value is nothing. Display color form Dictionary + Special from Dictionary
        elif (UNOcard.getSpecial(card) > ug.GENERAL ):
            print (ug.cardColor[UNOcard.getColor(card)] + " " +  ug.cardSpecials[UNOcard.getSpecial(card)])
                
        #otherwise, display Color form Dictionary + Number
        else:
            print (ug.cardColor[UNOcard.getColor(card)] + " " + str(UNOcard.getValue(card)))
    
    def displayCard(card):
        print("The Computer has played a: ")
        #If the color is nothing. Display Special form Dictionary
        if (UNOcard.getColor(card) == None):
            print (ug.cardSpecials[UNOcard.getSpecial(card) + "\n"])

        #if value is nothing. Display color form Dictionary + Special from Dictionary
        elif (UNOcard.getSpecial(card) > ug.GENERAL):
            print (ug.cardColor[UNOcard.getColor(card)] + " " +  ug.cardSpecials[UNOcard.getSpecial(card)] + "\n")
                
        #otherwise, display Color form Dictionary + Number
        else:
            print (ug.cardColor[UNOcard.getColor(card)] + " " + str(UNOcard.getValue(card)) + "\n")
    
    def isInteger(input):
        try:
            int(input)
            return True
        except:
            return False

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
        
         
