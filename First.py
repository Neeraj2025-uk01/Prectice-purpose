height = int(input("Enter height of tree: "))

# Tree foliage
for row in range(height):
    # Print leading spaces
    print(" " * (height - row), end="")
    # Print stars
    print("*" * (2 * row + 1))

# Tree trunk
# The number of spaces for the trunk is the same as the top of the tree
for _ in range(height // 3 + 1):
    print(" " * (height), end="")
    print("|")

print("Hello, World!")