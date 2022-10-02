N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
S = input()

# right_min : キーを k としたとき、y=k でありかつ右を向いている人のうち最も x 座標が小さい人
# left_max : キーを k としたとき、y=k でありかつ左を向いている人のうち最も x 座標が大きい人
right_min, left_max = dict(), dict()
ans = 'No'
for i in range(N):
    if S[i] == 'R':
        # 衝突する場合は終了
        if Y[i] in left_max and X[i] < left_max[Y[i]]:
            ans = 'Yes'
            break
        # 右向きの人として保持
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]])
        else:
            right_min[Y[i]] = X[i]
    else:
        # 衝突する場合は終了
        if Y[i] in right_min and right_min[Y[i]] < X[i]:
            ans = 'Yes'
            break
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]        
            
print(ans)