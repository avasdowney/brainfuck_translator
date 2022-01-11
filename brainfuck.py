# code taken from https://mathspp.com/blog/writing-interpreter-in-15-loc

from sys import*
import io
import os
V = argv
V.extend([""]*2)
stdin = io.StringIO(V[2])if V[2]else stdin
r = os.path.exists(V[1])
f = r and open(V[1])
b = f.read()if r else V[1]
r and f.close()


def I(b, t, p):
    while b:  # interpret while there's code
        c, *b = b
        c = "+-><,.[]".find(c)  # get next op
        if c in [0, 1]:
            t[p] += 1-2*c
            t[p] %= 256  # increase memory cell and wrap at 256
        if c in [2, 3]:
            p += 5-2*c
            t = [0]*(p < 0)+t+[0]*(p == len(t))
            p = max(p, 0)  # move pointer and adjust tape
        if c == 4:
            i = stdin.read(1) or chr(0)
            t[p] = ord(i) % 256  # read one char as numeric input
        if c == 5:
            stdout.write(chr(t[p]))  # print one char as output
        if c == 6:
            d = 1
            j = [d := d+(x == "[")-(x == "]")for x in b].index(0)
            b, b_ = b[j+1:], b[:j]
            while t[p]:
                t, p = I(b_, t, p)  # loop while memory cell is non-zero
    return t, p


t, p = I(b, [0], 0)
print()
print(t, p)  # interpret and print debugging info
