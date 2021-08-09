import turtle
from gamestate import GameState

pen = turtle.Turtle()
game = GameState()

NUM_SQUARES = 8
SQUARE = 50
SQUARE_COLORS = ("light gray", "white")

CIRCLE_COLORS = ("black", "red")
NUM_CIRCLES = 3
CIRCLE = 25

class DrawBoard:
    def __init__(self):
        self.create_board()
        self.create_window()

        turtle.bgcolor("white")
        turtle.tracer(0, 0)

        pen.penup()
        pen.hideturtle()

        self.draw_outline()
        self.draw_checkers_square()
        self.draw_black_pieces()
        self.draw_red_pieces()

        self.click()

        turtle.done()


    def draw_square(self, size):
        RIGHT_ANGLE = 90
        pen.begin_fill()
        pen.pendown()
        for i in range(4):
            pen.forward(size)
            pen.left(RIGHT_ANGLE)
        pen.end_fill()
        pen.penup()

    
    def draw_circle(self, radius):
        '''
            Function -- draw_circle
                Draw a circle with a given radius.
            Parameters:
                a_turtle -- an instance of Turtle
                size -- the radius of the circle
            Returns:
                Nothing. Draws a circle in the graphics window.
        '''
        pen.begin_fill()
        pen.pendown()
        pen.circle(radius)
        pen.end_fill()
        pen.penup()
    
    def calc_board_size(self):
        board_size = NUM_SQUARES * SQUARE
        return board_size

    def define_corner(self):
        board_size = self.calc_board_size()
        corner = -board_size / 2
        return corner

    def create_board(self):
        board_size = self.calc_board_size()
        turtle.screensize(board_size, board_size)
            

    def create_window(self):
        board_size = self.calc_board_size()
        window_size = board_size + SQUARE
        turtle.setup(window_size, window_size)

    
    def draw_outline(self):
        corner = self.define_corner()
        board_size = self.calc_board_size()
        pen.setposition(corner, corner)
        pen.color("black", SQUARE_COLORS[1])
        self.draw_square(board_size)

    
    def draw_checkers_square(self):
        corner = self.define_corner()
        pen.color("black", SQUARE_COLORS[0])
        for col in range(NUM_SQUARES):
            for row in range(NUM_SQUARES):
                if col % 2 != row % 2:
                    pen.setposition(corner + SQUARE * col, corner + SQUARE * row)
                    self.draw_square(SQUARE)

    
    def draw_black_pieces(self):
        corner = self.define_corner()
        pen.color("black", CIRCLE_COLORS[0])
        start_black_circle = corner + CIRCLE
        for col in range(NUM_SQUARES):
            for row in range(NUM_CIRCLES):
                if col % 2 != row % 2:
                    pen.setposition(start_black_circle + SQUARE * col, corner + SQUARE * row)
                    self.draw_circle(CIRCLE)


    def draw_red_pieces(self):
        corner = self.define_corner()
        pen.color("black", CIRCLE_COLORS[1])
        start_red_circle = -corner - (3 * SQUARE)
        start_black_circle = corner + CIRCLE
        for col in range(NUM_SQUARES):
            for row in range(NUM_CIRCLES):
                if col % 2 == row % 2:
                    pen.setposition(start_black_circle + SQUARE * col, start_red_circle + SQUARE * row)
                    self.draw_circle(CIRCLE)

    
    def click(self):
        screen = turtle.Screen()
        screen.onclick(self.click_handler)
    

    def set_pen_color(self, player):
        if player == "BLACK":
            return CIRCLE_COLORS[0]
        else:
            return CIRCLE_COLORS[1]

    
    def set_position(self, idx):
        start_y = (idx[0] / NUM_SQUARES) * (NUM_SQUARES * SQUARE)
        start_x = (idx[1] / NUM_SQUARES) * (NUM_SQUARES * SQUARE)
        return start_y, start_x

    
    def col_left_or_right(self, start_idx, end_idx):
        if end_idx[1] > start_idx[1]:
            return "right"
        else:
            return "left"

    
    def row_up_or_down(self, start_idx, end_idx):
        if end_idx[0] > start_idx[0]:
            return "up"
        else:
            return "down"

    
    def draw_board_square(self, start_idx):
        start_y, start_x = self.set_position(start_idx)
        pen.color("black", SQUARE_COLORS[0])
        pen.setposition(-200 + start_x, -200 + start_y)
        self.draw_square(SQUARE)
        pen.home()

    
    def circle_piece(self, end_idx, player):
        start_y, start_x = self.set_position(end_idx)
        pen.setposition(-175 + start_x, -200 + start_y)
        pen.color("black", self.set_pen_color(player))
        self.draw_circle(CIRCLE)


    def mark_king(self, end_idx):
        pen.begin_fill()
        start_y, start_x = self.set_position(end_idx)
        pen.setposition(-175 + start_x, -195 + start_y)
        pen.color("white", "pink")
        pen.pendown()
        pen.circle(20)
        pen.end_fill()
        pen.penup()


    def draw_capture_pieces(self, player, capture, start_idx, end_idx, king):
        self.draw_board_square(start_idx)
        if self.col_left_or_right(start_idx, end_idx) == "left":
            start_idx[1] -= 1
        else:
            start_idx[1] += 1
        
        if self.row_up_or_down(start_idx, end_idx) == "down":
            start_idx[0] -= 1
        else:
            start_idx[0] += 1

        self.draw_board_square(start_idx)
        self.circle_piece(end_idx, player)
        if king == True:
            self.mark_king(end_idx)


    def draw_moving_pieces(self, player, capture, start_idx, end_idx, king):
        if capture == False:
            self.draw_board_square(start_idx)
            self.circle_piece(end_idx, player)
            if king == True:
                self.mark_king(end_idx)
        else:
            self.draw_capture_pieces(player, capture, start_idx, end_idx, king)


    def draw_ai_move(self):
        game.ai_move()
        player = "RED"
        capture = game.current_move.capture
        start_idx = game.current_move.start
        end_idx = game.current_move.end
        king = game.squares[end_idx[0]][end_idx[1]].king
        self.draw_moving_pieces(player, capture, start_idx, end_idx, king)
        if game.current_move.capture:
            game.check_ai_double_capture()
            if game.capture_move != []:
                game.process_ai_double_capture()
                capture = game.current_move.capture
                start_idx = game.current_move.start
                end_idx = game.current_move.end
                king = game.squares[end_idx[0]][end_idx[1]].king
                self.draw_moving_pieces(player, capture, start_idx, end_idx, king)


    def click_handler(self, x, y):
        if game.current_player == "BLACK":
            if game.current_state == "SELECT_A_PIECE":
                game.select_piece(x, y)
            elif game.current_state == "MOVING_A_PIECE":
                player = game.current_player
                game.moving_piece(x, y)
                if game.piece_is_moving == True:              
                    capture = game.current_move.capture
                    start_idx = game.current_move.start
                    end_idx = game.current_move.end
                    king = game.squares[end_idx[0]][end_idx[1]].king
                    self.draw_moving_pieces(player, capture, start_idx, end_idx, king)
                    if game.current_player == "RED":
                        self.draw_ai_move()
                        game.current_player = game.change_player()
            elif game.current_state == "DOUBLE_CAPTURE":
                player = game.current_player
                game.process_double_capture(x, y)
                if game.piece_is_moving == True:
                    capture = game.double_capture.capture
                    start_idx = game.double_capture.start
                    end_idx = game.double_capture.end
                    king = game.squares[end_idx[0]][end_idx[1]].king
                    self.draw_moving_pieces(player, capture, start_idx, end_idx, king)
                    if game.current_player == "RED":
                        self.draw_ai_move()
                        game.current_player = game.change_player()
                    game.current_state = "SELECT_A_PIECE"
                    

                



                
                    
            