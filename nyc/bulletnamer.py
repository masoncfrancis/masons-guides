bullets = ['4', '5', '6', 'A', 'B', 'C', 'D']

for x in bullets:
    lowercase = x.lower()
    print(f"![{x} train](img/{lowercase}.png), ", end='')