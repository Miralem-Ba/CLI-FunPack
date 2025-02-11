start_price = 6.80                          # Variable definiert
km = int(input("Kilometer eingeben: "))     # Variable Commando Line
if km > 5:
    costs = 3.10
else:
    costs = 3.90 
total = start_price + costs * km            # Variable gesamtkosten
print("Kosten Taxifahrt", total)            
