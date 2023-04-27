import sys

print("Print values")


print("Print", "values", "with", "separator", sep=" | ")


print("Print", end=" ")
print("on the same line")


err = "File not found"
print(f"Error: {err}", file=sys.stderr)
