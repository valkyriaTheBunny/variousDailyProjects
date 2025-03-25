def print_spiral(matrix):
    if not matrix:
        return
    
    top_row, bottom_row = 0, len(matrix) - 1
    left_col, right_col = 0, len(matrix[0]) - 1

    while top_row <= bottom_row and left_col <= right_col:
        # Print top row
        for i in range(left_col, right_col + 1):
            print(matrix[top_row][i])
        top_row += 1

        # Print right column
        for i in range(top_row, bottom_row + 1):
            print(matrix[i][right_col])
        right_col -= 1

        # Print bottom row
        if top_row <= bottom_row:
            for i in range(right_col, left_col - 1, -1):
                print(matrix[bottom_row][i])
            bottom_row -= 1

        # Print left column
        if left_col <= right_col:
            for i in range(bottom_row, top_row - 1, -1):
                print(matrix[i][left_col])
            left_col += 1

def main() -> None:
    # Example usage
    matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

    print_spiral(matrix)

if __name__ == '__main__':
    main()