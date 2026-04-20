# Electricity Bill Calculator using slab rates

units = int(input("Enter units consumed: "))

# Calculate bill based on unit slabs
if units <= 100:
    bill = units * 1.50

elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50

else:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

print(f"Electricity Bill = Rs {bill:.2f}")