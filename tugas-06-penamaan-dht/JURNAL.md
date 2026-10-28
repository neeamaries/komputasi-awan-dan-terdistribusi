# Jurnal Proses — Tugas 6

## Implementasi find_successor
- Kesalahan pertama yang ditemui (mis. lupa wrap-around di ring): Pada implementasi awal, pencarian successor perlu memperhatikan kondisi ketika tidak ada node dengan hash yang lebih besar atau sama dengan hash yang dicari. Yang dimana jika kondisi ini tidak ditanangani, maka pencarian successor pada ring bisa menghasilkan node yang salah.

- Cara memperbaikinya: Cara kami memperbaikinya adalah dengan mengurutkan ID node, kemudian mencari node dengan ID terkecil yang lebih besar atau sama dengan hash key. Jika tidak ada node yang ditemukan, maka successor ditentukan dengan cara memilih node yang memiliki ID terkecil dalam ring (wrap-around). Dengan begitu, pencarian successor tetap dapat berjalan dengan benar dan sesuai dengan konsep Chord. 

## Skenario join/leave
* Hasil sebelum & sesudah node baru bergabung: Sebelum node baru bergabung, ring memiliki empat node, yaitu Jakarta-1 dengan ID 177, Jakarta-2 dengan ID 102, Bandung-1 dengan ID 40, dan Surabaya-1 dengan ID 136. Kemudian, node Medan bergabung dengan ID 123. Setelah node Medan bergabung, proses lookup tetap berjalan dengan benar, dan node Medan menjadi bagian dari ring. Contohnya, kurir-001 tetap ditemukan dengan IP 192.168.1.10 melalui node Jakarta-2. Yang dimana pada skenario ini tidak ada mapping kurir yang berpindah karena key kurir yang telah terdaftar tetap menjadi tanggung jawab node sebelumnya. 

* Hasil sebelum & sesudah node keluar: Ketika node Jakarta-1 dengan ID 177 keluar, lookup kurir masih berhasil. Yang dimana untuk menguji perpindahan tanggung jawab mapping, node Bandung-1 dengan ID 40 kemudian dikeluarkan dari ring. Yang dimana sebelum node Bandung-1 keluar, kurir-002 dengan hash 28 menjadi tanggung jawab dari Node Bandung-1. Setelah node Bandung-1 keluar, maka tanggung jawab akan berpindah ke node Jakarta-2. Proses lookup setelah perubahan akan tetap menghasilkan IP 192.168.1.11. Hasil ini menunjukan bahwa lookup masih dapat berjalan dengan benar meskipun telah terjadi perubahan topologi dan tanggung jawab mapping berpindah ke node lain. 

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |
