class Piece:
    def __init__(self, color):
        self.color = color
        self.direction = [[0, 0], [0, 0]]
        self.set_direction()
        self.king = False
        #self.set_king_direction()

    def __str__(self):
        return self.color
    
    def __repr__(self):
        return self.color

    def set_direction(self):
        if self.color == "BLACK":
            self.direction[0] = [1, -1]
            self.direction[1] = [1, 1]
        elif self.color == "RED":
            self.direction[0] = [-1, -1]
            self.direction[1] = [-1, 1]


    def king_direction(self):
        if self.king == True:
            if self.color == "BLACK":
                self.direction.append([-1, -1])
                self.direction.append([-1, 1])
            elif self.color == "RED":
                self.direction.append([1, -1])
                self.direction.append([1, 1])

        