def binary_search(
    list_to_search_from: list[int], number_to_search: int, low: int, high: int
) -> bool:
    mid: int = (high - low) // 2 + low

    # base condition
    if list_to_search_from[mid] == number_to_search:
        return True
    elif low == high:
        return False

    # recurrsion
    new_high: int = high
    new_low: int = low
    if number_to_search < list_to_search_from[mid]:
        if mid - 1 == -1:
            new_high = 0
        else:
            new_high: int = mid - 1
    else:
        new_low: int = mid + 1
    result: bool = binary_search(
        list_to_search_from, number_to_search, new_low, new_high
    )
    return result


while True:
    number_to_search: int = int(input("Enter number to Search:"))
    if number_to_search == -1:
        break
    else:
        print(
            binary_search(
                [12, 34, 56, 58, 83, 89, 101, 201, 220, 432, 521],
                number_to_search,
                0,
                10,
            )
        )
