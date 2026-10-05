# Loop luar mengatur baris dari 1 sampai 4.
# Loop dalam menghitung hasil perkalian i dan j.
# Accumulator digunakan untuk menjumlahkan hasil pada setiap baris.
# Output menampilkan jumlah hasil perkalian setiap baris.

for i in range(1, 5):
    total_baris = 0

    for j in range(1, 4):
        total_baris += i * j

    print(f"Jumlah baris {i} = {total_baris}")