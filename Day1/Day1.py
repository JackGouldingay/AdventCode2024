contents = open("input.txt").read().split("\n")
leftList = []
rightList = []
leftListSelected = True
for idx, i in enumerate(contents):
    rowSplit = i.split(" ")
    leftList.append(int(rowSplit[0]))
    rightList.append(int(rowSplit[len(rowSplit)-1]))

leftList.sort()
rightList.sort()
total_distance = 0

for i in range(len(leftList)):
    difference = abs(leftList[i] - rightList[i])
    total_distance += difference

print(total_distance)
