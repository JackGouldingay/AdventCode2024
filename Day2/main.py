from util import load_data

data = load_data("input.txt")

for idx, row in enumerate(data):
    isSafe = True
    isIncreasing = False
    lastNum = int(row[0])
    for col in range(1, len(row)):
        currentNum = int(row[col])
        difference = lastNum - currentNum
        if(difference > 3): isSafe = False
        print(lastNum, currentNum, difference)
        lastNum = currentNum
    print("Row: %s isSafe = %s" % (idx, isSafe))