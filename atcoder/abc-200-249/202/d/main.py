def cmb(n, k):
    ret = 1
    for i in range(1, k):
        ret = ret * (n-i) // (i+1)
    return ret
 
def solve(a, b, k):
    if k == 0:
        return "a"*a + "b"*b
    c = cmb(a+b-1, a-1)
    if c > k:
        return "a" + solve(a-1, b, k)
    else:
        return "b" + solve(a, b-1, k-c)


a, b, k = map(int, input().split())
print(solve(a, b, k-1))