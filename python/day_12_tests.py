# Part 1

# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.

# Part 2

# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

from day_12_1 import sum_json_numbers_regex
from day_12_2 import filter_red_json_from_string
import unittest
import json

class Day12Tests(unittest.TestCase):
    def test_sum_json_numbers_regex(self):
        self.assertEquals(sum_json_numbers_regex('[1,2,3]'), 6)
        self.assertEquals(sum_json_numbers_regex('{"a":2,"b":4}'), 6)
        self.assertEquals(sum_json_numbers_regex('[[[3]]]'), 3)
        self.assertEquals(sum_json_numbers_regex('{"a":{"b":4},"c":-1}'), 3)
        self.assertEquals(sum_json_numbers_regex('{"a":[-1,1]}'), 0)
        self.assertEquals(sum_json_numbers_regex('[-1,{"a":1}]'), 0)
        self.assertEquals(sum_json_numbers_regex('[]'), 0)
        self.assertEquals(sum_json_numbers_regex('{}'), 0)

    def test_filter_red_json_from_string(self):
        self.assertEquals(filter_red_json_from_string('[1,2,3]'), '[1,2,3]')
        self.assertEquals(filter_red_json_from_string('[1,{"c":"red","b":2},3]'), '[1,{},3]')
        self.assertEquals(filter_red_json_from_string('{"d":"red","e":[1,2,3,4],"f":5}'), '{}')
        self.assertEquals(filter_red_json_from_string('[1,"red",5]'), '[1,"red",5]')

if __name__ == '__main__':
    unittest.main()