class Move:
    def __init__(self, start, end, capture):
        self.start = start
        self.end = end
        self.capture = capture
        
    
    def __repr__(self):
        return str(self.start) + str(self.end) + str(self.capture)
        

    
    #def __str__(self):
    #    return "Start: " + self.start + "End: " + self.end + "Capture: " + self.capture

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

        #print("Move is" + str(self.start) + str(self.end) + "and capture is" + str(self.capture))

        #game.valid_move.append(start, end)
        #self.valid_move = []
        #self.capture_move = []

    #def set_capt_move(self):


    