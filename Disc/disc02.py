#make_keeper
def is_even(x):
    return x % 2 == 0
  
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"

    def f(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
            i += 1
    return f

#find_digit
def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    "*** YOUR CODE HERE ***"

    def kth_digit(x):
        # Divide x by 10^(k-1) to shift the kth digit to the rightmost position
        for i in range(1, k):
            x //= 10
        return x % 10
    return kth_digit

def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            right_digit = x % 10
            left_digit = (x // (10 ** k)) % 10
            if left_digit != right_digit:
                return False #只要不相等立刻退出循环，返回false
            x //= 10
        return True #while循环结束后执行,表示所有k位相隔的数字都相等
    return check

