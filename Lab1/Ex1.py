from itertools import product

S1 = "abc"
S2 = "xyz"

def concatenate(S1, S2):
    return S1 + S2

print(concatenate(S1, S2))


def invers(S1):
    return S1[::-1]

print(invers(S1))

def substitute(S1):
    return S1.replace("a", "b")

print(substitute(S1))

def length(S1):
    return len(S1)

print(length(S1))