# Jurnal Proses — Tugas 3

## [2 Oktober 2026] 
- Bethari Nevyta Amaries mengomentari analisis A'ilah Nailul Fa'izah : menurut pendapat saya, tambahkan alasan kenapa percobaan menggunakan lock memberikan hasil yang konsisten . 

## Percobaan tanpa Lock
- Hasil `processed_count` yang didapat: Pada percobaan pertama, hasil yang didapatkan sama seperti saat menggunakan lock, yaitu 100. Hal tersebut terjadi karena proses thread yang berjalan cukup cepat sehingga tidak terjadi race condition. 
- Hasil `processed_count` yang didapat: Kemudian pada percobaan kedua, hasil yang didapatkan adalah 60 dan 51 yang seharusnya adalah 100. Hal tersebut terjadi karena kami menambahkan sleep time pada percobaan kedua yang membuat race condition dapat terjadi. 
- Kenapa bisa meleset (jelaskan mekanisme race condition dengan kata sendiri): karena pada percobaan kedua, kami menambahkan sleep time pada proses thread sehingga race condition dapat terjadi, yang menyebabkan pada percobaan pertama tidak terjadi race condition karena proses yang berjalan terlalu cepat. Race condition terjadi karena thread beberapa thread mengakses dan mengubah data yang sama secara bersamaan, hal tersebut membuat hasilnya meleset karena thread saling berebutan untuk mengubah data.  

## Percobaan dengan Lock
- Hasil `processed_count` setelah perbaikan: Setelah melakukan percobaan dengan lock, hasil yang di dapatkan pada setiap percobaan adalah 100, ini merupakan hasil yang konsisten. Berbeda dengan percobaan tanpa lock yang hasilnya berubah-ubah.
- Kenapa hasilnya konsisten : Lock membuat proses `processed_count += 1` yang hanya bisa dikerjakan oleh satu thread dalam satu waktu. Saat satu thread sedang masuk ke bagian `with lock:`, thread lain yang ingin mengakses `processed_count` dipaksa menunggu sampai thread pertama selesai dan melepas lock-nya, sehingga tidak ada dua thread yang membaca nilai yang sama secara bersamaan dan setiap increment benar-benar dihitung satu persatu tanpa ada yang saling menimpa.

## Kendala Docker
- Bethari Nevyta Amaries : Docker desktop gagal start dan menunjukan pesan error "Virtualization support not detected". Solusi yang dilakukan adalah mengaktifkan fitur WSL dan VM platform melalui PowerShell. 
- Bethari Nevyta Amaries : Saat membuka docker desktop muncul prompt update WSL. Solusi yang dilakukan update melalui PowerShell kemudian restart laptop. 
- Bethari Nevyta Amaries : Dockerr pakai WSL2 backend, jadi pengaturan batas RAM tidak tersedia. Solusinya melakukan konfigurasi manual dengan file ".wslconfig".
- A'ilah Nailul Fa'izah : Docker Desktop juga gagal start dengan error "Virtualization support not detected" karena virtualisasi belum aktif. Solusi yang dilakukan adalah mengaktifkan fitur Virtual Machine Platform dan Windows Hypervisor Platform.


## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 30 September 2026 | Claude | Menanyakan fungsi threading.Lock serta perbandingan keunggulan dan kekurangan menggunakan lock dibanding tanpa lock | AI menjelaskan konsep dasar cara kerja Lock seperti mekanisme acquire/release, critical section dan poin-poin trade-off performa vs konsistensi data secara umum | Membandingkan penjelasan konsep ini dengan hasil percobaan yang kami jalankan sendiri |
| 30 September 2026 | Claude | Menanyakan solusi error Docker Desktop "Virtualization support not detected" | AI menyarankan langkah umum: cek status virtualisasi di Task Manager, aktifkan fitur Hyper-V/Virtual Machine Platform lewat PowerShell, dan update WSL2 | Mempraktikkan langkah-langkah ini di laptop sendiri |
| 30 September 2026 | Claude | Menanyakan konsep dasar Docker, container, image, dan Dockerfile | AI menjelaskan analogi container dan konsep umum kenapa Docker dipakai untuk portabilitas | Konsep dipakai sebagai pengetahuan awal sebelum mengisi TODO |
| 30 September 2026 | Claude | Menanyakan cara mengatasi error "Virtualization support not detected" dan konfigurasi WSL2/RAM di Docker Desktop | AI menjelaskan langkah teknis mengaktifkan fitur WSL2 lewat DISM, update WSL, dan cara membuat file `.wslconfig` untuk membatasi RAM | Langkah dipraktikkan langsung untuk memperbaiki error |
| ... | ... | ... | ... | ... |

