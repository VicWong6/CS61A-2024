""" for test Generalizing course: Get the approximate value of pi
"""

from operator import mul

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def term_pi(k):
    """ 定义了一个关于多项收敛的项，可以近似求pi的值
    """
    return 8 / mul(4 * k - 3, 4 * k - 1)

def summation(k, term):
    """ Sum the first K terms of sequence 
    >>> summation(5, cube)
    225
    """
    total, n = 0, 1
    while n <= k:
        # term 相当于是传递了一个函数，根据调用的时候来决定的
        total, n = total + term(n), n + 1
    return total


def sum_natural_2(k):
    """ to sum <= k natural numbers
    这个是将sum_natural_1 函数重构了，直接用泛化的统一的函数来替代
    >>> sum_natural_2(5)
    15
    """
    return summation(k, identity)

def sum_cubes_2(k):
    """ to sum <= k cube numbers, 
        这个是将sum_cubes_1 函数重构了，直接用泛化的统一的函数来替代
    >>> sum_cubes_2(5)
    225
    """
    return summation(k, cube)

def sum_natural_1(k):
    """ to sum <= k natural numbers 
    >>> sum_natural_1(5)
    15
    """
    total, n = 0, 1
    while n <= k:
        total += n
        n += 1
    return total

def sum_cubes_1(k):
    """ to sum <= k cube numbers, 可以看出来和sum_natural_1 有重复的代码
    >>> sum_cubes_1(5)
    225
    """
    total, n = 0, 1
    while n <= k:
        total, n = total + pow(n, 3), n + 1
    return total