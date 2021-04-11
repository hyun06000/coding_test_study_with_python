import collections
import sys

def sysmax():
    return sys.maxsize
a = collections.defaultdict(sysmax)

print(a['key'])