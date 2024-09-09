import heapq
d = {}
pi = {}
Q = []

def dijkstra(V, Adj, w, s):
    for v in V:
        d[v] = float('inf')
    d[s] = 0
    pi[s] = None
    S = []
    heapq.heappush(Q, [d[s], s])

    while Q:
        _, u = heapq.heappop(Q)
        S.append(u)
        for v in Adj[u]:
            if d[v] > d[u] + w[(u, v)]:
                d[v] = d[u] + w[(u, v)]
                pi[v] = u
                heapq.heappush(Q, [d[v], v])
                print("d[", v, "]:", d[v], ", pi[", v, "]:", pi[v])
        
w = {("s", "y"): 5, ("s", "t"): 10, ("t", "y"): 2, ("t", "x"): 1, ("x", "z"): 4, 
     ("y", "t"): 3, ("y", "z"): 2, ("y", "x"): 9, ("z", "s"): 7, ("z", "x"): 6}   

Adj = {"s":["t", "y"], "t": ["y", "x"], "x": ["z"], "y": ["t", "x", "z"], "z": ["s", "x"]}  
       
V = {"s", "t", "y", "x", "z"}

dijkstra(V, Adj, w, "s")
