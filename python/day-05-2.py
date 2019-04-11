#!/usr/bin/python
import sys

def main():
    assert is_nice_string('qjhvhtzxzqqjkmpb') == True
    assert is_nice_string('xxyxx') == True
    assert is_nice_string('aaaaaaaaa') == True
    assert is_nice_string('uurcxstgmygtbstg') == False
    assert is_nice_string('ieodomkazucvgmuy') == False

    file = open(sys.argv[1], 'r')
    count = 0
    for line in file:
        if is_nice_string(line):
            count += 1
    print count

def is_nice_string(string):
    has_non_overlapping_pairs = False
    has_repeat_letter = False
    pairs = dict()
    for idx in range(len(string)-1):
        sub = string[idx:idx+3]
        pair = string[idx:idx+2]
        if len(sub) == 3 and sub[0] == sub[2]:
            has_repeat_letter = True
        if pair in pairs:
            pairs[pair].append(idx)
            if idx - pairs[pair][0] > 1:
                has_non_overlapping_pairs = True
        else: 
            pairs[pair] = [idx]
        if has_repeat_letter and has_non_overlapping_pairs:
            return True
    return False

if __name__ == "__main__":
    main()