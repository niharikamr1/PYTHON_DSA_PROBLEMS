rows = 4

# Upper half
for i in range(1, rows+1):

    for j in range(i):
        print("*", end="")

    for j in range(2*(rows-i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()


# Lower half (start from rows, not rows-1)
for i in range(rows, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(2*(rows-i)):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()