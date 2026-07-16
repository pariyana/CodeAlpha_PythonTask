stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 200
}

name = input("Enter stock name: ").upper()
qty = int(input("Enter quantity: "))

if name in stocks:
    total = stocks[name] * qty
    print("Total Investment =", total)
else:
    print("Stock not found")