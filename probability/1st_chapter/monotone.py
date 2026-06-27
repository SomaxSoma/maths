import numpy as np

N = 10000
grid = np.linspace(0, 1, N)

def closed_open(a, b):
    return (grid >= a) & (grid < b)

def open_open(a, b):
    return (grid > a) & (grid < b)

print("INCREASING: A_n = [0, n/(n+1))")
union = np.zeros(N, dtype=bool)
for n in range(1, 8):
    A_n = closed_open(0, n/(n+1))
    union = union | A_n
    print(f"  n={n}  A_n reaches {n/(n+1):.4f}  |  union size = {union.sum()}")
print(f"  Limit → [0, 1)  ({union.sum()} of {N} points covered)\n")

print("DECREASING: A_n = [0, 1/n)")
intersection = np.ones(N, dtype=bool)
for n in range(1, 8):
    A_n = closed_open(0, 1/n)
    intersection = intersection & A_n
    print(f"  n={n}  A_n reaches {1/n:.4f}  |  intersection size = {intersection.sum()}")
print(f"  Limit → {{0}}  ({intersection.sum()} points remain)\n")

print("TEXTBOOK: Does the bracket at 0 matter?")
inter_closed = np.ones(N, dtype=bool)
inter_open   = np.ones(N, dtype=bool)
for i in range(1, 200):
    inter_closed = inter_closed & closed_open(0, 1/i)
    inter_open   = inter_open   & open_open(0, 1/i)
print(f"  [0,1/i) intersection: {inter_closed.sum()} points  → {{0}}")
print(f"  (0,1/i) intersection: {inter_open.sum()} points  → empty set")