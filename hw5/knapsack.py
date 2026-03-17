def knapsack_01(values, weights, capacity):
    """

    values : list
        List of item values (v_i)
    weights : list
        List of item weights (w_i)
    capacity : int
        Maximum weight capacity of knapsack (W)
    """
    n = len(values)

    # Step 1: Initialize DP table with zeros
    # K[i][c] = max value using first i items with capacity c
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Step 2: Fill the DP table row by row
    for i in range(1, n + 1):
        current_value = values[i - 1]  # v_i
        current_weight = weights[i - 1]  # w_i

        for c in range(1, capacity + 1):
            # Case 1: Don't take item i
            dp[i][c] = dp[i - 1][c]

            # Case 2: Take item i if it fits
            if current_weight <= c:
                value_if_take = dp[i - 1][c - current_weight] + current_value
                if value_if_take > dp[i][c]:
                    dp[i][c] = value_if_take

    # Step 3: Maximum value is in bottom-right cell
    max_value = dp[n][capacity]

    # Step 4: Trace back to find which items were selected
    selected_items = []
    remaining_capacity = capacity

    for i in range(n, 0, -1):
        # If value changed, item i was taken
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            selected_items.append(i - 1)
            remaining_capacity -= weights[i - 1]

    # Reverse to get items in original order
    selected_items.reverse()

    return max_value, selected_items, dp


if __name__ == "__main__":
    value, items, dp = knapsack_01([60, 100, 120], [10, 20, 30], 50)
    print(f"Knapsack Value = {value}")
    print(f"Selected Items = {items}")
