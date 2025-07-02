import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <current_year> <birth_year>")
    sys.exit(1)

current_year = int(sys.argv[1])
birth_year = int(sys.argv[2])

age = current_year - birth_year
print(f"You are {age} years old")

if age >= 18:
    print("Can drink :)))")
else:
    print("MINOR")
