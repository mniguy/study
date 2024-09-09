memo={}

def fibo(n):
    if n in memo:
        return memo[n]
    else:
        if n<=2:
            f=1
        else:
            f=fibo[n-1]+fibo[n-2]
        memo[n]=f
    return f

print(fibo(5))