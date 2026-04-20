#Diamond pattern
rows = 4

#Upper pattern
for i in range(1, rows+1):
    #print space
    for j in range(rows-i):
        print(" ", end=" ")
    #print stars
    for j in range(2*i-1):
        print("*",end=" ")
    print()

#Lower pattern
for i in range(rows-1,0,-1):

    #print spaces
    for j in range(rows-i):
        print(" ", end=" ")

    #print stars
    for j in range(2*i-1):
        print("*",end=" ")
    print()

    
