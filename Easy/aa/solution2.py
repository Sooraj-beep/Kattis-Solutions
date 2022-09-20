import sys
data = [w.strip() for w in sys.stdin.readlines()]
n = int(data[0])
i = 1
# ~ will be our aa character
isSort = True
while i < n:
    # print(sorted(data[i:i+2]))
    if sorted(data[i:i+2]) == data[i:i+2]:
        i+=1
        continue
    else:
        bigger = data[i+1]
        if "aa" in bigger:
            revBigger = bigger[::-1]
            if bigger == "aa":
                data[i+1] = "~"
                continue
            for j in range(len(revBigger) - 1):
                if revBigger[j] == "a" and revBigger[j+1] == "a":                      
                    revBigger = revBigger[:j] + revBigger[j+1:]
                    revBigger = revBigger[:j] + "~" + revBigger[j+1:]
                    data[i+1] = revBigger[::-1]

                    break
                    
        else:
            isLoop = False
            revSlightlyBigger = data[i][::-1]
            for j in range(len(revSlightlyBigger) - 1):
                if revSlightlyBigger[j] == "~" and revSlightlyBigger[j+1] == "~":
                    revSlightlyBigger = revSlightlyBigger[:j] + revSlightlyBigger[j+1:]
                    revSlightlyBigger = revSlightlyBigger[:j] + revSlightlyBigger[j+1:]
                    revSlightlyEvenBigger = revSlightlyBigger[:j] + "aa~" + revSlightlyBigger[j+1:]
                    revSlightlyBigger = revSlightlyBigger[:j] + "a~a" + revSlightlyBigger[j+1:]
                    
                    if revSlightlyBigger[::-1] > data[i-1] and revSlightlyBigger[::-1] < data[i+1]:
                       isLoop = True
                       data[i] = revSlightlyBigger[::-1]
                       i += 1 
                       break
                    elif revSlightlyEvenBigger[::-1] > data[i-1] and revSlightlyEvenBigger[::-1] < data[i+1]:
                       isLoop = True
                       data[i] = revSlightlyEvenBigger[::-1]
                       i += 1 
                       break

            
            if not isLoop:
                isSort = False
                break

if isSort:
    print("yes")
else:
    print("no")