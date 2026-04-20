piles = [3,6,7,11]
h = 8

left = 1
right = max(piles)

while left <= right:

    # check middle speed
    mid = (left + right) // 2

    total_hours = 0

    # find hours needed at this speed
    for pile in piles:
        total_hours += (pile + mid - 1) // mid

    # if possible in h hours, try smaller speed
    if total_hours <= h:
        right = mid - 1

    # otherwise increase speed
    else:
        left = mid + 1

# left will be minimum valid speed
print(left)