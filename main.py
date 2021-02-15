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
            capacity_remaining = popped_glass.capacity - popped_glass.water
            overflow = max(0.0, popped_glass_water - capacity_remaining)
            popped_glass.water += popped_glass_water - overflow
            print(popped_glass.water)

            if overflow > 0:
                child_left, child_right = popped_glass.return_children()

                assert child_left and child_right, f"child_left: {child_left}, child_right: {child_right}"

                split_overflow = overflow / 2

                queue.append((child_left, split_overflow))
                queue.append((child_right, split_overflow))


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

        self.connect_children(left_or_right)
        return new_child

    def connect_children(self, left_or_right):

        if 'left' in left_or_right:
            parent_glass = self.parent_left
        elif 'right' in left_or_right:
            parent_glass = self.parent_right

        if not parent_glass:
            return None

        if 'left' in left_or_right:
            child_to_connect = parent_glass.child_left
        elif 'right' in left_or_right:
            child_to_connect = parent_glass.child_right

        if not child_to_connect:
            child_to_connect = parent_glass.create_child('left')

        if 'left' in left_or_right:
            child_to_connect.child_right = self.child_left
            self.child_left.parent_left = child_to_connect
        elif 'right' in left_or_right:
            child_to_connect.child_left = self.child_right
            self.child_right.parent_right = child_to_connect

class TreeSearch:

    def __init__(self, i: int, j: int, water: float):
        self.row = i
        self.col = j
        self.water = water
        self.root = Glass()

    def find_glass(self):
        first_steps = self.col
        second_steps = self.row - self.col


        glass = self.root
        while second_steps > 0:
            glass = glass.child_left
            if not glass:
                return 0
            second_steps -= 1

        while first_steps > 0:
            glass = glass.child_right
            if not glass:
                return 0
            first_steps -= 1

        return glass.water


if __name__ == "__main__":

    test_values = [[0, 0, 0], [1, 1, 0], [1, 1, 2], [3, 2, 4]]
    expected_outputs = [0, 0, 0.250, 0.250]

    for index, test_value in enumerate(test_values):

        i = test_value[0]
        j = test_value[1]
        water = test_value[2]

        tree = TreeSearch(i, j, water)
        water_level = tree.find_glass()

        try:
            assert water_level == expected_outputs[index], f"The water level was {water_level} when it should have been {expected_outputs[index]}"

        except AssertionError as error:
            print(error)




