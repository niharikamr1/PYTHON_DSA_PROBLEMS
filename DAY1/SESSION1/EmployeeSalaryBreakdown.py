# Employee Salary Breakdown
basic_salary = float(input("Enter the salary:"))

hra= basic_salary * 0.20
da= basic_salary * 0.50

#Earnings
gross_salary = basic_salary + hra +da

#Deductions
pf= basic_salary * 0.12
tax= gross_salary * 0.10
total_deductions= pf + tax

#Net Salary
net_salary=gross_salary - total_deductions
print(f"Gross Salary:{gross_salary:.2f}")
print(f"Total Deductions:{total_deductions:.2f}")
print(f"Net Salary is: {net_salary:.2f}")





