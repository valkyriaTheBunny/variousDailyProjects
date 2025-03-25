def sort_colors(arr):
    # Initialize pointers for the boundaries of each color section
    red, blue = 0, len(arr) - 1
    current = 0

    while current <= blue:
        if arr[current] == 'R':
            # Swap with the red boundary and move the boundary and pointer forward
            arr[current], arr[red] = arr[red], arr[current]
            current += 1
            red += 1
        elif arr[current] == 'B':
            # Swap with the blue boundary and move the blue boundary backward
            arr[current], arr[blue] = arr[blue], arr[current]
            blue -= 1
        else:
            # Skip if it's 'G'
            current += 1


def test_sort_colors():
    arr = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
    sort_colors(arr)
    assert arr == ['R', 'R', 'R', 'G', 'G', 'B', 'B']