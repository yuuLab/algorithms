# 再帰関数を利用して解く方法
def resolve() : 
  N = int(input())

  def func(s, n):
      if n == N:
          return s + ' ' + str(n) + ' ' + s
      
      return func(s + ' ' + str(n) + ' ' + s, n+1)

  if N == 1:
      print('1')
  else:
      tmp = func('1', 2)
      print(tmp)

def resolve_2():
  # DPを利用して解く方法
  N = int(input())
          
  dp = [[] for _ in range(N + 1)]

  dp[1] = [1]
  for n in range(2, N + 1):
      dp[n] = dp[n - 1] + [n] + dp[n - 1]
      
  print(*dp[N])

def main(): 
  resolve()
  
if __name__ == "__main__":
    main()