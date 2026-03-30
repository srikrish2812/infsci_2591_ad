def total_n_queens(n):
    """
    returns the total number of solutions for n-queens problem
    """
    if n <= 0:
        return 0

    count = 0
    all_ones = (1 << n) - 1  # bitmask with n lowest bits set to 1

    def backtrack(row, cols, diag1, diag2):
        nonlocal count
        if row == n:
            count += 1
            return

        # available columns are bits that are not occupied by any of the three masks
        available = all_ones & ~(cols | diag1 | diag2)

        while available:
            # pick the lowest set bit as the column for the current row
            col_bit = available & -available
            # remove this column from the available set, toggle using xor
            available ^= col_bit  

            # put the queen and go to the next row
            backtrack(row + 1, cols | col_bit,
                ((diag1 | col_bit) << 1) & all_ones,
                ((diag2 | col_bit) >> 1) & all_ones,
            )
    backtrack(0, 0, 0, 0)
    return count

if __name__ == "__main__":
    for n in range(1, 16):
        print(f"n = {n}: {total_n_queens(n)} solutions")

# Output:
# n = 1: 1 solutions
# n = 2: 0 solutions
# n = 3: 0 solutions
# n = 4: 2 solutions
# n = 5: 10 solutions
# n = 6: 4 solutions
# n = 7: 40 solutions
# n = 8: 92 solutions
# n = 9: 352 solutions
# n = 10: 724 solutions
# n = 11: 2680 solutions
# n = 12: 14200 solutions
# n = 13: 73712 solutions
# n = 14: 365596 solutions
# n = 15: 2279184 solutions
