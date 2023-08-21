Adjacency matrix representation
Implement a program to show the adjacency matrix in graph

Input Format
Take Adjacency matrix input

Output Format
Show the Adjacency matrix representation of graph

Sample Input 0
4
0 1 1 0
1 0 1 1
1 1 0 1
0 1 1 0

Sample Output 0
0 1 1 0 
1 0 1 1 
1 1 0 1 
0 1 1 0 

Python Code:

def print_adjacency_matrix(adj_matrix):
    for row in adj_matrix:
        print(" ".join(map(str, row)))
def main():
    n = int(input())  # Number of nodes
    adj_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adj_matrix.append(row)
    print_adjacency_matrix(adj_matrix)
if __name__ == "__main__":
    main()
