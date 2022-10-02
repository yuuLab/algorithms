N, M, Q = map(int, input().split())
w_v_list = [list(map(int, input().split())) for _ in range(N)]
x = list(map(int, input().split()))

for i in range(Q):
    L, R = map(int, input().split())
    l = x[:]
    w_v_list_copy =  w_v_list[:]
    for j in range(L-1, R):
        l[j] = 0
        l.sort()
    max_val = 0
    for w in l:
        temp_max_val = 0
        idx = -1
        for k, w_v in enumerate(w_v_list_copy):
            if w >= w_v[0]:
                if temp_max_val < w_v[1]:
                    temp_max_val = w_v[1]
                    idx = k
                    
        max_val += temp_max_val
        if idx != -1:
            del w_v_list_copy[idx]
        
    print(max_val)