# --- Part Two ---
# Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

import sys
from day_07_1 import Circuit

def main():
    circuit = Circuit()
    file = open(sys.argv[1], 'r')
    for line in [l.rstrip("\n") for l in file]:
        circuit.add_instruction(line)

    a_signal = circuit.get_signal('a')

    circuit.add_instruction(str(a_signal) + ' -> ' + 'b')
    circuit.print_all_signals()

if __name__ == "__main__":
    main()