# Jurnal Proses — Tugas 3

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: Pada percobaan pertama, hasil yang didapatkan sama seperti saat menggunakan lock, yaitu 100. Hal tersebut terjadi karena proses thread yang berjalan cukup cepat sehingga tidak terjadi race condition. 
- Hasil `processed_count` yang didapat: Kemudian pada percobaan kedua, hasil yang didapatkan adalah 60 dan 51 yang seharusnya adalah 100. Hal tersebut terjadi karena kami menambahkan sleep time pada percobaan kedua yang membuat race condition dapat terjadi. 
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): karena pada percobaan kedua, kami menambahkan sleep time pada proses thread sehingga race condition dapat terjadi, yang menyebabkan pada percobaan pertama tidak terjadi race condition karena proses yang berjalan terlalu cepat. Race condition terjadi karena thread beberapa thread mengakses dan mengubah data yang sama secara bersamaan, hal tersebut membuat hasilnya meleset karena thread saling berebutan untuk mengubah data.  

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: ...

## Kendala Docker
- Bethari Nevyta Amaries : Docker desktop gagal start dan menunjukan pesan error "Virtualization support not detected". Solusi yang dilakukan adalah mengaktifkan fitur WSL dan VM platform melalui PowerShell. 
- Bethari Nevyta Amaries : Saat membuka docker desktop muncul prompt update WSL. Solusi yang dilakukan update melalui PowerShell kemudian restart laptop. 
- Bethari Nevyta Amaries : Dockerr pakai WSL2 backend, jadi pengaturan batas RAM tidak tersedia. Solusinya melakukan konfigurasi manual dengan file ".wslconfig".
- Error yang ditemui saat `docker build`/`docker run` dan cara memperbaikinya: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
