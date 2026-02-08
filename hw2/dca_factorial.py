"""
Use the divide-and-conquer apporach to write a recursive algorithm that computes n!
"""

from ast import Return


def factorial(n):
    def product(l, r):
        if l > r:
            return 1  # handles n=0 case
        if l == r:
            return l
        m = (l + r) // 2
        return product(l, m) * product(m + 1, r)

    return product(1, n)


def dca_fact(p, q):
    if p > q:
        return 1
    if p == q:
        return p
    m = (p + q) // 2
    return dca_fact(p, m) * dca_fact(m + 1, q)


if __name__ == "__main__":
    n = int(input())
    print("Factorial function", factorial(n))
    print("Second Factorial", dca_fact(1, n))
