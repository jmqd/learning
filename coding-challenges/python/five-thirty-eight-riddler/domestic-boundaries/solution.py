import random
import math
import itertools
import logging
import matplotlib.pyplot as plt
import numpy as np
import click
from matplotlib.collections import PatchCollection

logging.basicConfig(level=logging.INFO)

class Ranch:
    def __init(self):
        logging.info("Making a ranch.")
        self.house_location = None

    def build_house(self):
        self.house_location = random.uniform(1, 2), random.uniform(1, 2)
        logging.info("Built a house for %s at %s", self, self.house_location)

    @staticmethod
    def make_ranch():
        ranch = Ranch()
        ranch.build_house()
        return ranch

    def __str__(self):
        return "Ranch object: house at: {}".format(self.house_location)

class RanchGrid:
    def __init__(self, ranches):
        assert len(ranches) == 4

        self.grid = [ranches[0:2], ranches[2:4]]

    def get_polygon(self):
        top_left = self.grid[0][0].house_location
        top_right = self.grid[0][1].house_location
        bottom_left = self.grid[1][0].house_location
        bottom_right = self.grid[1][1].house_location

        top_left = top_left[0], top_left[1] + 1
        top_right = top_right[0] + 1, top_right[1] + 1
        bottom_right = bottom_right[0] + 1, bottom_right[1]

        return top_left, top_right, bottom_right, bottom_left

    def __str__(self):
        positions = ('top-left', 'top-right', 'bottom-right', 'bottom-left')
        polygon = self.get_polygon()
        message = ''
        for i, p in enumerate(positions):
            message += p
            message += str(polygon[i])
            message += '\n'
        return "RanchGrid:\n{}".format(message)

@click.command()
@click.option('--plot', 'is_plotting', default=False, is_flag=True)
@click.option('--num', 'num_simulations', default=100)
def main(is_plotting=False, num_simulations=100):
    concave_polygon_count = 0
    for i in range(0, num_simulations):
        result = simulate(is_plotting)
        if result:
            concave_polygon_count += 1

        print(i, result)

    print("In {} simulations, found {} occurences of concave polgons.".format(num_simulations,
                                                                              concave_polygon_count))
    print("Estimated probability that the kids can walk from any given point in the field" +
            " to any other point in a straight line, legally: {}".format(
                (num_simulations - concave_polygon_count) / num_simulations))


def simulate(is_plotting):
    '''Runs a single simulation of the problem.'''
    ranches = [Ranch.make_ranch() for _ in range(0, 4)]
    grid = RanchGrid(ranches)
    polygon = grid.get_polygon()

    if is_plotting:
        plot_polygon(polygon)

    concavity = is_concave(polygon)
    return concavity


def plot_polygon(polygon):
    '''Useful for plotting the polygon during testing.'''
    data = np.array(polygon)
    polygon_plot = plt.Polygon(data)

    patches = []
    fig, ax = plt.subplots()

    xmin = 1
    xmax = 3
    ymin = 1
    ymax = 3

    axes = plt.gca()
    axes.set_xlim([xmin,xmax])
    axes.set_ylim([ymin,ymax])

    patches.append(polygon_plot)

    p = PatchCollection(patches)
    ax.add_collection(p)
    plt.show()


def is_concave(polygon):
    '''Given a polygon, which is just a tuple of (x,y) catesian points, return if it is concave.

    Notes:
        This algorihm solves the problem of determining concavity in a clever way:

        - Observe that as you traverse a convex polygon in a clock-wise motion,
        that each next step will "rotate to the right". You can imagine a polarized
        plane that is tangential to the slope of the "current side", and check to see
        if the next clockwise point in the polygon exists to the right of that plane
        using a cross product function. If it exists to the right, it is still convex.
        Otherwise, we can say that the polygon is concave.

    For more information on this family of algorthms, you can visit this page:
    https://www.cs.cmu.edu/~quake/robust.html
    '''
    points = itertools.cycle(polygon)

    for i in range(0, 4):
        p1, p2, p3 = next(points), next(points), next(points)
        x, y = p1
        x2, y2 = p2
        x3, y3 = p3

        dx1 = x2 - x
        dy1 = y2 - y

        dx2 = x3 - x2
        dy2 = y3 - y2

        cross_product = dx1 * dy2 - dy1 * dx2

        logging.info("cross product is %s", cross_product)

        is_turning_left = cross_product >= 0

        if is_turning_left:
            return True

    return False


if __name__ == '__main__':
    main()
