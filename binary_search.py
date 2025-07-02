import sys

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        left, right = (mid + 1, right) if arr[mid] < target else (left, mid - 1)
    return -1

def get_input():
    try:
        if len(sys.argv) >= 3:
            size = int(sys.argv[1])
            if len(sys.argv) < size + 3:
                raise ValueError(f"Expected {size} elements plus target, got {len(sys.argv) - 2}")
            arr = list(map(int, sys.argv[2:2 + size]))
            target = int(sys.argv[2 + size])
        else:
            size = int(input("Array size: "))
            arr = [int(input(f"Element {i+1}: ")) for i in range(size)]
            target = int(input("Target: "))
        return arr, target
    except (ValueError, EOFError):
        arr, target = [1, 3, 5, 7, 9, 11, 13], 7
        print(f"Using default array: {arr}, target: {target}")
        return arr, target

if __name__ == "__main__":
    print("BINARY SEARCH PROGRAM\n" + "="*30)
    arr, target = get_input()
    original = arr[:]
    arr.sort()
    if arr != original:
        print(f"Original: {original}\nSorted: {arr}")
    idx = binary_search(arr, target)
    print(f"{' Found' if idx != -1 else '✗ Not found'} {target}{f' at index {idx}' if idx != -1 else ''}")