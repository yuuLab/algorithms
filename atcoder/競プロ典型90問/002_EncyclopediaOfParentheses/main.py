N = int(input())

def checkPattern(pattern: str) -> bool:
    can_use_count = 0
    for i in range(len(pattern)):
        if pattern[i] == ')':
            if can_use_count == 0:
                return False
            else:
                can_use_count -= 1
        else:
            can_use_count += 1
    return True if can_use_count == 0 else False
 
 
def dfs():
    def _dfs(pattern : str):
        if len(pattern) == N:
            if checkPattern(pattern):
                print(pattern)
            return
        _dfs(pattern + '(')
        _dfs(pattern + ')')
    _dfs('(')
    
dfs()


# 下記スタックキューを使っても判定処理を実現できるが、本条件では今回はTLEになるため却下
import queue

def checkPattern2(pattern : str) -> bool:
    q = queue.LifoQueue()
    for p in pattern:
        if p == ')':
            if q.empty():
                return False
            else:
                q.get()
        else:
            q.put('(')
    return q.empty()