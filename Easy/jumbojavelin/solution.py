import sys
first = True
d = None
s = 0
for line in sys.stdin:
    if first:
        d = int(line)
        first = False
    else:
        s += int(line)    

print(s - (d-1))


