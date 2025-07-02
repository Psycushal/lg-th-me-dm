import sys
import yaml

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

def main():
    if len(sys.argv) != 2:
        print("Usage: python quicksort_config.py quicksort_config.yaml>")
        sys.exit(1)
    config_file = sys.argv[1]
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)
    arr = config.get('array', [])
    print(f"Original array: {arr}")
    sorted_arr = quicksort(arr)
    print(f"Sorted array: {sorted_arr}")

if __name__ == "__main__":
    main()
