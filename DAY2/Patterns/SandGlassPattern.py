rows=4

# Upper part
for i in range(1,rows+1):
    #print space
    for j in range(i-1):
        print(" ",end="")
    #print stars
    for j in range(2*(rows-i)+1):
        print("*",end="")

    print()


# Lower part
for i in range(rows,0,-1):
    #print space
    for j in range(i-1):
        print(" ",end="")

    #print stars
    for j in range(2*(rows-i)+1):
        print("*",end="")

    print()