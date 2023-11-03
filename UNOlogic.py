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
    
    def cpuPlay(deck, centerCard, cpuHand):
        drawCard = True
        for cards in range(0, len(cpuHand)):
            if(UNOlogic.playableCard(centerCard, cpuHand[cards]) == True):
                drawCard = False
                #if the card selected is a wildcard
                if(UNOcard.getColor(cpuHand[cards]) == None):
                    card = UNOlogic.cpuSetWildCard(cpuHand[cards])
                    removeCard = cpuHand[cards]
                    cpuHand.remove(removeCard)
                    output = [card, cpuHand]
                    return output
                centerCard = cpuHand[cards]
                cpuHand.remove(cpuHand[cards])
                output = [centerCard, cpuHand]
                UNOlogic.displayCard(centerCard)
                return output
    
        if(drawCard == True):
            output = [None, UNOlogic.draw(deck, cpuHand)]
            print("The Computer Has Drawn a Card!\n")
            return output

    def draw(deck, hand):
            card = random.choice(deck)
            UNOcard.removeCard(deck, card)
            hand.append(card)
            return hand

    def cpuSetWildCard(card):
        randomColor = random.randint(1,4)
        print("The Computer has set the color to " + ug.cardColor[randomColor] + "!")
        if(UNOcard.getSpecial(card) == ug.WILD):
            card = UNOcard(randomColor, ug.WILD, None, "small/" + str(randomColor) + "_w.png")
            return card
        elif(UNOcard.getSpecial(card) == ug.WILD4):
            card = UNOcard(randomColor, ug.WILD4, None, ("small/" + str(randomColor) + "_w4.png"))
            return card            

   # def playerSetWildCard(card):



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
        
         
