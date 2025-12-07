# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for row in seats:
      total += len(row) # Dodajemy długość każdego rzędu
   return total

def seats_available(seats):
   available = 0
   for row in seats:
      # Metoda .count() zlicza wystąpienia elementu w liście
      available += row.count('A')
   return available

def seats_booked(seats):
   booked = 0
   for row in seats:
      booked += row.count('B')
   return booked

def seat_status(seats, row, place):
   status_code = seats[row - 1][place - 1]

   if status_code == 'A':
      return "Available" #(Dostępne)
   else:
      return "Booked" #(Zarezerwowane)

print('CINEMA INFORMATION TABLE')
print(f'Total seats: {seats_total(cinema_seats)}')
print(f'Seats available: {seats_available(cinema_seats)}')
print(f'Seats booked: {seats_booked(cinema_seats)}')
print(f'Seat in row 1, place 1: {seat_status(cinema_seats, 1, 1)}')
print(f'Seat in row 5, place 5: {seat_status(cinema_seats, 5, 5)}')
print(f'Seat in row 3, place 5: {seat_status(cinema_seats, 3, 5)}')