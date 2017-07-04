import random
import math
import itertools
import logging
import click

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

LOWER_BOUND_HOUSE_LOCATION = 1
UPPER_BOUND_HOUSE_LOCATION = 2
NUMBER_OF_RANCHES = 4

class Ranch:
    def __init(self):
        logging.info("Making a ranch.")
        self.house_location = None

    def build_house(self):
        rand1 = random.uniform(LOWER_BOUND_HOUSE_LOCATION,
                               UPPER_BOUND_HOUSE_LOCATION)
        rand2 = random.uniform(LOWER_BOUND_HOUSE_LOCATION,
                               UPPER_BOUND_HOUSE_LOCATION)
        self.house_location = rand1, rand2
        logging.info("Built a house for %s at %s", self, self.house_location)

    @staticmethod
    def make_ranch():
        ranch = Ranch()
        ranch.build_house()
        return ranch

    def __str__(self):
        return "Ranch object: house at: {}".format(self.house_location)

class RanchGrid:
    position_map = {
            'top_left': (0, 0),
            'top_right': (0, 1),
            'bottom_right': (1, 1),
            'bottom_left': (1, 0)
            }
    positions = ('top-left', 'top-right', 'bottom-right', 'bottom-left')

    def __init__(self, ranches):
        assert len(ranches) == NUMBER_OF_RANCHES
        midpoint = NUMBER_OF_RANCHES // 2
        self.grid = [ranches[0:midpoint],
                     ranches[midpoint:NUMBER_OF_RANCHES]]

    def getranch(self, pos):
        indices = self.position_map[pos]
        return self.grid[indices[0]][indices[1]]

    def get_polygon(self):
        top_left = self.getranch('top_left').house_location
        top_right = self.getranch('top_right').house_location
        bottom_left = self.getranch('bottom_left').house_location
        bottom_right = self.getranch('bottom_right').house_location

        top_left = top_left[0], top_left[1] + 1
        top_right = top_right[0] + 1, top_right[1] + 1
        bottom_right = bottom_right[0] + 1, bottom_right[1]

        return top_left, top_right, bottom_right, bottom_left

    def __str__(self):
        polygon = self.get_polygon()
        return 'RanchGrid:\n' + '\n'.join(p + str(polygon[i]) for i, p in enumerate(self.positions))

@click.command()
@click.option('--plot', 'is_plotting', default=False, is_flag=True)
@click.option('--num', 'num_simulations', default=100)
@click.option('--is_saving', default=False, is_flag = True)
@click.option('--verbose', default=False, is_flag = True)
def main(is_plotting=False, num_simulations=100, is_saving=False, verbose=False):
    '''Program entry point --- mile-high view of program execution.'''
    if verbose:
        logging.basicConfig(level=logging.INFO)

    concave_polygon_count = 0
    for i in range(0, num_simulations):
        convex = simulate(is_plotting, is_saving)
        if not convex:
            concave_polygon_count += 1

    print("In {} simulations, found {} occurences of concave polgons.".format(num_simulations,
                                                                              concave_polygon_count))
    print("Estimated likelihood that the children can travel in whatever" +
            " straight line they please within their allowed area: {}".format(
                (num_simulations - concave_polygon_count) / num_simulations))


def simulate(is_plotting, is_saving):
    '''Runs a single simulation of the problem.

    Returns True if the kids can walk in any straight line.
    '''
    ranches = [Ranch.make_ranch() for _ in range(0, NUMBER_OF_RANCHES)]
    grid = RanchGrid(ranches)
    polygon = grid.get_polygon()

    if is_plotting:
        plot_polygon(polygon, is_saving)

    convex = is_convex(polygon)

    if not convex:
        logging.info("Found a grid with non-convex quadrilateral: {}".format(grid))
    return convex


def plot_polygon(polygon, is_saving):
    '''Useful for plotting the polygon during testing.'''
    if is_saving:
        # a small hack to keep the state of # of saved imgs to avoid filename collision
        try:
            getattr(plot_polygon, 'img_saved_count')
            plot_polygon.img_saved_count += 1
        except AttributeError:
            setattr(plot_polygon, 'img_saved_count', 1)

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

    if is_saving:
        fig.savefig('plot{}.png'.format(plot_polygon.img_saved_count))


def is_convex(polygon):
    '''Given a polygon, which is just a tuple of (x,y) catesian points, return if it is convex.

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

    for i in range(0, len(polygon)):
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
            logging.info("Found a cross product that isn't turning left: p1: {}, p2: {}, p3: {}".format(
                p1, p2, p3))
            return False

    logging.info("Walking the polygon, all turns seemed to be to the right, indicating convexity.")
    return True


if __name__ == '__main__':
    main()
