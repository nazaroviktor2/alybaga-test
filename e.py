def closeness(arr1: list[int], arr2: list[int]) -> int:
    """Считает близость двух массивов."""
    min_length = min(len(arr1), len(arr2))
    for i in range(min_length):
        if arr1[i] != arr2[i]:
            return i
    return min_length


def calculate_closeness(arrays: list[list[int]]) -> int:
    """Считает общую близость нескольких массивов."""
    sum_closeness = 0
    n = len(arrays)
    for i in range(n):
        for j in range(i + 1, n):
            sum_closeness += closeness(arrays[i], arrays[j])

    return sum_closeness


if __name__ == '__main__':
    n = int(input())
    arrays = []
    for _ in range(n):
        _ = input()
        arr = list(map(int, input().split()))
        arrays.append(arr)

    print(calculate_closeness(arrays))
