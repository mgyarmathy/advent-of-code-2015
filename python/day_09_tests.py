# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

from day_09_1 import RouteSolver
import unittest

class RouteSolverTests(unittest.TestCase):
    def setUp(self):
        self.routeSolver = RouteSolver()
        self.routeSolver.add_distance("London", "Dublin", 464)
        self.routeSolver.add_distance("London", "Belfast", 518)
        self.routeSolver.add_distance("Dublin", "Belfast", 141)

    def test_get_route_distance(self):
        self.assertEquals(self.routeSolver.get_route_distance(["Dublin", "London", "Belfast"]), 982)

    def test_get_shortest_route(self):
        shortest_route = self.routeSolver.get_shortest_route()
        self.assertEquals(shortest_route["distance"], 605)
        self.assertEquals(shortest_route["route"], ["London", "Dublin", "Belfast"])

    def test_get_longest_route(self):
        longest_route = self.routeSolver.get_longest_route()
        self.assertEquals(longest_route["distance"], 982)
        self.assertEquals(longest_route["route"], ["Dublin", "London", "Belfast"])

if __name__ == "__main__":
    unittest.main()