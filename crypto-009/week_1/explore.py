
import string
from itertools import combinations

from origin import strxor

MESSAGES_FILE = "messages.txt"

messages = map(lambda s: s[:-1].decode("hex"), open(MESSAGES_FILE).readlines())

alphabet = string.ascii_lowercase + string.ascii_uppercase

key_len = max(map(len, messages))
key = " " * key_len

enum_messasges = enumerate(messages)
combinations = combinations(enum_messasges, 2)

for ((first_num, first), (second_num, second)) in combinations:
    # print "*" * 10
    # print "{} ^ {} \n".format(first_num, second_num)
    for (char_position, check_char) in enumerate(strxor(first, second)):
        if check_char in
