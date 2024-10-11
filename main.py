# Ethan Lawrence
# Oct 11 2024
# Carpet Calculator Evidence report

# Input
length = float(input('Please enter the length of the room in feet (ex: 23):      '))
width = float(input('Please enter the width of the room in feet (ex: 26):      '))
cost_per_yard = float(input('Please enter the cost per yard of the carpet between $2.00 and $4.50 (do not include the "$" sign):      '))
STATE_TAX = 0.06

# Process
yards_needed = length * width / 3   # finds the area and converts to yards
subtotal = yards_needed * cost_per_yard     # Multiplys area by cost
grand_total = (subtotal * STATE_TAX) + subtotal     # Adds sales tax

# Output
print(f'This room has an area of {yards_needed:,.3f}yd\u00b2. The subtotal is ${subtotal:,.2f}, Including salestax you will have to pay ${grand_total:,.2f}')