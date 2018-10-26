#Devin Patel
#6/26/2017
#Word Search

import random
import GameBoardPiece

directions =  [[1, 0], [0, 1], [1, 1]]

class WordSearch:
    def __init__(self, board_size, file: open):
        self.numRows = board_size;
        self.numColumns = board_size;
        self.board = [[GameBoardPiece.GameBoardPiece() for i in range(self.numColumns)] for j in range(self.numRows)]
        self.words = []
        print("Initializing")
        self._populate_board(file, board_size)
        self.found_words = set()
        print("Done")
                
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


    def _is_game_over(self) -> bool:
        return len(self.words) == len(self.found_words)
    
    def _populate_board(self, file : open, board_size):
        for line in file:
            okay = False
            data = line.strip().upper()
            data = ''.join([i for i in data if i.isalpha()])
            print(data)
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
                                print(self.board[temp_x][temp_y].letter, char)
                                okay = True
                            else:
                                okay = False
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

    def make_move(self, row1,col1,row2,col2) -> bool:
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
        startx = row1
        starty = col1
        if(reachable):
            for j in range(count):
                word += self.board[startx][starty].letter
                startx += direction[0]
                starty += direction[1]
        for w in self.words:
            if w == word:
                for j in range(count):
                    self.board[row1][col1].color = '#42f456'
                    row1 += direction[0]
                    col1 += direction[1]
                self.found_words.add(w)
                return True
        return False

if __name__ == '__main__':
    game = WordSearch(15, open('fruits.txt'))
