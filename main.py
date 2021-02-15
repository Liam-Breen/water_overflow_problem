from collections import deque

class Glass:

    def __init__(self):

        self.child_left = None
        self.child_right = None

        self.parent_left = None
        self.parent_right = None

        self.capacity = 0.250
        self.water = 0

    def fill(self,water: float):
        queue = deque()
        queue.append((self, water))

        while len(queue) > 0:
            popped_glass, popped_glass_water = queue.popleft()
            capacity_remaining = self.capacity - self.water
            overflow = max(0, popped_glass_water - capacity_remaining)
            self.water += water - overflow

            if overflow > 0:

                child_left, child_right = self.return_children()
                assert child_left and child_right, f"child_left: {child_left}, child_right: {child_right}"


    def return_children(self):

        if self.child_left and self.child_right:
            return [self.child_left, self.child_right]

        elif self.child_left and not self.child_right:
            return self.child_left, self.create_child('right')

        elif not self.child_left and self.child_right:
            return self.create_child('left'), self.child_right

        elif not self.child_left and not self.child_right:
            return self.create_child('left'), self.create_child('right')

    def create_child(self, left_or_right):
        new_child = Glass()

        if 'left' in left_or_right:
            new_child.parent_right = self
            self.child_left = new_child

        elif 'right' in left_or_right:
            new_child.parent_left = self
            self.child_right = new_child

        return new_child





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

    glass = Glass()
    glass.fill(1)

    # test_values = [[0, 0, 0], [1, 1, 0], [1, 1, 2], [3, 2, 4]]
    # expected_outputs = [0, 0, 0.250, 0.250]

    # for index, test_value in enumerate(test_values):

    #     i = test_values[0]
    #     j = test_values[1]
    #     water = test_values[2]

    #     tree = TreeSearch(i, j, water)
    #     water_level = tree.find_glass()

    #     try:
    #         assert water_level == expected_outputs[index], f"The water level was {water_level} when it should have been {expected_outputs[index]}"

    #     except AssertionError as error:
    #         print(error)




