def merge_optimized(A, m, n):
    # if either subarray size is 0 then we already the sorted array A
    if m == 0 or n == 0:
        return A

    if m <= n:
        # if left subarray size(m) < right subarray size(n)
        # auxiliary array size = m
        aux = A[:m]
        i, j, k = 0, m, 0
        while i < m and j < m + n:
            if aux[i] <= A[j]:
                A[k] = aux[i]
                i += 1
            else:
                A[k] = A[j]
                j += 1
            k += 1
        # i am copying the remaining elements from auxiliary
        while i < m:
            A[k] = aux[i]
            i += 1
            k += 1

    else:
        # if left subarray size(m) > right subarray size(n)
        # auxiliary array size =n
        aux = A[m : m + n]
        i, j, k = n - 1, m - 1, m + n - 1
        while i >= 0 and j >= 0:
            if aux[i] >= A[j]:
                A[k] = aux[i]
                i -= 1
            else:
                A[k] = A[j]
                j -= 1
            k -= 1
        # copying remaining elements from auxiliary
        while i >= 0:
            A[k] = aux[i]
            i -= 1
            k -= 1

    return A


test_cases_p1 = [
    (0, 3, [3,7,9]),
    (3, 1, [2, 7, 9, 1]),
    (4, 4, [1, 7, 10, 15, 3, 8, 12, 18]),
    (7,12, [1, 3, 5, 5, 15, 18, 21, 5, 5, 6, 8, 10, 12, 16, 17, 17, 20, 25, 28])
]

print("--- Problem 1 Results ---")
for idx, (m, n, A) in enumerate(test_cases_p1):
    original = list(A)
    merged = merge_optimized(A, m, n)
    print(f"Test Case {idx+1}: \n  Original: {original}\n  Merged:   {merged}\n")