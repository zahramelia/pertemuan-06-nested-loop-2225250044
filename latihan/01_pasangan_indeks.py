# Loop luar mengatur nilai i dari 1 sampai 3.
# Loop dalam mengatur nilai j dari 1 sampai 4.
# Counter digunakan untuk menghitung banyak pasangan yang ditampilkan.
# Tidak ada kondisi if pada latihan ini.
# Output menampilkan setiap pasangan (i, j) dan jumlah seluruh pasangan.

count = 0

for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")