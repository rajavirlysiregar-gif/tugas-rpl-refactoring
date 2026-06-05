# Tugas Konstruksi Perangkat Lunak: Refactoring & Coding Standards

**Nama:** [Raja Virly Fadhillah Siregar]  
**NIM:** [241112409]  

## 1. Coding Standards yang Digunakan
Proyek ini mengadopsi standar kode **PEP 8** untuk bahasa pemrograman Python, dengan fokus pada:
* Penamaan variabel menggunakan `snake_case`.
* Penggunaan konstanta dengan huruf kapital (`UPPER_CASE`).
* Dokumentasi fungsi yang jelas.

## 2. Identifikasi Code Smells Sebelum Refactoring
Pada commit awal, ditemukan beberapa permasalahan pada file `main.py`:
* **Long Method / Bloated Function:** Fungsi `hitung()` melakukan terlalu banyak kalkulasi sekaligus.
* **Bad Naming:** Nama variabel seperti `q`, `p`, dan `tot` tidak deskriptif.
* **Magic Numbers:** Penggunaan angka desimal langsung (`0.1` dan `0.11`) tanpa kejelasan konteks bisnisnya.

## 3. Teknik Refactoring yang Diterapkan
Perbaikan dilakukan secara bertahap melalui riwayat commit:
1. **Rename Variables & Functions:** Mengubah nama fungsi dan variabel agar lebih mudah dibaca (*self-documenting code*).
2. **Replace Magic Number with Constant:** Memindahkan angka persentase diskon dan pajak ke variabel konstanta global.
3. **Extract Method:** Memecah fungsi utama menjadi fungsi-fungsi kecil (`apply_discount` dan `apply_tax`).