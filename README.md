# Pertemuan 06 Nested Loop Python

Nama: Zahra Amelia  
NIM: 2225250044  
Kelas: S1 Pendidikan Matematika

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan

Jalankan program dengan perintah:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

- **Loop luar** digunakan untuk mengatur baris tabel dari 1 sampai n.
- **Loop dalam** digunakan untuk mengatur kolom tabel dari 1 sampai n.
- **Accumulator** `total_baris` digunakan untuk menjumlahkan hasil pada setiap baris, sedangkan `total_semua` digunakan untuk menjumlahkan seluruh hasil perkalian.
- **Counter** `count_genap` digunakan untuk menghitung banyak hasil perkalian yang genap.

## Hasil Pengujian

| Input | Jumlah Pasangan | Hasil yang Diharapkan | Keluaran Aktual | Status |
|---|---:|---|---|---|
| n = 1 | 1 | Total = 1, hasil genap = 0 | Total = 1, hasil genap = 0 | Berhasil |
| n = 2 | 4 | Total = 9, hasil genap = 3 | Total = 9, hasil genap = 3 | Berhasil |
| n = 3 | 9 | Total = 36, hasil genap = 5 | Total = 36, hasil genap = 5 | Berhasil |

## Analisis Efisiensi

Untuk input n, loop luar berjalan sebanyak n kali. Pada setiap iterasi loop luar, loop dalam juga berjalan sebanyak n kali. Jadi, badan loop dalam berjalan sebanyak:

n × n = n² kali.

## Refleksi

Kesalahan yang perlu diperhatikan pada nested loop adalah salah menempatkan inisialisasi `total_baris`. Jika `total_baris = 0` diletakkan di dalam loop dalam, jumlah setiap baris akan selalu direset sehingga hasilnya salah.

Perbaikannya adalah meletakkan `total_baris = 0` di awal setiap iterasi loop luar, sebelum loop dalam dimulai.