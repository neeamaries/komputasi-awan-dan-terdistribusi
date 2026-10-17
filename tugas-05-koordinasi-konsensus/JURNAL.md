# Jurnal Proses — Tugas 5

## Implementasi Bully
- Kendala saat mengisi TODO 1-2 : Kendala yang dihadapi saat mengisi TODO 1 dan 2 adalah dalam memahami alur pengiriman pesan dan memastikan bahwa setiap node dapat menentukan leader berdasarkan ID tertinggi yang masih aktif. Selain itu, diperlukan juga pengujian berulang agar hasil dapat berjalan sesuai skenario yang diinginkan ketika leader berhenti. 
- Kendala saat mengisi TODO 3-4 : Pada TODO 3, kendalanya adalah memastikan `COORDINATOR` dikirim ke seluruh node, bukan hanya node yang lebih besar, dan tetap berjalan meskipun ada node yang sudah mati. Pada TODO 4, kendalanya adalah menentukan kapan pemilihan baru perlu dimulai agar tidak muncul pemilihan yang tidak perlu. Selain itu, pemilihan yang berjalan bersamaan membuat pesan `ELECTION` dan `COORDINATOR` terkirim berulang sehingga log sulit dibaca.

## Skenario 1: Start normal
- Leader yang terpilih: Node 5 
- Log/observasi: Saat kelima node dijalankan secara bersamaan, node dengan ID yang lebih rendah akan mengirimkan pesan election ke node yang lebih tinggi. Kemudian node yang lebih tinggi dan masih aktif akan merespons dengan pesan OK untuk menandakan bahwa mereka masih aktif dan dapat menjadi leader. Kemudian proses ini berlanjut sehingga node dengan ID 5 terpilih menjadi leader karena merupakan ID tertinggi. Kemudian, node 5 akan mengirimkan pesan coordinator ke seluruh node untuk memberitahukan bahwa dia adalah leader baru. 

## Skenario 2: Leader dimatikan
- Leader baru yang terpilih: Node 4 
- Berapa lama waktu sampai leader baru terdeteksi: 3 - 5 detik 
- Log/observasi: Saat node 5 dihentikan, node lain akan mendeteksi bahwa leader tidak lagi merespons. Kemudian node dengan ID yang lebih rendah akan memulai proses election kembali, proses akan berjalan kembali hingga node 4 terpilih menjadi leader baru karena merupakan node dengan ID yang tertinggi dan masih aktif. Setelah terpilih, node 4 akan mengirimkan pesan coordinator ke seluruh node untuk memberitahukan bahwa dia adalah leader baru. 


## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 15 Oktober 2026 | ChatGPT | Membantu memahami TODO 1–4 pada implementasi Bully Algorithm | Menjelaskan fungsi pesan ELECTION, OK, dan COORDINATOR, serta proses pemilihan leader berdasarkan ID node tertinggi yang masih aktif. | Menggunakan penjelasan untuk memahami alur algoritma, kemudian menerapkannya pada bagian TODO di kode yang telah disediakan. |
| 16 Oktober 2026 | Gemini | Jelaskan perbandingan antara Bully Algorithm dan Raft consensus algorithm secara konsep, terutama kelebihan dan kelemahannya untuk laporan sistem terdistribusi | Menjelaskan perbedaan mekanisme pemilihan, penanganan split-brain, efisiensi pesan, dan alasan mengapa Raft lebih modern serta aman untuk produksi dibanding Bully. | Menyusun ulang poin-poin penjelasan tersebut untuk mengisi sub-bab analisis perbandingan algoritma pada laporan. |
