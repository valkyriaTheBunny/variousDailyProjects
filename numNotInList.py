from random import choice
from big_o import big_o

def randNotInList(entry) -> int:
    num = entry[0]
    lst = entry[1]
    
    # Generate a list of numbers from 0 to num - 1 excluding those in lst
    valid_numbers = [i for i in range(num) if i not in lst]
    
    # Select a random number from the valid numbers list
    return choice(valid_numbers)


def test_randIsNot() -> None:
    lst = [10, 37, 43, 2, 7, 14]
    assert randNotInList(55, lst) not in lst

def main() -> None:
    lstOfLsts = [[0], [10, 37, 43, 2, 7, 14], [2, 5, 9, 11, 13, 4, 22, 8], 
                [8, 4, 6, 2, 13, 7, 9, 5, 10, 20], [4, 2, 9, 7, 16, 11, 13, 12], 
                [9, 5, 13, 11, 15, 14, 1, 2, 7]]
    
    lstOfNums = [10, 55, 25, 30, 16, 20]

    def dataGrab(n: int):
        try:
            return (lstOfNums[n], lstOfLsts[n])
        except IndexError:
            raise ValueError(f"Index out of bounds: {n}")
        
    print(randNotInList(dataGrab(1)))
    result = big_o(randNotInList, dataGrab, min_n=1, max_n=len(lstOfLsts) - 1)[0]
    print(result) 

if __name__ == '__main__':
    main()