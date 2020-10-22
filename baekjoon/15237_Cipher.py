import sys
from collections import OrderedDict
input = sys.stdin.readline

n, c = map(int, input().split())
messages = list(input().split())
ordered_dict = OrderedDict()

for message in messages:
    if message in ordered_dict:
        ordered_dict[message] += 1
    else:
        ordered_dict[message] = 1

sorted_dict = {k: v for k, v in sorted(ordered_dict.items(), key=lambda item: item[1], reverse=True)}

for k, v in sorted_dict.items():
    print(' '.join([k] * v), end=' ')
