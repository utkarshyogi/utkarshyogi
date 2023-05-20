def binary_search(list_numbers, target):
    left = 0
    right = len(list_numbers) - 1

    while left <= right:
        mid = int((left + right) / 2)
        if target == list_numbers[mid]:
            return target

        if target < list_numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binary_search([-1, 0, 1, 2, 3, 4], 2))

