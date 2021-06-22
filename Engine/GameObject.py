class GameObject:
    def __init__(self, x, y, sx, sy, r):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.r = r
    def __repr__(self):
        return f"x : {self.x}, y : {self.y}, scale(x) : {self.sx}, scale(y) : {self.sy}, rotation : {self.r}"