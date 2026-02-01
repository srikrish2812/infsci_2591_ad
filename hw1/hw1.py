"""
Write an algorithm that prints out all the subsets of three elements of a set of n elements.
The elements of this set are stored in a list that is the input to the algorithm.

Test Case 1 = {1, 2, 3, 4},
Test Case 2 = {7, 3},
Test Case 3 = {4, 1, 7, 4, 3, 9, 1, 5}.

Do not remove the duplicates as they are different elements although they have the same value.
"""


def print_subsets(s):
    n = len(s)
    print(f"For Test Case {s}")

    if n < 3:
        print("Cannot print subsets of 3 if input data size less than 3")
        print("Total subsets = 0\n\n")
        return

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                print([s[i], s[j], s[k]])
                count += 1

    print(f"Total subsets found = {count}\n\n")


if __name__ == "__main__":
    print_subsets([1, 2, 3, 4])
    print_subsets([7, 3])
    print_subsets([4, 1, 7, 4, 3, 9, 1, 5])
