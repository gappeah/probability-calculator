import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents += [key] * value
        print(self.contents)

    def draw(self, number):
        if number >= len(self.contents):
            return self.contents

        drawn_balls = random.sample(self.contents, number)
        for ball in drawn_balls:
            self.contents.remove(ball)

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        colours_gotten = hat_copy.draw(num_balls_drawn)
        expected_copy = copy.deepcopy(expected_balls)  # Corrected method name

        for colour in colours_gotten:
            if colour in expected_copy:
                expected_copy[colour] -= 1
        if all(x <= 0 for x in expected_copy.values()):
            count += 1
    probability = count / num_experiments
    return probability