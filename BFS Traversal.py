BFS Traversal
Given an undirected and disconnected graph G(V, E), print its BFS traversal.
Note:
Here you need to consider that you need to print BFS path starting from vertex 0 only.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Take graph input in the adjacency matrix.
Handle for Disconnected Graphs as well

Input Format
The first line of input contains two integers, that denote the value of V and E.
Each of the following E lines contains space separated two integers, that denote that there exists an edge between vertex a and b.

Constraints
0 <= V <= 1000
0 <= E <= (V * (V - 1)) / 2
0 <= a <= V - 1
0 <= b <= V - 1
Time Limit: 1 second

Output Format
Print the BFS Traversal, as described in the task.
  
Sample Input 0
4 4
0 1
0 3
1 2
2 3

Sample Output 0
0 1 3 2

Sample Input 1
0 0

Python Code:

from collections import deque
def bfs(graph, start, visited, result):
    queue = deque([start])
    visited[start] = True
    while queue:
        current_vertex = queue.popleft()
        result.append(current_vertex)
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
def bfsTraversal(V, E, edges):
    graph = {i: [] for i in range(V)}
    visited = [False] * V
    result = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    for vertex in range(V):
        if not visited[vertex]:
            bfs(graph, vertex, visited, result)
    return result
if __name__ == "__main__":
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    result = bfsTraversal(V, E, edges)
    print(" ".join(map(str, result)))
