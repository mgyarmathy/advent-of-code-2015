# For example:

# 1 becomes 11 (1 copy of digit 1).
# 11 becomes 21 (2 copies of digit 1).
# 21 becomes 1211 (one 2 followed by one 1).
# 1211 becomes 111221 (one 1, one 2, and two 1s).
# 111221 becomes 312211 (three 1s, two 2s, and one 1).

from day_10_x import encode, decode
import unittest

class Day10Tests(unittest.TestCase):
    def test_encode(self):
        self.assertEquals(encode('1'), '11')
        self.assertEquals(encode('11'), '21')
        self.assertEquals(encode('21'), '1211')
        self.assertEquals(encode('1211'), '111221')
        self.assertEquals(encode('111221'), '312211')
    
    def test_decode(self):
        self.assertEquals(decode('11'), '1')
        self.assertEquals(decode('21'), '11')
        self.assertEquals(decode('1211'), '21')
        self.assertEquals(decode('111221'), '1211')
        self.assertEquals(decode('312211'), '111221')

if __name__ == '__main__':
    unittest.main()