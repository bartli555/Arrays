# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

laczna_wartosc = 0.0

liczba_produktow = len(product_prices)

for i in range(liczba_produktow):
    cena = product_prices[i]
    ilosc = product_quantities[i]
    wartosc = cena * ilosc
    laczna_wartosc += wartosc

print(f"Całkowita wartość wszystkich towarów: {laczna_wartosc:.2f}")