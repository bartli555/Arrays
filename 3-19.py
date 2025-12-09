real_numbers = [1.5, 3.2, -4.0, 5.5, 0.0, 3.21, 10.5, -2.3]

print(f"Tablica: {real_numbers}")

try:
    threshold_str = input("Podaj wartość (liczbę rzeczywistą): ")
    threshold = float(threshold_str.replace(',', '.'))
    count = 0
    print(f"\nSzukam liczb większych od {threshold}...")
    for number in real_numbers:
        if number > threshold:
            count += 1
            
    print(f"Liczba elementów większych od {threshold}: {count}")

except ValueError:
    print("BŁĄD: Wprowadzono niepoprawną liczbę.")        