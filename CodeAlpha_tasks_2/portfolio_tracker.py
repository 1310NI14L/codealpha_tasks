import  csv

print("         ___Stock Portfolio Tracker___")
print("\n The Goat is of  Build a simple stock tracker that calculates total investment based on manually defined stock prices.\n")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 350,
    "NVDA": 120,
    "MSFT": 420
}

portfolio = {}
stop_input = True

print("___ Grab of your portfolio (Enter 'end' for stop writing) ___")

while stop_input:
    names = input("Enter the name of action : ").strip().upper()

    if names == "END" or names == "":
        break

    if names not in stock_prices:
        print(f"Warning : '{names}' is not listed in our stock prices. Please enter a valid stock.\n")
        continue

    quantity = int(input(f"Enter the quantity for {names} : "))
    print("")

    if names in portfolio:
        portfolio[names] += quantity
    else:
        portfolio[names] = quantity

total_investment = 0

print("\n   ___ Report of Portfolio Automatic Tracker ___ ")
for names, quantity in portfolio.items():
    price = stock_prices[names]
    subtotal = quantity * price

    total_investment += subtotal

    print(f" {names} : {quantity} * {price}$ = {subtotal}")

print("\n______________________________________")
print(f"Total Investment: {total_investment} $")
print("________________________________________")

filename = "saved_fileCSV/portfolio_CodeAlpha.csv"

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    writer.writerow(["Action Name", "Quantity Action", "Unit Price ($)", "Total Values ($)"])

    for names, quantity in portfolio.items():
        price = stock_prices[names]
        subtotal = quantity * price
        writer.writerow([names, quantity, price, subtotal])

    writer.writerow([])
    writer.writerow(["Total Investment ($)", "", "", f"{total_investment}"])

print(f"\n Portfolio automatically saved in '{filename}'!")