
import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
      if num_balls >= len(self.contents):
        all_balls = self.contents.copy()
        self.contents.clear()  # remove all balls
        return all_balls
      drawn_balls = random.sample(self.contents, num_balls)
      for ball in drawn_balls:
        self.contents.remove(ball)
      return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Copy the original hat
        trial_hat = copy.deepcopy(hat)
        drawn = trial_hat.draw(num_balls_drawn)

        # Count the drawn balls
        drawn_counts = {}
        for color in drawn:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1

        # Check if drawn balls meet expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(probability)