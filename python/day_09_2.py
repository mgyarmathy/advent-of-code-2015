# --- Part Two ---
# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# What is the distance of the longest route?

from day_09_1 import RouteSolver
import sys

def main():
    routeSolver = RouteSolver()
    file = open(sys.argv[1], 'r')
    for line in file:
        line = line.strip()
        [origin, to, destination, equals, distance] = line.split(' ')
        routeSolver.add_distance(origin, destination, int(distance))

    longest_route = routeSolver.get_longest_route()

    print "Route: " + str(longest_route["route"])
    print "Distance: " + str(longest_route["distance"])

if __name__ == '__main__':
    main()