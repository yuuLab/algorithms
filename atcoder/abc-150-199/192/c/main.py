N, K = map(int, input().split())

def f(num: int):
    if num == 0:
        return 0
    
    l = list(str(num))
    l_desc = sorted(l, reverse=True)
    l_desc_str = ''
    for l_ in l_desc:
        l_desc_str += l_

    l_asc = sorted(l)
    l_asc_str = ''
    removeZero = True
    for l_ in l_asc:
        if removeZero and l_ == '0':
            continue
        else:
            l_asc_str += l_
            removeZero = False
    num = int(l_desc_str) - int(l_asc_str) 
    return num

a = N
for i in range(K):
    a = f(a)
    if a == 0:
        break
print(a)



# 模範回答
def g1(n):
    return int(''.join(sorted(str(n))[::-1]))
def g2(n):
    return int(''.join(sorted(str(n))))
def f(n):
    return g1(n)-g2(n)
for _ in range(K):
    N = f(N)
print(N)