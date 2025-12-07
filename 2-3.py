# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
suma_jedzenie = 0
suma_transport = 0
suma_media = 0

suma_tydzien1 = 0
suma_tydzien2 = 0
suma_tydzien3 = 0
suma_tydzien4 = 0

suma_calkowita = 0

for i, wydatki_tygodnia in enumerate(monthly_expenses):
    suma_jedzenie += wydatki_tygodnia[0]      # Kolumna 0: Jedzenie
    suma_transport += wydatki_tygodnia[1]     # Kolumna 1: Transport
    suma_media += wydatki_tygodnia[2]         # Kolumna 2: Media

    suma_tygodnia = sum(wydatki_tygodnia)

    if i == 0:
        suma_tydzien1 = suma_tygodnia
    elif i == 1:
        suma_tydzien2 = suma_tygodnia
    elif i == 2:
        suma_tydzien3 = suma_tygodnia
    elif i == 3:
        suma_tydzien4 = suma_tygodnia

        suma_calkowita += suma_tygodnia

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print(f'Food: {suma_jedzenie}')
print(f'Transport: {suma_transport}')
print(f'Utilities: {suma_media}')
print(f'Week 1: {suma_tydzien1}')
print(f'Week 2: {suma_tydzien2}')
print(f'Week 3: {suma_tydzien3}')
print(f'Week 4: {suma_tydzien4}')
print('---------------')
print(f'TOTAL: {suma_calkowita}')