"""
Use the divide-and-conquer apporach to write a recursive algorithm that computes n!
"""


def factorial(n):
    def product(l, r):
        if l > r:
            return 1  # handles n=0 case
        if l == r:
            return l
        m = (l + r) // 2
        return product(l, m) * product(m + 1, r)

    return product(1, n)


if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
