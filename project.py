'''
Elsa Tamara
CS 5001 - Fall 2020
Project Milestone 1
'''
from gamestate import GameState
from drawboard import DrawBoard
import turtle

NUM_SQUARES = 8
SQUARE = 50
SQUARE_COLORS = ("light gray", "white")

CIRCLE_COLORS = ("black", "red")
NUM_CIRCLES = 3
CIRCLE = 25

game = GameState()
pen = turtle.Turtle()
board = DrawBoard()

def click_handler(x, y):
    if game.current_state == "BLACK_TURN":
        game.select_black_piece(x, y)
    elif game.current_state == "BLACK_MOVING":
        old_row, old_col, new_row, new_col = game.moving_black_piece(x, y)
        old_y = (old_row / 8) * 400
        old_x = (old_col / 8) * 400
        pen.color("black", SQUARE_COLORS[0])
        pen.setposition(-200 + old_x, -200 + old_y)
        board.draw_square(SQUARE)
        pen.home()

        new_y = (new_row / 8) * 400
        new_x = (new_col / 8) * 400
        pen.setposition(-175 + new_x, -200 + new_y)
        pen.color("black", CIRCLE_COLORS[0])
        board.draw_circle(CIRCLE)
    elif game.current_state == "RED_TURN":
        game.select_red_piece(x, y)
    elif game.current_state == "RED_MOVING":
        game.moving_red_piece(x, y)



def main():
    board_size = NUM_SQUARES * SQUARE
    window_size = board_size + SQUARE

    turtle.setup(window_size, window_size)
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")
    turtle.tracer(0, 0)

    pen.penup()
    pen.hideturtle()

    pen.color("black", "white")

    

    #Step 1 - Draw the board outline
    corner = -board_size / 2
    pen.setposition(corner, corner)
    board.draw_square(board_size)

    #Step 2 - Draw the squares
    pen.color("black", SQUARE_COLORS[0])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.setposition(corner + SQUARE * col, corner + SQUARE * row)
                board.draw_square(SQUARE)
    
    #Step 3 - Draw black circle pieces
    pen.color("black", CIRCLE_COLORS[0])
    start_black_circle = corner + CIRCLE
    for col in range(NUM_SQUARES):
        for row in range(NUM_CIRCLES):
            if col % 2 != row % 2:
                pen.setposition(start_black_circle + SQUARE * col, corner + SQUARE * row)
                board.draw_circle(CIRCLE)

    #Step 3 - Draw red circle pieces
    pen.color("black", CIRCLE_COLORS[1])
    start_red_circle = -corner - (3 * SQUARE)
    for col in range(NUM_SQUARES):
        for row in range(NUM_CIRCLES):
            if col % 2 == row % 2:
                pen.setposition(start_black_circle + SQUARE * col, start_red_circle + SQUARE * row)
                board.draw_circle(CIRCLE)
    

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler)

    # Click click
    
    
    

    turtle.done()


if __name__ == "__main__":
    main()