name = input("Enter the name: ")

mid = len(name) // 2

firsthalf = name[:mid]
secondhalf = name[mid:]

firstHalfRev = firsthalf[::-1]
secondHalfRev = secondhalf[::-1]
result = firstHalfRev + secondHalfRev

print("Output:", result)