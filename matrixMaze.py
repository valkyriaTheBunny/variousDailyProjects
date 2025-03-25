from collections import deque

def min_steps_to_reach_end(matrix: list[list[bool]], start: list[int, int], end: list[int, int]):
    if not matrix or not matrix[0]:
        return None

    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set()

    while queue:
        current_row, current_col, steps = queue.popleft()

        if (current_row, current_col) == end:
            return steps

        for dr, dc in directions:
            new_row, new_col = current_row + dr, current_col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == False and (new_row, new_col) not in visited:
                queue.append((new_row, new_col, steps + 1))
                visited.add((new_row, new_col))

    return None  # No path found

# Example usage:
matrix = [
    [False, False, False, False],
    [True, True, False, True],
    [False, False, False, False],
    [False, False, False, False]
]
start = (3, 0)
end = (0, 0)

result = min_steps_to_reach_end(matrix, start, end)
print(result)
