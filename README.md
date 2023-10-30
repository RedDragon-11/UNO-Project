# UNO-Porject
This is a simple project that I took on to help teach me some OOP with python 
Its not going to be perfect and could probably be done in a more effectient manner but this project is one of my first full projects with Python!
As a warning, some cards might not function properly (i.e. Draws and Skips). I am currently still working on it and they should be implimented soon.

####-----How to RUN------####
1. Make sure you have Python installed (pretty sure it must be at least Python 3)
2. Right Click main.py and open with Python
3. Enjoy my simplistic little 1v1 Uno Project!

####-----KNOWN ISSUES------####
1. If the first card set as Center is a wild card, playing any card will crash the game
2. To put it lightly... Skips and Reverses just do no function yet. When the player plays a Skip or Reverse, nothing happens and the CPU carrys on as normal but when the cpu plays a skip, it skips the player INDEFINITELY. For now, skips will be commented out.
3. deckReset() Function is dumb and cant see that a card is in the deck variable when it actually is. Causing a crash since it starts complaining that the card it needs to remove isn't there. 
4. Wild Draw 4's don't make the person draw 4 cards. This is most likely because it uses newCenter, which when a wild is played makes the new card a normal wild card instead of a +4
