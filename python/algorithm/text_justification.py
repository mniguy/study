# def reconstruct_text(words, breaks):
#     lines=[]
#     linebreaks=[]
    
#     i=0
#     while True:
#         linebreaks.append(breaks[i])
#         i = breaks[i]
        
#         if i==len(words):
#             linebreaks.append(0)
#             break
    
#     for i in range(len(linebreaks)):
#         lines.append(' '.join(words[linebreaks[i-1]: linebreaks[i]]).strip())
    
#     return lines
      
def badness(line, width):
    length = len(line)-1
    for word in line:
        length += n

    if length > width: return float('inf')
    
    return (width-length)**3


words = input("Enter words >>> ")
width = int(input("Enter width >>> "))

n = len(words)
DP = [0]*(n+1)

for i in range(n-1, -1, -1):
    DP[i] = min(badness(words[i:j], width) + DP[j] for j in range(i+1, n+1))

    

    
    
    
