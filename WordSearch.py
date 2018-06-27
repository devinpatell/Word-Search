#Devin Patel
#6/26/2017
#Word Search

import random
import GameBoardPiece
directions =  [[1, 0], [0, 1], [1, 1],  [-1, -1], [-1, 1], [1, -1], [-1, 0], [0, -1]]

class WordSearch:
    def __init__(self, board_size, file: open):
        self.numRows = board_size;
        self.numColumns = board_size;
        self.board = [[GameBoardPiece.GameBoardPiece() for i in range(self.numColumns)] for j in range(self.numRows)]
        #self._print_board()
        self.words = []
        self._populate_board(file, board_size)
        self._print_board()
        self.found_words = []
        


        
    def _print_board(self):
        print("\n")
        for i, row in enumerate(self.board):
            column = ""
            for j, col in enumerate(row):        
                if j != len(row) - 1:
                    column = column + col.letter + " | "
                else:
                    column = column + col.letter
            print(column)
            if i != len(self.board) - 1:
                divider = "__|_" * len(row)
                print(divider[:-2])
        print("\n")
        
    def _populate_board(self, file : open, board_size):
        for line in file:
            okay = False
            data = line.rstrip().upper()
            self.words.append(data)
            while(not okay):
                start_x = ((int)(board_size * random.random()))
                start_y = ((int)(board_size * random.random()))
                temp_x = start_x
                temp_y = start_y
                direction = directions[(int)((len(directions) * random.random()))]
                if(len(data) <= board_size):
                    if((start_x + (direction[0] * len(data)) in range(board_size)) and (start_y + (direction[1] * len(data)) in range(board_size))):
                        for char in data:  
                            if(self.board[temp_x][temp_y].part_of_word == False or ( self.board[temp_x][temp_y].part_of_word == True and self.board[temp_x][temp_y].letter == char)):
                                okay = True
                            else:
                                break
                            temp_x += direction[0]
                            temp_y += direction[1]
                        if(okay):
                            for char in data:
                                self.board[start_x][start_y].letter = char
                                self.board[start_x][start_y].part_of_word = True
                                start_x += direction[0]
                                start_y += direction[1]
    
    def get_game_board(self) -> [[GameBoardPiece.GameBoardPiece]]:
        return self.board

    def make_move(self, row1,col1,row2,col2):
        print(row1,col1,row2,col2)
        direction = []
        if(row1 == row2):
            direction.append(0)
        elif(row1 < row2):
            direction.append(1)
        else:
            direction.append(-1)
            
        if(col1 == col2):
            direction.append(0)
        elif(col1 < col2):
            direction.append(1)
        else:
            direction.append(-1)
        print(direction)
        print()
        reachable = False
        startx = row1
        starty = col1
        count = 1
        for i in range(self.numRows):
            if(startx == row2 and starty == col2):
                reachable = True
                break
            startx += direction[0]
            starty += direction[1]
            count += 1
        word = ""
        if(reachable):
            for j in range(count):
                word += self.board[row1][col1].letter
                row1 += direction[0]
                col1 += direction[1]
        print(reachable)
        print(word)
        for w in self.words:
            if word == w:
                self.found_words.append(w)
        

if __name__ == '__main__':
    game = WordSearch(15, open('fruits.txt'))
