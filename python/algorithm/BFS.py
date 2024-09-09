def BFS(V, Adj, s):
    level = { s : 0 }
    parent = { s : None } 
    i = 1
    frontier = [s]
    
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i+=1
        
    for i in V:
        print(level[i], parent[i])
        
        
Adj = {"v": ["r"], "r": ["s", "v"], "s": ["r", "w"], "w": ["s", "t", "x"], 
     "t": ["w", "x", "u"], "x": ["w", "t", "u", "y"], "u": ["t", "x", "y"], "y": ["x", "u"]}

V = ["r", "s", "t", "u", "v", "w", "x", "y"]

BFS(V, Adj, "s")
   