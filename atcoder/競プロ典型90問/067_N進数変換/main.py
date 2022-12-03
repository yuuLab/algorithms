N, K = input().split()

def n_ary_number_from_decimal(value: int, base: int) -> str:
    if value // base:
        return n_ary_number_from_decimal(value // base, base) + str(value % base)
    return str(value % base)
     
    
def to_five_from_eight(target: str) -> str:
    changed = ''
    for t in target:
        if t == '8':
            changed += '5'
        else:
            changed += t
    return changed
   

def operate(octal : str):
    n_decimal = int(octal, 8)
    nine = n_ary_number_from_decimal(n_decimal, 9)
    return to_five_from_eight(nine)


num = N
for i in range(int(K)):
    num = operate(num)
    
print(num)