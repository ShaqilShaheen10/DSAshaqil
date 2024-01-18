Kruskal's Algorithm
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
For printing MST follow the steps -
In one line, print an edge which is part of MST in the format -
v1 v2 w
where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
Print V-1 edges in above format in different lines.
Note : Order of different edges doesn't matter.

Input Format
Line 1: Two Integers V and E (separated by space)
Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)

Constraints
2 <= V, E <= 10^5
Time Limit: 1 sec

Output Format
Print the MST, as described in the task.

Sample Input 0
4 4
0 1 3
0 3 5
1 2 1
2 3 8

Sample Output 0
1 2 1
0 1 3
0 3 5

Sample Input 1
3 3
1 2 6
2 0 2
1 0 2

Sample Output 1
0 2 2
0 1 2


Python Code:

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
def find_set(ds, v):
    if ds.parent[v] != v:
        ds.parent[v] = find_set(ds, ds.parent[v])
    return ds.parent[v]
def union_sets(ds, u, v):
    root_u = find_set(ds, u)
    root_v = find_set(ds, v)
    if ds.rank[root_u] < ds.rank[root_v]:
        ds.parent[root_u] = root_v
    elif ds.rank[root_u] > ds.rank[root_v]:
        ds.parent[root_v] = root_u
    else:
        ds.parent[root_u] = root_v
        ds.rank[root_v] += 1
def kruskal_mst(edges, V):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(V)
    mst_edges = []
    for edge in edges:
        u, v, w = edge
        if find_set(ds, u) != find_set(ds, v):
            mst_edges.append(edge)
            union_sets(ds, u, v)
    return mst_edges
V, E = map(int, input().split())
edges = []
for _ in range(E):
    ei, ej, w = map(int, input().split())
    edges.append((ei, ej, w))
mst_edges = kruskal_mst(edges, V)
for edge in mst_edges:
    v1, v2, w = edge
    print(min(v1, v2), max(v1, v2), w)
