vehicles = int(input("Enter total vehicles: "))
wheels = int(input("Enter total wheels: "))

four_wheelers = (wheels - 2 * vehicles) // 2
two_wheelers = vehicles - four_wheelers

if wheels < 2 * vehicles or wheels > 4 * vehicles or wheels % 2 != 0:
    print("No valid solution")
else:
    print("2-wheelers =", two_wheelers)
    print("4-wheelers =", four_wheelers)