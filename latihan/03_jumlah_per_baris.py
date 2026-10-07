a = int(input("Masukan nilai a: "))
b = int(input("Masukan nilai b: "))
c = int(input("Masukan nilai c: "))
d = int(input("Masukan nilai d: "))

for i in range(a, b):
    total_baris = 0
    for j in range(c, d):
        total_baris += i * j
    print(f"Jumlah baris {i} = {total_baris}")