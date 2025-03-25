def meanByElement(seq: list[int]) -> list[int]:
    sorted_sequence = []
    medians = []

    for num in seq:
        # Insert the new number into the sorted sequence without changing the original order
        insert_index = len(sorted_sequence)
        for i, x in enumerate(sorted_sequence):
            if num < x:
                insert_index = i
                break
        sorted_sequence.insert(insert_index, num)

        # Calculate the median
        n = len(sorted_sequence)
        if n % 2 == 0:
            median = (sorted_sequence[n // 2 - 1] + sorted_sequence[n // 2]) / 2
        else:
            median = sorted_sequence[n // 2]
        medians.append(median)

    return medians


def test_meanByElement():
    medians = meanByElement([2, 1, 5, 7, 2, 0, 5])
    assert medians == [2, 1.5, 2, 3.5, 2, 2, 2]

