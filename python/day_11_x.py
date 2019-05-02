# --- Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

# Given Santa's current password (your puzzle input), what should his next password be?

import sys

def main():
    current_password = sys.argv[1]
    print next_valid_password(current_password)

def next_valid_password(current_password):
    new_password = increment_password(current_password)
    while not is_valid_password(new_password):
        new_password = increment_password(new_password)
    return new_password

def increment_password(password):
    def increment_char(c):
        return chr(ord(c) + 1) if c != 'z' else 'a'

    lpart = password.rstrip('z')
    num_replacements = len(password) - len(lpart)
    new_password = lpart[:-1] + increment_char(lpart[-1]) if lpart else 'a'
    new_password += 'a' * num_replacements
    return new_password

def is_valid_password(password):
    if 'i' in password or 'o' in password or 'l' in password:
        return False

    has_non_overlapping_pairs = False
    has_increasing_straight = False
    pair_locations = list()
    for idx in range(len(password)-1):
        sub = password[idx:idx+3]
        pair = password[idx:idx+2]
        if len(sub) == 3 and (ord(sub[0]) == (ord(sub[1]) - 1) == (ord(sub[2]) - 2)):
            has_increasing_straight = True
        if pair[0] == pair[1]:
            pair_locations.append(idx)
            if idx - pair_locations[0] > 1:
                has_non_overlapping_pairs = True
        if has_increasing_straight and has_non_overlapping_pairs:
            return True
    return False

if __name__ == '__main__':
    main()