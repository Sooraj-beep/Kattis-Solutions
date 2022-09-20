import sys
n =  int(sys.stdin.read())

if n < 100:
    print(99)
else:
    if str(n)[len(str(n))-2:] == "49":
        n += 2
    print(int(round(float(n)/100)*100 - 1))