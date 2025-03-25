#naive approach
def flipBulb(bulbs: list[int]) -> int:
    bulbs_ = bulbs.copy()
    cost = 0
    while 0 in bulbs_:
        for i in range(len(bulbs)):
            if bulbs_[i] == 1:
                pass
            else:
                bulbs_[i] = 1
                cost += 1
                for j in range(i + 1, len(bulbs_)):
                    bulbs_[j] = 0 if bulbs_[j] == 1 else 1 
    return cost

print(flipBulb([1, 0, 1]))

def findCost(bulbs: list[int]) -> int:
    temp = bulbs.copy()
    cost = 0

    for bulb in temp:
        if cost % 2 == 0:
            bulb = bulb
        else:
            bulb = not bulb

        if bulb % 2 == 1:
            continue
        else:
            cost += 1

    return cost

print(findCost([0, 1, 0, 1, 1, 0, 1, 1]))