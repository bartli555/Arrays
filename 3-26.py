import matplotlib.pyplot as plt
import math

x_stopnie = []
y_wartosci = []

for kat in range(0, 361):
    x_stopnie.append(kat)

    radiany = math.radians(kat)
    y = math.sin(radiany)

    y_wartosci.append(y)

plt.plot(x_stopnie, y_wartosci)
plt.title("Wykres funkcji y = sin(x)")
plt.xlabel("Kąt (stopnie)")
plt.ylabel("sin(x)")
plt.grid(True)

plt.show()