N = int(input())
s_dic = {}
t_dic = {}
names = []
for i in range(N):
    s, t = map(str, input().split())
    if s in s_dic.keys():
        l = s_dic[s]
        l.add(i)
        s_dic[s] = l
    else:
        s_dic[s] = set([i])
        
    if t in t_dic.keys():
        l = t_dic[t]
        l.add(i)
        t_dic[t] = l
    else:
        t_dic[t] = set([i])
        
    names.append([s, t])
    
ans = 'Yes'
for i in range(N):
    s, t = names[i]
    if (len(s_dic[s]) >= 2 or (s in t_dic.keys() and len(t_dic[s]) >= 1 and i not in t_dic[s])) and (len(t_dic[t]) >= 2 or (t in s_dic.keys() and len(s_dic[t]) >= 1 and i not in s_dic[t])):
        ans = 'No'
print(ans)