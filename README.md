# Pertemuan 06 Nested Loop Python

**Nama:** Zahra Amelia  
**NIM:** 2225250044  
**Kelas:** S1 Pendidikan Matematika

## Tujuan

- Memahami penggunaan nested loop dalam Python.
- Membuat pola menggunakan nested loop.
- Menggunakan accumulator dan counter dalam program.
- Menghitung dan menampilkan hasil dari perulangan bersarang.

## Cara Menjalankan Program

Jalankan program dengan perintah:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```
## Algoritma Tugas 3

1. Input bilangan bulat positif `n`.
2. Jika `n <= 0`, program meminta input ulang sampai `n` bernilai positif.
3. Inisialisasi `total_semua = 0` dan `count_genap = 0`.
4. Gunakan loop luar untuk mengatur baris `i` dari 1 sampai `n`.
5. Pada setiap baris, inisialisasi `total_baris = 0`.
6. Gunakan loop dalam untuk mengatur kolom `j` dari 1 sampai `n`.
7. Hitung `hasil = i * j`.
8. Tambahkan `hasil` ke `total_baris` dan `total_semua`.
9. Jika `hasil` genap, tambahkan `count_genap` sebanyak 1.
10. Tampilkan jumlah setiap baris.
11. Setelah semua perulangan selesai, tampilkan total seluruh hasil dan banyak hasil genap.

## Testing

| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| n = 1 | Total = 1, hasil genap = 0 | Total = 1, hasil genap = 0 | Berhasil |
| n = 2 | Total = 9, hasil genap = 3 | Total = 9, hasil genap = 3 | Berhasil |
| n = 3 | Total = 36, hasil genap = 5 | Total = 36, hasil genap = 5 | Berhasil |

## Efisiensi

Program menggunakan nested loop dengan kompleksitas waktu O(n²) karena terdapat dua perulangan yang masing-masing berjalan sebanyak n kali.

## Refleksi

Nested loop digunakan untuk membuat tabel perkalian karena membutuhkan perulangan baris dan kolom. 
Accumulator digunakan untuk menghitung jumlah hasil pada setiap baris dan total seluruh hasil. 
Counter digunakan untuk menghitung banyak hasil perkalian yang genap.