from UNOcard import UNOcard



class UNOdisplay:

    def draw_hand_visble(playerHand, centerCard, screen):
        for cards in range(0,len(playerHand)):
            screen.blit(UNOcard.getImage(playerHand[cards]), (100 * cards, 500))
        screen.blit(UNOcard.getImage(centerCard), (600, 500))









