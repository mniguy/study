# # recursive
x = {}
def cut_rod(l, v):
    if l < 1: return 0
    if l not in x:
        for piece in range(1, l+1):
            y = v[piece] + cut_rod(l-piece, v)
            if (l not in x) or (x[l] < y):
                x[l] = y
    return x[l]

v = [1, 5, 8, 9, 10, 17, 17, 20]
l = len(v)-1
print(cut_rod(l, v))

x ={}
def cutrod(l, v):
    if l<1: return 0
    if l not in x:
        for piece in range(1, l+1):
            y = v[piece] + cut_rod(1-piece, v)
            if (l not in x) or (x[l]<y):
                x[l] = y
    return x[l]

x={}
def cut_rod(l, v):
    if l<1: return 0
    if l not in x:
        for piece in range(1, l+1):
            y = v[piece] + cut_rod(l-piece, v)
            if (l not in x) or (x[l]<y):
                x[l] =y
    return x[l]