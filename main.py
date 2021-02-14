class Glass:

    def __init__(self,):

        self.child_left = None
        self.child_right = None

        self.capacity = 0.250
        self.water = 0

class TreeSearch:

    def __init__(self, i, j, water):
        self.row = i
        self.col = j
        self.water = water
        self.root = Glass()
