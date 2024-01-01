Rat in the maze 1
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block i.e., maze[0][0] and destination block is lower rightmost block 
i.e., maze[N-1][N-1]. A rat starts from source and has to reach the destination. The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination. Note that this is a
simple version of the typical Maze problem. For example, a more complex version can be that the rat can move in 4 directions and a more complex version can be with 
a limited number of moves.
Input Format
First line row value
Second line col value
Thrid line start taking matrix

Constraints
Time:- 1 Sec

Output Format
Path of the rat in the form of matrx

Sample Input 0
4
4
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1

Sample Output 0
1 0 0 0 
1 1 0 0 
0 1 0 0 
0 1 1 1 

Sample Input 1
4
4
1 0 0 1
1 1 0 1
0 1 0 0
1 1 1 1

Sample Output 1
1 0 0 0 
1 1 0 0 
0 1 0 0 
0 1 1 1 

Python Code:

def solve_maze(rows, cols, maze):
    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1
    def solve(x, y):
        if x == rows - 1 and y == cols - 1:
            solution[x][y] = 1
            return True
        if is_valid_move(x, y):
            solution[x][y] = 1
            if solve(x + 1, y) or solve(x, y + 1):
                return True
            solution[x][y] = 0 
            return False
    solution = [[0] * cols for _ in range(rows)]
    if solve(0, 0):
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("No solution exists.")
rows = int(input())
cols = int(input())
maze = [list(map(int, input().split())) for _ in range(rows)]
solve_maze(rows, cols, maze)
