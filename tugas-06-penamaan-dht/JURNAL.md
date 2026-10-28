# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Pada implementasi awal, pencarian successor perlu memperhatikan kondisi ketika tidak ada node dengan hash yang lebih besar atau sama dengan hash yang dicari. Yang dimana jika kondisi ini tidak ditanangani, maka pencarian successor pada ring bisa menghasilkan node yang salah.
 
- Cara memperbaikinya: Cara kami memperbaikinya adalah dengan mengurutkan ID node, kemudian mencari node dengan ID terkecil yang lebih besar atau sama dengan hash key. Jika tidak ada node yang ditemukan, maka successor ditentukan dengan cara memilih node yang memiliki ID terkecil dalam ring (wrap-around). Dengan begitu, pencarian successor tetap dapat berjalan dengan benar dan sesuai dengan konsep Chord. 

## Skenario join/leave
- Hasil sebelum & sesudah node baru bergabung: ...
- Hasil sebelum & sesudah node keluar: ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
