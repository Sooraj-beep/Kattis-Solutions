import sys
data = [w.strip() for w in sys.stdin.readlines()]
stores = int(data[0])
inventory = ['']*int(data[0])


for i in range(int(data[1])):
    (store_number, item) = data[i+2].split()
    inventory[int(store_number)] += item

offset = 2 + int(data[1]) + 1
total_items = int(data[offset - 1])

j = 0
i = 0
isFirst = True
firstStore = None

while i < total_items and j < stores:
    if data[i + offset] in inventory[j]:
        if isFirst:
            isFirst = False
            firstStore = j
        i += 1
    else:
        j +=1

if i == total_items:
    i = 0:
    while i < total_items:
        if i + 1 < total_items:
            if data[i + offset + 1] in inventory[firstStore] 
                print('ambiguous')
                break
        if firstStore + 1 < stores:
            if data[i + offset] in inventory[firstStore + 1]
else:
    print('impossible')