#Breadth First Search
def BFS(start,graph):
    visited=[start]
    q=[start]
    while len(q)!=0:
        ele=q.pop(0)
        for i in graph[ele]:
            if i not in visited:
                q.append(i)
                visited.append(i)
    return visited

graph={
    "A":["B","C"],
    "B":["C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}
res=BFS("B",graph)
print(res)



#Depth First Search
def DFS(start,graph,visited=None):
    if visited==None:
        visited=[]
    visited.append(start)
    for neighbour in graph[start]:
        if neighbournot in visited:
            DFS(neighbour,graph,visited)
    return visited
graph={
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","E"],
    "D":["B","E"],
    "E":["C","D"]
}

res = BFS("E", graph)
print(res)
