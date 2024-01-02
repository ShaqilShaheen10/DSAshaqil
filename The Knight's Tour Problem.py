The Knight's Tour Problem
Given a N*N board with the Knight placed on the first block of an empty board. Moving according to the rules of chess knight must visit each square exactly once.
Print the order of each cell in which they are visited.

Input Format
Take value as 8 only

Constraints
Time:- 1 Sec

Output Format
Knight tour in the form of matrix

Sample Input 0
8

Sample Output 0
0 59 38 33 30 17 8 63 
37 34 31 60 9 62 29 16 
58 1 36 39 32 27 18 7 
35 48 41 26 61 10 15 28 
42 57 2 49 40 23 6 19 
47 50 45 54 25 20 11 14 
56 43 52 3 22 13 24 5 
51 46 55 44 53 4 21 12 

Python Code:

def solveKT(n):
    board = [[-1 for _ in range(n)] for _ in range(n)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    def isSafe(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    def printSolution():
        for row in board:
            print(*row)
    def solveKTUtil(curr_x, curr_y, pos):
        nonlocal n
        if pos == n**2:
            return True
        for i in range(8):
            new_x, new_y = curr_x + move_x[i], curr_y + move_y[i]
            if isSafe(new_x, new_y):
                board[new_x][new_y] = pos
                if solveKTUtil(new_x, new_y, pos + 1):
                    return True
                board[new_x][new_y] = -1
        return False
    board[0][0] = 0
    if not solveKTUtil(0, 0, 1):
        print("Solution does not exist")
    else:
        printSolution()
if __name__ == "__main__":
    n = 8
    solveKT(n)
