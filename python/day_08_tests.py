# For example:

# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

# For example:

# "" encodes to "\"\"", an increase from 2 characters to 6.
# "abc" encodes to "\"abc\"", an increase from 5 characters to 9.
# "aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
# "\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.

from day_08_1 import code_length, memory_length
from day_08_2 import encode_string
import unittest

class Day8Tests(unittest.TestCase):
    def test_code_length(self):
        self.assertEquals(code_length(r'""'), 2)
        self.assertEquals(code_length(r'"abc"'), 5)
        self.assertEquals(code_length(r'"aaa\"aaa"'), 10)
        self.assertEquals(code_length(r'"\x27"'), 6)
    
    def test_memory_length(self):
        self.assertEquals(memory_length(r'""'), 0)
        self.assertEquals(memory_length(r'"abc"'), 3)
        self.assertEquals(memory_length(r'"aaa\"aaa"'), 7)
        self.assertEquals(memory_length(r'"\x27"'), 1)

    def test_encode_string(self):
        self.assertEquals(encode_string(r'""'), r'"\"\""')
        self.assertEquals(encode_string(r'"abc"'), r'"\"abc\""')
        self.assertEquals(encode_string(r'"aaa\"aaa"'), r'"\"aaa\\\"aaa\""')
        self.assertEquals(encode_string(r'"\x27"'), r'"\"\\x27\""')


if __name__ == "__main__":
    unittest.main()