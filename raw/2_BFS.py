import numpy as np

# Global Init
a = np.zeros((20,20), dtype=int) #Adjecency Matrix
visited = np.zeros(20, dtype=int)
queue = []
n = 0

def bfs(v:int):
    for i in range(1,n+1):
        if a[v][i] and not visited[i]:
            queue.append(i)
    if len(queue)!=0:
        f = queue.pop(0)
        visited[f] = 1
        bfs(f)
        

if __name__ == "__main__":
    n = int(input("Enter no. vertices: "))
    
    print("\nEnter adjacency matrix : ")
    for i in range(1, n+1):
        for j in range(1, n+1):
            a[i][j] = int(input())
            
    v = int(input("Enter Starting Vertice: "))
    bfs(v)
    
    print("The nodes that are reachable are: ")
    
    for i in range(1, n+1):
        if(visited[i]):
            print(i, "\t")
        else:
            print("BFS not possible")
