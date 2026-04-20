item = input("Enter item name for product:")
quantity = int(input("Enter the quantity of the product:"))
price = float(input("Enter the price of per product:"))
member = bool(int(input("Enter 1 for member and 0 for non-member:")))

subtotal = quantity * price 

discount = subtotal * 0.10 if member else 0   
amount = subtotal - discount   

gst_rate = 0.05 if amount > 500 else 0.12   
gst = amount * gst_rate  

total = amount + gst   

print(f"Item = {item}")
print(f"Subtotal = Rs {subtotal:.2f}") 
print(f"Discount = Rs {discount:.2f}")
print(f"GST = Rs {gst:.2f}")
print(f"Final Total = Rs {total:.2f}")  