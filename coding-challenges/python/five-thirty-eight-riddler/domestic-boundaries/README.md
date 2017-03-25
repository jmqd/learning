# FiveThirtyEight Riddler Problem

[https://fivethirtyeight.com/features/can-you-find-the-honest-prince/](https://fivethirtyeight.com/features/can-you-find-the-honest-prince/)

## the problem

### From Stephen Carrier, a puzzle about domestic boundaries:

Consider four square-shaped ranches, arranged in a two-by-two pattern, as if part of a larger checkerboard. One family lives on each ranch, and each family builds a small house independently at a random place within the property. Later, as the families in adjacent quadrants become acquainted, they construct straight-line paths between the houses that go across the boundaries between the ranches, four in total. These paths form a quadrilateral circuit path connecting all four houses. This circuit path is also the boundary of the area where the families’ children are allowed to roam.

What is the probability that the children are able to travel in a straight line from any allowed place to any other allowed place without leaving the boundaries? (In other words, what is the probability that the quadrilateral is convex?)

# the solution

_Simulated by solution.py script._

### General strategy of simulation:

- Uniformly at random generate a point within each quadrant.
- Starting from the "top left", moving clockwise, traverse the points, applying a numerical `orientation test` to check if the polygon formed from the four points is convex or not.
- Repeat this process N times and compute the observed frequency of convex polygons.

More about the numerical geometry algorithms here: https://www.cs.cmu.edu/~quake/robust.html


## Results

- In 10,000,000 simulations, found 906320 occurences of concave polgons.
- Estimated/observed probability: 0.909368

## Animated gif of 100 simulations

![100 simulations of ranch polygons][plots]

[plots]: plots.gif "Animated Gif of Ranch Playground Polygon Simulations"

## usage of solution.py

`python3 solution.py [--num --plot --is_saving]`
- `--num` defaults to `100`
