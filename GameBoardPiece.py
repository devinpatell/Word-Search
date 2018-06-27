#Devin Patel
#6/26/2018
#word search project

import random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class GameBoardPiece:
    def __init__(self):
            self.letter = ALPHABET[((int)(26 * random.random()))]
            self.part_of_word = False
            self.color = '#000000'
