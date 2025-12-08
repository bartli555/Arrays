names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

print("Names:", end=" ")
for name in names:
    print(name, end=" ")
print()

najdluzsze = ""

for name in names:
    if len(name) > len(najdluzsze):
        najdluzsze = name

print(f"Longest name: {najdluzsze}")        