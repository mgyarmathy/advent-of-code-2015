# --- Part Two ---
# Uh oh - the Accounting-Elves have realized that they double-counted everything red.

# Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

from day_12_1 import sum_json_numbers_regex
import sys
import json

def main():
    input_file = sys.argv[1]
    json_string = open(input_file, 'r').read()
    print sum_json_numbers_regex(filter_red_json_from_string(json_string))

def filter_red_json_from_string(json_string):
    return json.dumps(json.loads(json_string, cls=IgnoreRedJsonDecoder)).replace(' ', '')

class IgnoreRedJsonDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.ignore_red, *args, **kwargs)

    def ignore_red(self, obj):
        return obj if 'red' not in obj.values() else dict()

if __name__ == '__main__':
    main()