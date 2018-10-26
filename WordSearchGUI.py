# Devin Patel
# 9/21/2017
# word search gui

import tkinter
import WordSearch
import sys

DEFAULT_FONT = ('Helvetica', 12)
class WordSearchGUI:
    def __init__(self):
        self._game = WordSearch.WordSearch(12, open('fruits.txt'))
        self._root_window = tkinter.Tk()
        self._root_window.minsize(400, 445)
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 400, height = 445,
            background = '#ffffff')

        self._canvas.grid(
            row = 0, column = 0, padx = 0, pady = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._word_bank_text = tkinter.StringVar()
        self._update_word_bank_text()
        self._label2 = tkinter.Label(master = self._root_window, textvariable=self._word_bank_text, font=DEFAULT_FONT)
        self._label2.grid(
            row = 0, column = 1, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._display_text = tkinter.StringVar()
        self._update_display_text()
        self._label1 = tkinter.Label(master = self._root_window,
                                    textvariable=self._display_text,
                                     font=DEFAULT_FONT)
        self._label1.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 0)
        self.first_move = []

    def start(self) -> None:
        self._root_window.mainloop()

    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Whenever the Canvas' size changes, redraw the othello game,'''
        self._redraw()

    def _update_display_text(self):
        '''updates how many words are left to find'''
        temp_num_words_left = (len(self._game.words) - len(self._game.found_words))
        if(temp_num_words_left == 1):
            self._display_text.set("{} word left".format(temp_num_words_left))
        else:
            self._display_text.set("{} words left".format(temp_num_words_left))
    def _update_word_bank_text(self):
        pass

    
    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''performs an wordSearch move when the canvas is clicked.'''
        if not self._game._is_game_over:
            canvas_width = self._canvas.winfo_width()
            canvas_height = self._canvas.winfo_height()

            rows = self._game.numRows
            columns = self._game.numColumns

            cell_width = canvas_width // columns
            cell_height = canvas_height // rows


            col = event.x // cell_width
            row = event.y // cell_height

            worked = False
            if(self.first_move):
                worked = self._game.make_move(self.first_move[0], self.first_move[1], row, col)
                self.first_move = []
            else:
                self.first_move.append(row)
                self.first_move.append(col)

            print(self._game.found_words)
            self._redraw()

    def _redraw(self) -> None:
        '''redraws the entire Othello game and updates appropriate text labels.'''
        self._canvas.delete(tkinter.ALL)

        self._update_display_text()
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        self._canvas.create_rectangle(0, 0, canvas_width, canvas_height,
                                      outline='black')

        rows = self._game.numRows
        columns = self._game.numColumns

        cell_width = canvas_width // columns
        cell_height = canvas_height // rows

        for i in range(rows):
            self._canvas.create_line(0, (i * cell_height),
                                     canvas_width,(i * cell_height),
                                     fill = '#9eabbf', width = 2)
        for i in range(columns):
            self._canvas.create_line((i * cell_width), 0,
                                     (i * cell_width), canvas_height,
                                     fill = '#9eabbf', width = 2)


        board = self._game.get_game_board()
        for r, row in enumerate(board):
            for c, piece in enumerate(row):
                y = r * cell_height
                x = c * cell_width
                self._canvas.create_text(x + cell_width / 2.0, y + cell_height / 2.0, font=DEFAULT_FONT,activefill='blue', fill=piece.color, anchor=tkinter.W, width=100, text= piece.letter)

        self._canvas.update()


if __name__ == '__main__':
    WordSearchGUI().start()
