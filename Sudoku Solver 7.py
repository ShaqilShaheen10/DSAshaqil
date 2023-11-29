Sudoku Solver 7
Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and 
subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.

Input Format
First line value of row
Second Line value of col
From third line matrix input taking start

Constraints
Time:- 1 Sec

Output Format
Fully Filled matrix

Sample Input 0
9
9
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0 
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0

Sample Output 0
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9

Sample Input 1
9
9
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 2 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 6 
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 9

Sample Output 1
No Solution exists

Python Code:
def is_safe(grid, row, col, num):
    # Check if the number is not already present in the row, column, and subgrid
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num or grid[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(grid):
    empty = find_empty_location(grid)
    if not empty:
        return True  # No empty locations, puzzle is solved

    row, col = empty

    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True  # If placing the number leads to a solution, return True

            # If placing the number doesn't lead to a solution, backtrack
            grid[row][col] = 0

    return False  # No number can be placed, backtrack further

def find_empty_location(grid):
    # Find the first empty location in the grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()

# Input
row = int(input())
col = int(input())
grid = []
for _ in range(row):
    row_values = list(map(int, input().split()))
    grid.append(row_values)

# Solve Sudoku
if solve_sudoku(grid):
    # Output the solution
    print_grid(grid)
else:
    print("No Solution exists")

