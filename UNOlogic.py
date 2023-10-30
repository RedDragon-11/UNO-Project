from UNOcard import UNOcard
import UNOGlobals as ug
import random

#TODO rework the playableCard Function with the reminder that cardColors NONE isn't real
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
    def play(deck, centerCard, playerHand, cpuHand):
        userInput = (input("Which Card would you like to play?(must be a number or 'draw')\n"))



        if (UNOlogic.isInteger(userInput) == False):
            if (userInput.lower() == "draw"):
                output = [None, UNOlogic.draw(deck, playerHand)]
                return output
            else:
                print("Check Spelling of draw.")
                output = UNOlogic.play(deck, centerCard, playerHand, cpuHand)
                return output

        elif(int(userInput) <= len(playerHand)):
            if (UNOlogic.playableCard(centerCard, playerHand[int(userInput) - 1]) == True):
                if(UNOcard.getSpecial(playerHand[int(userInput) - 1]) == ug.WILD or UNOcard.getSpecial(playerHand[int(userInput) - 1]) == ug.WILD4):
                    card = UNOlogic.playerSetWildCard()
                    playerHand = playerHand.remove(card)
                    output = [card, playerHand]
                    return output
                centerCard = playerHand[int(userInput)-1]
                playerHand.remove(playerHand[int(userInput) - 1])
                output = [centerCard, playerHand]
                return output

        else:
            print("Please only input Valid Integers.")
            output = UNOlogic.play(deck, centerCard, playerHand, cpuHand)
            return output
    
    def cpuPlay(deck, centerCard, cpuHand, playerHand):
        drawCard = True
        for cards in range(0, len(cpuHand)):
            if(UNOlogic.playableCard(centerCard, cpuHand[cards]) == True):
                drawCard = False
                #if the card selected is a wildcard
                if(UNOcard.getColor(cpuHand[cards]) == None):
                    card = UNOlogic.cpuSetWildCard()
                    output = [card, cpuHand]
                    return output
                elif(UNOcard.getSpecial(cpuHand[cards]) == ug.SKIP):
                    UNOlogic.cpuPlay(deck, centerCard, cpuHand, playerHand)
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

    def cpuSetWildCard():
        randomColor = random.randint(1,4)
        print("The Computer has sent the color to " + ug.cardColor[randomColor] + "!")
        card = UNOcard(randomColor, None, None)
        return card

    def playerSetWildCard():
        userInput = input("Which color? 1. Red 2. Blue 3. Green 4. Yellow")
        if(int(userInput) <= 4 and int(userInput) != 0):
            print("You have sent the color to " + ug.cardColor[int(userInput)])
            card = UNOcard(int(userInput), ug.WILD, None)
            return card

    def setCenterCard(deck):
        card = random.choice(deck)
        UNOcard.removeCard(deck, card)
        return card
    
    def displayCenter(card):
        print("Current Card: ")
        #If the color is nothing. Display Special form Dictionary
        if (UNOcard.getColor(card) == None):
            print (ug.cardSpecials[UNOcard.getSpecial(card)])

        #if value is nothing. Display color form Dictionary + Special from Dictionary
        elif (UNOcard.getSpecial(card) > ug.GENERAL):
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


        
         
