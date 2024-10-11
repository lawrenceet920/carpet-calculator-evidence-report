# Ethan Lawrence
# Oct 11 2024
# Carpet Calculator Evidence report

# Input
length = float(input('Please enter the length of the room in feet (ex: 15):      '))
width = float(input('Please enter the width of the room in feet (ex: 20):      '))
cost_per_yard = float(input('Please enter the cost per yard of the carpet between $2.00 and $4.50 (do not include the "$" sign):      '))

STATE_TAX = 0.06

# Process
yards_needed = length * width / 3   # finds the area and converts to yards
subtotal = yards_needed * cost_per_yard     # Multiplys area by cost
tax = subtotal * STATE_TAX      # Finds sales tax
grand_total = tax + subtotal     # Adds sales tax

# Output
print(f' The area of the room is is {yards_needed:,.3f}')
print(f' The order subtotal is ${subtotal:,.2f}')
print(f' The order will be taxed for {tax:,.2f}')
print(f' The order grand total is ${grand_total:,.2f}')