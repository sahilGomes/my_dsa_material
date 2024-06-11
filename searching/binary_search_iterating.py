def binary_search(list_to_search:list[int],number_to_find:int) -> bool:
    length_of_list_to_search:int = len(list_to_search)
    low:int = 0
    high:int = length_of_list_to_search-1
    mid:int = length_of_list_to_search // 2
    result:bool = False
    while True:
        if list_to_search[mid] == number_to_find:
            result = True
            break
        elif low == high:
            break
        if number_to_find < list_to_search[mid]:
            high = mid-1
            if high == -1:
                high = 0 if high == -1 else high
        else:
            low = mid + 1
        mid = ((high-low)//2) + low
    return result

while True:
    number_to_search:int = int(input("Enter number to Search:"))
    if number_to_search == -1:
        break
    else:
        print(binary_search([12,34,56,58,83],number_to_search))