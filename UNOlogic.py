from UNOcard import UNOcard
import UNOGlobals as ug
import random

#TODO rework the playableCard Function with the reminder that cardColors NONE isn't real
class UNOlogic:
    
    def playableCard(centerCard, playedCard):
        if(UNOcard.getColor(centerCard) == UNOcard.getColor(playedCard)):
            print("Color pass")
            return True
        elif(UNOcard.getValue(centerCard) != None or UNOcard.getValue(playedCard) != None):
            if(UNOcard.getValue(centerCard) == UNOcard.getValue(playedCard)):
                    print("Value pass")
                    return True
        elif(UNOcard.getSpecial(centerCard) != ug.GENERAL or UNOcard.getSpecial(playedCard) != ug.GENERAL):
            if(UNOcard.getSpecial(centerCard) == UNOcard.getSpecial(playedCard)):
                print("Special Pass")
                return True
        elif(UNOcard.getSpecial(playedCard) == ug.WILD or UNOcard.getSpecial(playedCard) == ug.WILD4):
            print("Wild Pass")
            return True
        
    def drawStartingHand(deck):
        hand = []
        for val in range(0,7):
                card = random.choice(deck)
                UNOcard.removeCard(deck, card)
                hand.append(card)
        return hand

        
         
