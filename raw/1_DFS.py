import numpy as np

a = np.zeros((20, 20), dtype=int)
reach = np.zeros(20, dtype=int)
n = int(input("Enter no of vertices : "))

def dfs(v):
    reach[v] = 1
    for i in range(1, n+1):
        if a[v][i] and not reach[i]:
            print(f"\n{v}->{i}")
            dfs(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        reach[i] = 0
        a[i][j] = 0

print("\nEnter adjacency matrix : ")
for i in range(1, n+1):
    for j in range(1, n+1):
        a[i][j] = int(input())

dfs(1)

count = np.count_nonzero(reach)
if count == n:
    print("\nGraph is connected.")
else:
    print("\nGraph is disconnected.")
