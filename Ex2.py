from itertools import product

s1 ="1 2 3 4 5 6 7 8 9"
s2 = "a b c d e f g h i j k"

def invers(s2):
    return s2[::-1]

def concat(s1, s2):
    return s1+s2

print(concat(s1,s2))

def inverse(s2):
    return s2[::-1]

print(invers(s2))

def extract(s, i, j):
    return s[i:j+1]

print(extract(s2, 5, 12))

s = "Andrei este student"

def replace(s, sub):
    return s.replace(sub, "Alex")

print(replace(s, "Andrei"))