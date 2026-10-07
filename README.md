# pertemuan-06-nested-loop-2225250002

---

## Tujuan Repositori
Repositori ini dibuat untuk memenuhi tugas praktikum Pertemuan 6 mata kuliah Algoritma dan Pemrograman. Repositori ini berfokus pada penggunaan nested loop (perulangan bersarang), pola, akumulasi, dan pencacahan (counting) di Python.

---

## Algoritma Tugas 
1. **Loop Luar**: Mengontrol iterasi baris tabel perkalian atau iterasi utama sebanyak $n$ kali.
2. **Loop Dalam**: Mengontrol iterasi kolom di dalam setiap baris untuk menghasilkan pasangan nilai yang dikalikan.
3. **Akumulator**: Menyimpan dan menjumlahkan total keseluruhan hasil perhitungan dari seluruh iterasi bersarang.
4. **Counter**: Menghitung frekuensi atau jumlah kemunculan kondisi tertentu (seperti banyaknya hasil perkalian yang bernilai genap).

---

## Hasil Pengujian

| n | Jumlah pasangan | Total semua | Banyak hasil genap | Status |
| :-: | :-: | :-: | :-: | :-: |
| 1 | 1 | 1 | 0 | Sesuai |
| 2 | 4 | 9 | 3 | Sesuai |
| 3 | 9 | 36 | 5 | Sesuai |

---

## Cara Menjalankan
Buka terminal di direktori utama repositori ini, lalu jalankan program menggunakan perintah berikut:

```bash
python3 tabel_perkalian_dan_statistik.py.
```

---
## Refleksi
Kesalahan yang sempat ditemukan adalah penempatan inisialisasi variabel akumulator atau pencacahan yang keliru di dalam loop luar atau loop dalam, sehingga nilai total dan jumlah data genap tereset kembali ke nol pada setiap perpindahan baris baru. Masalah ini berhasil diatasi dengan menempatkan inisialisasi variabel akumulator dan di luar loop utama (sebelum loop luar dimulai) agar proses akumulasi data dari seluruh kombinasi pasangan iterasi dapat berjalan secara akurat dan berkesinambungan.
