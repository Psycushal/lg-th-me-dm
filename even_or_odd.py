import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

number = int(sys.argv[1])

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
