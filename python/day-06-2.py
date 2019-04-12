#!/usr/bin/python
from enum import Enum
import sys
import re

class Lights:
    rows = 0
    columns = 0
    lights = None

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.lights = rows * columns * [0]

    def apply_instruction(self, instr):
        start_x = instr.from_coords[0]
        start_y = instr.from_coords[1]
        end_x = instr.to_coords[0]
        end_y = instr.to_coords[1]

        num_rows = end_x - start_x + 1
        num_cols = end_y - start_y + 1

        for idx in range(num_rows):
            idxA = ((idx + start_x) * self.columns) + start_y
            idxB = idxA + num_cols
            if instr.action == LightInstructionAction.ON:
                self.lights[idxA:idxB] = [brightness + 1 for brightness in self.lights[idxA:idxB]]
            elif instr.action == LightInstructionAction.OFF:
                self.lights[idxA:idxB] = [max(brightness - 1, 0) for brightness in self.lights[idxA:idxB]]
            elif instr.action == LightInstructionAction.TOGGLE:
                self.lights[idxA:idxB] = [brightness + 2 for brightness in self.lights[idxA:idxB]]
            else:
                pass

    def total_brightness(self):
        return sum(self.lights)

    def __str__(self):
        return '\n'.join([''.join(self.lights[row*self.columns:((row+1)*self.columns)]) for row in range(self.rows)])

class LightInstruction:
    action = None
    from_coords = None
    to_coords = None

    def __init__(self, instruction):
        self.action, self.from_coords, self.to_coords = self.parse_instruction(instruction)

    def parse_instruction(self, instruction):
        tokens = re.findall('(turn on|turn off|toggle|\d+,\d+)', instruction)

        if tokens[0] == 'turn on':
            action = LightInstructionAction.ON
        elif tokens[0] == 'turn off':
            action = LightInstructionAction.OFF
        elif tokens[0] == 'toggle':
            action = LightInstructionAction.TOGGLE
        else:
            action = None

        from_coords = tuple([int(i) for i in tokens[1].split(',')])
        to_coords = tuple([int(i) for i in tokens[2].split(',')])

        return (action, from_coords, to_coords)

    def __str__(self):
        return str(self.action) + ' ' + str(self.from_coords) + ' - ' + str(self.to_coords)

class LightInstructionAction(Enum):
    ON = 1
    OFF = 2
    TOGGLE = 3

def main():
    run_tests()

    lights = Lights(1000, 1000)
    file = open(sys.argv[1], 'r')
    instructions = [LightInstruction(line) for line in file]

    for instr in instructions:
        lights.apply_instruction(instr)

    print 'total brightness: ' + str(lights.total_brightness())

def run_tests():
    lights = Lights(5, 5)
    assert lights.total_brightness() == 0

    # 00000
    # 00000
    # 00000
    # 00000
    # 00000

    toggleInstruction = LightInstruction('toggle 0,0 through 1,4')
    assert toggleInstruction.action == LightInstructionAction.TOGGLE
    assert toggleInstruction.from_coords == (0,0)
    assert toggleInstruction.to_coords == (1,4)
    lights.apply_instruction(toggleInstruction)
    assert lights.total_brightness() == 20

    # 00000    22222
    # 00000    22222
    # 00000 -> 00000
    # 00000    00000
    # 00000    00000

    onInstruction = LightInstruction('turn on 3,0 through 3,4')
    assert onInstruction.action == LightInstructionAction.ON
    assert onInstruction.from_coords == (3,0)
    assert onInstruction.to_coords == (3,4)
    lights.apply_instruction(onInstruction)
    assert lights.total_brightness() == 25

    # 22222    22222
    # 22222    22222
    # 00000 -> 00000
    # 00000    11111
    # 00000    00000

    offInstruction = LightInstruction('turn off 0,2 through 1,4')
    assert offInstruction.action == LightInstructionAction.OFF
    assert offInstruction.from_coords == (0,2)
    assert offInstruction.to_coords == (1,4)
    lights.apply_instruction(offInstruction)
    assert lights.total_brightness() == 19

    # 22222    22111
    # 22222    22111
    # 00000 -> 00000
    # 11111    11111
    # 00000    00000

    toggleInstruction = LightInstruction('toggle 0,0 through 4,0')
    assert toggleInstruction.action == LightInstructionAction.TOGGLE
    assert toggleInstruction.from_coords == (0,0)
    assert toggleInstruction.to_coords == (4,0)
    lights.apply_instruction(toggleInstruction)
    assert lights.total_brightness() == 29

    # 22111    42111
    # 22111    42111
    # 00000 -> 20000
    # 11111    31111
    # 00000    20000

if __name__ == "__main__":
    main()
