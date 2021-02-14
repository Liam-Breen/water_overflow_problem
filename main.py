class Glass:

    def __init__(self,):

        self.child_left = None
        self.child_right = None

        self.capacity = 0.250
        self.water = 0

    def fill(self, water: float):
        ...

class TreeSearch:

    def __init__(self, i: int, j: int, water: float):
        self.row = i
        self.col = j
        self.water = water
        self.root = Glass()

    def find_glass(self):
        ...
        # return glass


if __name__ == "__main__":

    test_values = [[0, 0, 0], [1, 1, 0], [1, 1, 2], [3, 2, 4]]
    expected_outputs = [0, 0, 0.250, 0.250]

    for index, test_value in enumerate(test_values):

        i = test_values[0]
        j = test_values[1]
        water = test_values[2]

        tree = TreeSearch(i, j, water)
        water_level = tree.find_glass()

        try:
            assert water_level == expected_outputs[index], f"The water level was {water_level} when it should have been {expected_outputs[index]}"

        except AssertionError as error:
            print(error)




