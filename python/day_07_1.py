# --- Day 7: Some Assembly Required ---
# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

import sys

def main():
    circuit = Circuit()
    file = open(sys.argv[1], 'r')
    for line in [l.rstrip("\n") for l in file]:
        circuit.add_instruction(line)

    circuit.print_all_signals()

class Circuit:
    wires = None
    memo = None

    def __init__(self):
        self.wires = dict()
        self.memo = dict()

    def add_instruction(self, instruction):
        value, wire = instruction.split(' -> ')
        self.add_wire(wire, value)

    def add_wire(self, wire, value):
        self.wires[wire] = value
        self.memo.clear()

    def get_signal(self, wire):
        # return memoized value if it has already been computed
        if wire in self.memo:
            return self.memo[wire]

        signal = None

        if wire in self.wires:
            value = self.wires[wire]

            if value.isdigit():
                signal = int(value)
            elif 'AND' in value:
                left, right = value.split(' AND ')
                if left.isdigit():
                    left_signal = int(left)
                else:
                    left_signal = self.get_signal(left)
                if right.isdigit():
                    right_signal = int(right)
                else:
                    right_signal = self.get_signal(right)
                if left_signal is not None and right_signal is not None:
                    signal = (left_signal & right_signal)
            elif 'OR' in value:
                left, right = value.split(' OR ')
                if left.isdigit():
                    left_signal = int(left)
                else:
                    left_signal = self.get_signal(left)
                if right.isdigit():
                    right_signal = int(right)
                else:
                    right_signal = self.get_signal(right)
                if left_signal is not None and right_signal is not None:
                    signal = (left_signal | right_signal)
            elif 'LSHIFT' in value:
                left, lshift = value.split(' LSHIFT ')
                if left.isdigit():
                    left_signal = int(left)
                else:
                    left_signal = self.get_signal(left)
                if left_signal is not None and lshift.isdigit():
                    signal = left_signal << int(lshift)
            elif 'RSHIFT' in value:
                left, rshift = value.split(' RSHIFT ')
                if left.isdigit():
                    left_signal = int(left)
                else:
                    left_signal = self.get_signal(left)
                if left_signal is not None and rshift.isdigit():
                    signal = left_signal >> int(rshift)
            elif 'NOT' in value:
                _, right = value.split('NOT ')
                if right.isdigit():
                    right_signal = int(right)
                else:
                    right_signal = self.get_signal(right)
                if right_signal is not None:
                    signal = ~right_signal
            else:
                signal = self.get_signal(value)

            if signal is not None:
                signal = signal % 65536

        # cache value for future references
        self.memo[wire] = signal
        return signal

    def print_all_signals(self):
        for wire in sorted(self.wires.keys()):
            print wire + ': ' + str(self.get_signal(wire))

    def print_all_connections(self):
        for wire in self.wires.keys():
            print self.wires[wire] + ' -> ' + wire

if __name__ == "__main__":
    main()