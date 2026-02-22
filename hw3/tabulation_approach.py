def howSum_tabu(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]
    return table[targetSum]


if __name__ == "__main__":
    test_cases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (300, [7, 14])]
    print("--- Testing Tabulation ---\n")
    for target, nums in test_cases:
        result = howSum_tabu(target, nums)
        res = result if result is not None else "null"
        print(f"howSum({target}, {nums}) -> {res}")
