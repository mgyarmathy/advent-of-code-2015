# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).

# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

from day_11_1 import increment_password, is_valid_password, next_valid_password
import unittest

class Day11Tests(unittest.TestCase):
    def test_increment_password(self):
        self.assertEquals(increment_password('a'), 'b')
        self.assertEquals(increment_password('z'), 'aa')
        self.assertEquals(increment_password('aa'), 'ab')
        self.assertEquals(increment_password('az'), 'ba')
    
    def test_is_valid_password(self):
        self.assertFalse(is_valid_password('hijklmmn'))
        self.assertFalse(is_valid_password('abbceffg'))
        self.assertFalse(is_valid_password('abbcegjk'))
        self.assertTrue(is_valid_password('abcdffaa'))
        self.assertTrue(is_valid_password('ghjaabcc'))

    def test_next_valid_password(self):
        self.assertEquals(next_valid_password('abcdefgh'), 'abcdffaa')
        self.assertEquals(next_valid_password('ghijklmn'), 'ghjaabcc')

if __name__ == '__main__':
    unittest.main()