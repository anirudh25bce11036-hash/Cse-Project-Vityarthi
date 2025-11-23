def brokerage_calculator():
 print("------ Brokerage & Profit/Loss Calculator ------\n")

# Taking inputs
buy_qty = int(input("Enter number of shares bought: "))
buy_price = float(input("Enter buy price per share: "))
sell_qty = int(input("Enter number of shares sold: "))
sell_price = float(input("Enter sell price per share: "))

# Calculations
total_buy = buy_qty * buy_price
total_sell = sell_qty * sell_price
gross_profit = total_sell - total_buy

turnover = total_buy + total_sell
brokerage = 0.0002 * turnover # 2% brokerage
other_charges = 10 # fixed charge

net_profit = gross_profit - (brokerage + other_charges)

# Results
print("\n----------- Results -----------")
print(f"Total Buy Value : ₹{total_buy:.2f}")
print(f"Total Sell Value : ₹{total_sell:.2f}")
print(f"Gross Profit/Loss : ₹{gross_profit:.2f}")
print(f"Turnover : ₹{turnover:.2f}")
print(f"Brokerage (2%) : ₹{brokerage:.2f}")
print(f"Other Charges : ₹{other_charges:.2f}")
print(f"Net Profit/Loss : ₹{net_profit:.2f}")
print("--------------------------------")

# Run the program
brokerage_calculator()