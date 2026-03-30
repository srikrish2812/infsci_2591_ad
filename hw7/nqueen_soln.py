def total_n_queens(n):
    """
    returns the total number of solutions for n-queens problem
    """
    if n <= 0:
        return 0

    count = 0
    all_ones = (1 << n) - 1  # bitmask with n lowest bits set to 1

    def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
        nonlocal count
        if row == n:
            count += 1
            return

        # available columns: bits that are not occupied by any of the three masks
        available = all_ones & ~(cols | diag1 | diag2)

        while available:
            # pick the lowest set bit as the column for the current row
            col_bit = available & -available
            available ^= col_bit  # remove this column from the available set

            # place queen and recurse to the next row
            backtrack(
                row + 1,
                cols | col_bit,
                ((diag1 | col_bit) << 1) & all_ones,
                ((diag2 | col_bit) >> 1) & all_ones,
            )

    backtrack(0, 0, 0, 0)
    return count


# Example usage
if __name__ == "__main__":
    for n in range(1, 16):
        print(f"n = {n}: {total_n_queens(n)} solutions")
