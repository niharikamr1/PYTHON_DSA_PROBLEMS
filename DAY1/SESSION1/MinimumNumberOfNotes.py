# Minimum Number of Notes - Greedy Algorithm

amount = int(input("Enter amount: "))
notes = [100, 50, 20, 10, 2, 1]

total_notes = 0

for note in notes:
    count = amount // note

    if count:
        print(f"{note} : {count}")
        total_notes += count

    amount %= note

print("Minimum notes =", total_notes)