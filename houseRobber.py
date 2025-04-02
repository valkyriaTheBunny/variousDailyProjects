def houseRobber(numLst: list[int]) -> int:
    if not numLst or numLst == []:
        return 0

    include = 0
    exclude = 0

    for num in numLst:
        newExclude = max(include, exclude)
        include = exclude + num
        exclude = newExclude

    return max(include, exclude)

def test_houseRobber():
    assert houseRobber([2, 4, 6, 2, 5]) == 13
