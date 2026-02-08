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
    print(f"{0}! = {dca_fact(1, 0)}")
    print(f"{1}! = {dca_fact(1, 1)}")
    print(f"{2}! = {dca_fact(1, 2)}")
    print(f"{3}! = {dca_fact(1, 3)}")
    print(f"{5}! = {dca_fact(1, 5)}")
    print(f"{8}! = {dca_fact(1, 8)}")
    print(f"{10}! = {dca_fact(1, 10)}")
