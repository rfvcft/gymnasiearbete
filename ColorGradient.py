import numpy as n
from matplotlib import pyplot as plt
import time

startTime = time.time()
N = 50
r = 0.2
s = (1 / 338)


# TODO: Fixa så att man inte behöver evaluera över alla punkter om de är i rätt distans.
# TODO: Lägg till så att man kan ta bort överlappande maximum

def point_eval(distance, radius):
    # returns a number (score)
    score = radius - distance
    return score


def distance_to_point(my_point, eval_point):
    # returns a number (distance)
    distance = ((eval_point[0] - my_point[0]) ** 2 + (eval_point[1] - my_point[1]) ** 2) ** 0.5
    return distance


class GridEvaluator:
    def __init__(self, radius, number_of_points, grid_size, random_seed=None):
        self.radius = radius
        self.number_of_points = number_of_points
        self.grid_size = grid_size
        self.random_seed = random_seed

    def create_random_points(self):
        # creates a list of 2D points of length number_of_points
        points = []

        if self.random_seed:
            n.random.seed(self.random_seed)

        for z in range(self.number_of_points):
            random_point = n.random.random(2)
            points.append([random_point[0], random_point[1]])

        return points

    def eval_my_point(self, my_point, all_points, radius):
        # returns a number (sum of all scores)
        # TODO: lägg till så att man kan få ut points_in_distance

        points_in_distance = []
        evaluation = 0
        for point in all_points:
            distance = distance_to_point(my_point, point)
            if distance < radius:
                points_in_distance.append(point)
                evaluation += point_eval(distance, radius)
        return evaluation

    def evaluate_over_grid(self, points_to_evaluate, step_size, radius):
        width = self.grid_size[0]
        height = self.grid_size[1]
        start_x = step_size / 2
        y = step_size / 2
        list_of_evaluations = []

        while y <= height:
            row_evaluations = []
            x = start_x
            while x <= width:
                evaluation = self.eval_my_point((x, y), points_to_evaluate, radius)
                row_evaluations.append(evaluation)
                x += step_size
            list_of_evaluations.append(row_evaluations)
            y += step_size

        return list_of_evaluations


evaluator = GridEvaluator(r, N, (1, 1), random_seed=92069)
randomPoints = evaluator.create_random_points()
data = evaluator.evaluate_over_grid(randomPoints, s, r)

# figure
fig, ax1 = plt.subplots()


# labels
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('step size %s' % s)

# c sequence
c = ax1.pcolormesh(data, cmap='hot')

plt.axis('equal')

print(time.time() - startTime)
print(r)
cbar = plt.colorbar(c, ax=ax1)
plt.show()
