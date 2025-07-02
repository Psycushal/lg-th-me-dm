import sys

if len(sys.argv) != 4:
    print("Usage: python script.py <num1> <num2> <num3>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

smallest = min(a, b, c)
print(f"The smallest number is: {smallest}")
