def linear_sort(arr):
    n = len(arr)
    aux_arr = [0] * n
    for i in range(n):
        aux_arr[arr[i] - 1] = arr[i]

    for i in range(n):
        arr[i] = aux_arr[i]
    return arr


if __name__ == "__main__":
    print(linear_sort(arr=[6, 4, 5, 1, 2, 3]))
