class music():
    def __init__(self, s, last_coord):
        self.last_coord = last_coord
        self.s = s
    def Shagi(self, coord):
        self.x, self.y = coord
        if (self.x - self.last_coord[0] != 0) or (self.y - self.last_coord[1] != 0):
            self.s.play()
        else:
            self.s.stop()
        self.last_coord = [self.x, self.y]





