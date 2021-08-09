'''
Elsa Tamara
CS 5001 - Fall 2020

A game state class
'''

SELECT_A_PIECE = "SELECT_A_PIECE"
MOVING_A_PIECE = "MOVING_A_PIECE"

RANDOM_INDEX = 0
BLACK = "BLACK"
RED = "RED"
EMPTY = "EMPTY"

from move import Move

from piece import Piece



class GameState:
    '''
        Class -- GameState
            Represents the game state.
        Attributes:
    '''

    def __init__(self):
        self.squares =\
            [[EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK")],
            [Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY],
            [EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK"), EMPTY, Piece("BLACK")],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
            [Piece("RED"), EMPTY, Piece("RED"), EMPTY, Piece("RED"), EMPTY, Piece("RED"), EMPTY],
            [EMPTY, Piece("RED"), EMPTY, Piece("RED"), EMPTY, Piece("RED"), EMPTY, Piece("RED")],
            [Piece("RED"), EMPTY, Piece("RED"), EMPTY, Piece("RED"), EMPTY, Piece("RED"), EMPTY]]
        self.current_player = "BLACK"
        self.current_state = SELECT_A_PIECE
        
        self.valid_move = []
        self.capture_move = []
        self.current_move = Move(None, None, None)
        self.double_capture = Move(None, None, None)

        self.valid_start_piece = False
        self.piece_is_moving = False


    def get_square_x_index(self, x):
        BASE_X_COORDINATE = -200 # x coordinate when the index is 0
        DIVISOR = 50 #size of the square
        x_index = int((BASE_X_COORDINATE - x) // - DIVISOR)
        return x_index

    
    def get_square_y_index(self, y):
        BASE_Y_COORDINATE = -200 # y coordinate when the index is 0
        DIVISOR = 50 #size of the square
        y_index = int((BASE_Y_COORDINATE - y) // - DIVISOR)
        return y_index


    def click_index(self, x, y):
        col = self.get_square_x_index(x)
        row = self.get_square_y_index(y)
        return row, col

    
    def search_valid_move(self):
        print("SEARCHING FOR", self.current_player, self.valid_move)
        for row, lst in enumerate(self.squares):
            for col, elem in enumerate(lst):
                if elem != EMPTY:
                    if elem.color == self.current_player:
                        for lstt in elem.direction:
                            move_row = row + lstt[0]
                            move_col = col + lstt[1]
                            if self.check_negative_row_col(move_row, move_col):
                                if self.squares[move_row][move_col] == EMPTY:
                                    self.valid_move.append(Move([row, col], [move_row, move_col], False))
                                elif self.squares[move_row][move_col].color != self.current_player:
                                    move_row += lstt[0]
                                    move_col += lstt[1]
                                    if self.check_negative_row_col(move_row, move_col):
                                        if self.squares[move_row][move_col] == EMPTY:
                                            self.valid_move.append(Move([row, col], [move_row, move_col], True))
        print(self.valid_move)


    def check_negative_row_col(self, move_row, move_col):
        if move_row <= 7 and move_row >= 0 and move_col <= 7 and move_col >= 0:
            return True


    def has_capture_move(self):
        for obj in self.valid_move:
            if obj.capture == True:
                self.capture_move.append(Move(obj.start, obj.end, obj.capture))

    
    def is_equal_valid_move(self):
        for obj in self.valid_move:
            if self.current_move.__eq__(obj):
                self.current_move.capture = obj.capture
                return True
        return False


    def is_equal_capture_move(self):
        for obj in self.capture_move:
            if self.current_move.__eq__(obj):
                self.current_move.capture = obj.capture
                return True
        return False

    
    def is_equal_double_capture(self):
        for obj in self.capture_move:
            if self.double_capture.__eq__(obj):
                self.double_capture.capture = obj.capture
                return True
        return False


    def change_player(self):
        if self.current_player == "BLACK":
            return "RED"
        else:
            return "BLACK"


    def check_move(self):
        if self.capture_move != []:
            self.is_equal_capture_move()
            if self.is_equal_capture_move():
                return True
        elif self.capture_move == []:
            self.is_equal_valid_move()
            if self.is_equal_valid_move():
                return True
        return False

    def check_double_capture(self):
        self.capture_move *= 0
        self.search_valid_move()
        self.has_capture_move()
        self.valid_move *= 0
        if self.capture_move != []:
            self.current_state = "DOUBLE_CAPTURE"
            self.double_capture.start = self.current_move.end
        else:
            print("The code changes state else checkdoublecapt")
            self.current_player = self.change_player()
            self.current_state = SELECT_A_PIECE
    

    def process_double_capture(self, x, y):
        self.piece_is_moving = False
        row, col = self.click_index(x, y)
        self.double_capture.end = [row, col]
        self.is_equal_double_capture()
        if self.is_equal_double_capture() == True:
            self.current_move.start = self.double_capture.start
            self.current_move.end = self.double_capture.end
            self.update_grid()
            self.is_king(row, col)
            self.valid_move *= 0
            self.capture_move *= 0
            self.piece_is_moving = True
            #self.current_state = MOVING_A_PIECE
            print("Game current state is during double capt is ", self.current_state)
            self.current_player = self.change_player()
            print("Game current PLAYER is during double capt is ", self.current_player)


    def is_king(self, row, col):
        if row == 7 and self.squares[row][col].color == "BLACK":
                self.squares[row][col].king = True
                self.squares[row][col].direction.append([-1, -1])
                self.squares[row][col].direction.append([-1, 1])
        elif row == 0 and self.squares[row][col].color == "RED":
                self.squares[row][col].king = True
                self.squares[row][col].direction.append([1, -1])
                self.squares[row][col].direction.append([1, 1])


    def update_grid(self):
        if self.current_move.capture == True:
            self.squares[self.current_move.end[0]][self.current_move.end[1]] = self.squares[self.current_move.start[0]][self.current_move.start[1]]
            move_row_idx = self.find_enemy_row_idx()
            move_col_idx = int((self.current_move.end[1] + self.current_move.start[1]) / 2)
            self.squares[move_row_idx][move_col_idx] = EMPTY
            self.squares[self.current_move.start[0]][self.current_move.start[1]] = EMPTY 
        else:
            self.squares[self.current_move.end[0]][self.current_move.end[1]] = self.squares[self.current_move.start[0]][self.current_move.start[1]]
            self.squares[self.current_move.start[0]][self.current_move.start[1]] = EMPTY


    def find_enemy_row_idx(self):
        if self.current_move.end[0] > self.current_move.start[0]:
            move_row_idx = self.current_move.start[0] + 1
        else:
            move_row_idx = self.current_move.start[0] - 1
        return move_row_idx


    def select_piece(self, x, y):
        self.piece_is_moving = False
        row, col = self.click_index(x, y)
        self.current_move.start = [row, col]
        if self.squares[row][col] != EMPTY and self.squares[row][col].color == self.current_player:
            self.search_valid_move()
            self.has_capture_move()
            self.current_state = MOVING_A_PIECE


    def moving_piece(self, x, y):
        row, col = self.click_index(x, y)
        self.current_move.end = [row, col]
        self.check_move()
        if self.check_move() == True:
            self.piece_is_moving = True
            self.update_grid()
            self.is_king(row, col)
            self.valid_move *= 0
            if self.capture_move != []:
                self.check_double_capture()                
            else:
                self.current_player = self.change_player()
                print("The code changes state first else movingpiece")
                self.current_state = SELECT_A_PIECE
        else:
            print("The code changes state second else movingpiece")
            self.current_state = SELECT_A_PIECE
    
    
    def ai_move(self):
        self.search_valid_move()
        self.has_capture_move()
        if self.capture_move == []:
            self.current_move.start = self.valid_move[0].start
            self.current_move.end = self.valid_move[0].end
            self.current_move.capture = False
        else:
            self.current_move.start = self.capture_move[0].start
            self.current_move.end = self.capture_move[0].end
            self.current_move.capture = True
        self.update_grid()
        self.is_king(self.current_move.end[0], self.current_move.end[1])
        self.valid_move *= 0

    
    def check_ai_double_capture(self):
        self.capture_move *= 0
        self.search_valid_move()
        self.has_capture_move()


    def process_ai_double_capture(self):
        self.current_move.start = self.current_move.end
        self.current_move.end = self.capture_move[0].end
        self.update_grid()
        self.is_king(self.current_move.end[0], self.current_move.end[1])
        self.valid_move *= 0
        self.capture_move *= 0





        

    

        





        