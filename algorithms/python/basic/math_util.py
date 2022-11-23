import math

def make_divisors(n : int) -> list:
    """
    nの約数を返却する。
    """
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def factorial(n : int) -> int: 
    """
    nの階乗を算出する。
    """
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  


def is_prime(n : int) -> bool:
    """
    素数判定
    """
    if n == 1: return False
 
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True


def to_n_ary_number_from_decimal(value: int, base: int) -> str:
    """
    10進数の数値をN進数に変換した文字列を返す。
    
    Parameters
    ----------
    param value: target value (Decimal number)
    param base: change to {base} digits
    """
    if value // base:
        return to_n_ary_number_from_decimal(value // base, base) + str(value % base)
    return str(value % base)