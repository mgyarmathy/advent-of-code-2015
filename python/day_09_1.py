# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

import sys
from collections import defaultdict
from itertools import permutations

def main():
    routeSolver = RouteSolver()
    file = open(sys.argv[1], 'r')
    for line in file:
        line = line.strip()
        [origin, to, destination, equals, distance] = line.split(' ')
        routeSolver.add_distance(origin, destination, int(distance))

    shortest_route = routeSolver.get_shortest_route()

    print "Route: " + str(shortest_route["route"])
    print "Distance: " + str(shortest_route["distance"])

class RouteSolver:
    distances = None

    def __init__(self):
        self.distances = defaultdict(dict)

    def add_distance(self, origin, destination, distance):
        self.distances[origin][destination] = distance
        self.distances[destination][origin] = distance

    def get_route_distance(self, route):
        if len(route) < 2:
            return 0
        return sum(self.distances[route[i]][route[i+1]] for i in range(len(route) - 1))

    def get_shortest_route(self):
        # BRUTE FORCE
        routes = [ {"distance": self.get_route_distance(route), "route": list(route)} for route in permutations(self.distances.keys())]
        return min(routes, key=lambda x: x['distance'])

    def get_longest_route(self):
        # BRUTE FORCE
        routes = [ {"distance": self.get_route_distance(route), "route": list(route)} for route in permutations(self.distances.keys())]
        return max(routes, key=lambda x: x['distance'])

    def print_distances(self):
        for origin in self.distances.keys():
            for destination in self.distances[key].keys():
                print "%s to %s = %i" % (origin, destination, self.distances[origin][destination])

if __name__ == '__main__':
    main()