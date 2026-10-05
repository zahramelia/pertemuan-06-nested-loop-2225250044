# Loop luar mengatur baris tabel perkalian.
# Loop dalam mengatur kolom tabel perkalian.
# total_baris digunakan untuk menjumlahkan hasil pada setiap baris.
# total_semua digunakan untuk menjumlahkan seluruh hasil perkalian.
# count_genap digunakan untuk menghitung banyak hasil yang genap.
# Kondisi if mengecek apakah hasil perkalian merupakan bilangan genap.
# Output menampilkan tabel, jumlah setiap baris, total seluruh hasil,
# dan banyak hasil genap.

print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print(f" | jumlah baris = {total_baris}")

print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")