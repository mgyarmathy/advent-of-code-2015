import unittest
from day_07_1 import Circuit

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

class CircuitTest(unittest.TestCase):
    def runTest(self):
        circuit = Circuit()
        circuit.add_instruction('123 -> x')
        circuit.add_instruction('456 -> y')
        circuit.add_instruction('x AND y -> d')
        circuit.add_instruction('x OR y -> e')
        circuit.add_instruction('x LSHIFT 2 -> f')
        circuit.add_instruction('y RSHIFT 2 -> g')
        circuit.add_instruction('NOT x -> h')
        circuit.add_instruction('NOT y -> i')
        circuit.add_instruction('i -> j')
        self.assertEqual(circuit.get_signal('d'), 72)
        self.assertEqual(circuit.get_signal('e'), 507)
        self.assertEqual(circuit.get_signal('f'), 492)
        self.assertEqual(circuit.get_signal('g'), 114)
        self.assertEqual(circuit.get_signal('h'), 65412)
        self.assertEqual(circuit.get_signal('i'), 65079)
        self.assertEqual(circuit.get_signal('j'), 65079)
        self.assertEqual(circuit.get_signal('x'), 123)
        self.assertEqual(circuit.get_signal('y'), 456)
        self.assertEqual(circuit.get_signal('a'), None)

if __name__ == "__main__":
    unittest.main()