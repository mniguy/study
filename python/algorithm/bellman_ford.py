d = {}
pi = {}

def bFord(V, Adj, w, s):
    for v in V:
        d[v] = float('inf')
    d[s] = 0
    pi[s] = None
    a = False
    n = len(Adj)
    for k in range(n-1):
        for u in V:
            for v in Adj[u]:
                if d[v] > d[u] + w[(u, v)]:
                    d[v] = d[u] + w[(u, v)]
                    pi[v] = u
                    print("d[", v, "]:", d[v], ", pi[", v, "]:", pi[v])
    for u in V:
        for v in Adj[u]:
            if d[v] > d[u] + w[(u, v)]:
                a = True
                break
    print(a)           
        
        
w = {("t", "x"): 5, ("t", "y"): 8, ("t", "z"): -4, ("x", "t"): -2, ("y", "x"): -3,
     ("y", "z"): 9, ("z", "x"): 7, ("z", "s"): 2, ("s", "t"): 6, ("s", "y"): 7}

Adj = {"s":["t", "y"], "t": ["y", "x", "z"], "x": ["t"], "y": ["x", "z"], "z": ["s", "x"]}  
       
V = {"s", "t", "y", "x", "z"}

bFord(V, Adj, w, "s")
