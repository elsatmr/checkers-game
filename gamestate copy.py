def check_move(self):
    if self.capture_move != []:
        if self.is_equal_capture_move:
            return True
    else:
        if self.is_equal_valid_move:
            return True

def check_double_capture(self):
    self.capture_move.clear()
    self.search_valid_move()
    self.has_capture_move()
    self.valid_move.clear()
    if self.capture_move != []:
        self.current_state = "DOUBLE_CAPTURE"


def moving_piece(self, x, y):
    row, col = self.click_index(x, y)
    self.current_move.end = [row, col]
    if self.check_move:
        self.update_grid()
        self.is_king(row, col)
        self.valid_move.clear
    if self.capture_move != []:
        self.check_double_capture()
    
    return self.current_player, self.current_move.capture, self.current_move.start, self.current_move.end, self.squares[row][col].king




