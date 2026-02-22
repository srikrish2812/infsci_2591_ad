"""
Write a function ‘howSum(targetSum, numbers)’ that takes in a targetSum and an array of numbers as arguments. The function should return an array containing any valid combination of elements that adds up to the targetSum. You can use the elements as many times as needed. It should return null if there is no combination found. If there are multiple combinations available, you may return any one of them.

You should use both memoization and tabulation method, respectively, to optimize your algorithm. Test the following cases:

(7, [2,3])
(7, [5,3,4,7])
(300,[7,14])
"""


def howSum_memo(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}

    # checking if it is already there in memo
    if targetSum in memo:
        return memo[targetSum]

    # checking for base cases
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        rem_res = howSum_memo(remainder, numbers, memo)

        if rem_res is not None:
            memo[targetSum] = rem_res + [num]
            return memo[targetSum]
    memo[targetSum] = None
    return None


if __name__ == "__main__":
    test_cases = [(7, [2, 3]), (7, [5, 3, 4, 7]), (300, [7, 14])]

    print("--- Testing Memoization Appraoch ---\n")
    for target, nums in test_cases:
        result = howSum_memo(target, nums)
        res = result if result is not None else "null"
        print(f"howSum({target}, {nums}) -> {res}")
