from gamestate import GameState

class Bla:
    def __init__(self):
        self.lst = [[1, 2], [3, 4]]

    def prnt(self):
        move_col = 0
        move_row = 0
        for row, lst in enumerate(self.lst):
            for col, elem in enumerate(lst):
                if row == 0 and col == 1:
                    move_col = elem + 2
                    move_row = elem + 1
                    
        return move_col, move_row, elem

    def has_capture_move(self):
        for obj in self.valid_move:
            if obj.capture == True:
                   return True
        return False

    
    def remove_non_capture_move(self):
        if self.has_capture_move():
            idx_lst = []
            for obj in self.valid_move:
                if obj.capture == True:
                    idx_lst.append(obj)
            self.valid_move.clear()
            for obj in idx_lst:
                self.valid_move.append(idx_lst)
            print(self.valid_move)
            print(self.valid_move[0].start)

def main():
    #lst = [[0, 0], [0, 0]]
    #lst[0] = [1, -1]
    #lst[1] = [1, 1]
    #lst.append([-2], [-3])
    #print(lst)

    game = GameState.valid_move


if __name__ == "__main__":
    main()