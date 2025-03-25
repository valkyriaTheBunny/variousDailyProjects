from big_o import big_o

def divideAndConqSearch(data: tuple[list: int, int]) -> int:
    nums = data[0]
    val = data[1]

    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low
        count = high - low
        while count > 0:
            count -= 1
            mid += 1

        if nums[mid] == val:
            return True
        elif nums[mid] < val:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main() -> None:
    lstOfLsts = [[0, 2, 3], [2, 7, 10, 14, 37, 43], [2, 4, 5, 8, 9, 11, 13, 22],
                [2, 5, 4, 6, 8, 9, 10, 13, 20], [2, 4, 7, 9, 11, 12, 13, 16],
                [1, 2, 5, 7, 9, 11, 13, 14, 15], [2, 4, 6, 9, 11, 14, 15, 16, 18, 19, 20],
                [7, 8, 12, 14, 17, 20, 21, 23, 24, 30, 35, 38, 41, 43, 44, 45, 47, 48],
                [4, 5, 7, 9, 10, 11, 13, 14, 16, 18, 20, 23, 25, 26, 27, 29, 32, 35, 37, 38, 39, 40,
                 42, 45, 47, 50, 54, 56, 57, 61, 64, 65, 66, 72],
                [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 22,
                 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 39, 40, 41, 42,
                 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 57, 57, 58, 59, 60, 61, 62, 63,
                 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                 84, 85, 86, 87, 88, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 99, 100],
                [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 22,
                 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 39, 40, 41, 42,
                 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 57, 57, 58, 59, 60, 61, 62, 63,
                 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                 84, 85, 86, 87, 88, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 99, 100, 101, 102,
                 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
                 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134],
                [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 22,
                 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 39, 40, 41, 42,
                 43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 54, 55, 57, 57, 58, 59, 60, 61, 62, 63,
                 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
                 84, 85, 86, 87, 88, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 99, 100, 101, 102,
                 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118,
                 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134,
                 136, 138, 141, 143, 144, 147, 149, 151, 154, 156, 158, 159, 162, 164, 167, 170]]

    lstOfNums = [0, 7, 13, 4, 16, 5, 13, 6, 2, 92, 127, 151]

    def dataGrab(n: int):
        try:
            return (lstOfLsts[n], lstOfNums[n])
        except IndexError:
            raise ValueError(f"Index out of bounds: {n}")

    result = big_o(divideAndConqSearch, dataGrab, min_n=1, max_n=len(lstOfLsts) - 1)[0]
    print(result)

if __name__ == '__main__':
    main()
