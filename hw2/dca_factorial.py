"""
Use the divide-and-conquer apporach to write a recursive algorithm that computes n!
"""


def dca_fact(p, q):
    if p > q:
        return 1
    if p == q:
        return p
    m = (p + q) // 2
    return dca_fact(p, m) * dca_fact(m + 1, q)


if __name__ == "__main__":
    n = int(input())
    print(f"{n}! =", dca_fact(1, n))
