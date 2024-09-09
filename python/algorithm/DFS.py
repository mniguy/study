count = 0
parent = {}
start = {}
end = {}
edge = {}
            
def DFS_visit(V, Adj, s):
    global count
    count += 1
    start[s] = count   
        
    for v in Adj[s]:
        if v not in parent:
            parent[v] = s
            edge[(s, v)] = "tree"
            DFS_visit(V, Adj, v)  
        if (s, v) not in edge:
            if v not in end:
                edge[(s, v)] = "back"
            elif start[s] < start[v]:
                if v in end:
                    if s not in end:
                        edge[(s, v)] = "forward"
            else:
                edge[(s, v)] = "cross"
                

    count += 1
    end[s] = count

def DFS(V, Adj):
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS_visit(V, Adj, s)   
                    
    for s in V:
        print(s, ":", parent[s], "(", start[s], ",", end[s], ")")  
        
    
Adj = {"u": ["v", "x"], "v": ["y"], "w": ["y", "z"], "x": ["v"], "y": ["x"], "z": ["z"]}

V = ["u", "v", "w", "x", "y", "z"]

DFS(V, Adj)    
print(edge)