# Jurnal Proses — Tugas 7

## Diskusi pemilihan model konsistensi
- Argumen yang dipertimbangkan: Kelompok kami mempertimbangan dua model konsistensi yaitu sequential consistency dan eventual consistency. Yang dimana sequential consistency dapat menjamin bahwa urutan perubahan data yang dilakukan tetap konsisten pada seluruh server. Namun, penerapannya tersebut membutuhkan koordinasi antarserver yang dapat mmebuat proses transaksi menjadi lebih lambat. Sedangkan pada model eventual consistency, replikasi data berjalan secara bertahap tanpa harus menunggu seluruh server memiliki data yang sama. Namun, model ini juga memiliki kekurangan, yaitu pelanggan masih bisa membaca data lama sebelum proses replikasi selesai dilakukan. Yang dimana pada kasus FoodGO, hal ini dapat menyebabkan pesanan ditolak meskipun pelanggan sudah melakukan top up dan memiliki saldo yang cukup. 

- Kesimpulan akhir & alasan: Berdasarkan hasil analisis dan simulasi, kami memutuskan untuk menggunakan eventual consistency yang dikombinasikan dengan read-your-writes. Eventual consistency sendiri dipilih karena proses replikasi yang berjalan antara server daapat dilakukan secara bertahap. Namun, eventual consistency saja masih belum cukup karena pelanggan masish berisiko dalam membaca saldo lama sebelum proses replikasi selesai. Maka dari itu, kami menambahkan read-your-writes agar pelanggan dapat membaca hasil perubahan data yang sebelumnya dilakukan oleh dirinya sendiri. Pada simulasi yang telah dilakukan, setiap perubahan saldo memiliki nomor versinya sendiri. Sehingga, jika pelanggan membaca saldo melalui Bandung dan versi datanya masih lebih rendah dari versi data terakhir, sistem akan mengalihkan pembacaan ke Jakarta yang memiliki versi data terbaru. 

## Simulasi (jika dikerjakan)
- Hasil skenario naif vs Read-Your-Writes: Pada skenario naif, kami melakukan top-up sebesar Rp50.000 melalui server Jakarta, lalu langsung membaca saldo dari server Bandung setelah 0,5 detik. Hasilnya saldo yang terbaca adalah 0, padahal seharusnya 50.000. Hal ini terjadi karena replikasi ke Bandung sengaja kami tunda selama 2 detik, sehingga data baru belum sampai saat saldo dibaca. Hal ini membuktikan bahwa pelanggan bisa membaca saldo lama jika hanya mengandalkan eventual consistency. Pada skenario Read-Your-Writes, top-up Rp20.000 dilakukan melalui Jakarta sehingga saldo menjadi 70.000 (versi 2). Saat saldo dibaca dari Bandung, sistem menemukan bahwa versi data di Bandung masih 1, lebih rendah dari versi minimal yang dibutuhkan yaitu 2. Sistem kemudian mengalihkan pembacaan ke Jakarta, sehingga saldo yang terbaca benar, yaitu 70.000, walaupun replikasi belum selesai. Beberapa detik kemudian, Bandung ikut terbarui ke versi 2.

- Kendala yang ditemui: Log replikasi ke Bandung muncul belakangan dan tidak berurutan dengan proses pembacaan, karena replikasi berjalan terpisah dari program utama. 

- Cara mengatasi: Kami memberi jeda waktu di antara kedua skenario supaya replikasi skenario pertama selesai terlebih dahulu dan tidak tercampur dengan skenario kedua. 

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 15 November 2026 | Claude | Membantu memahami perbedaan Sequential Consistency, Eventual Consistency, dan Client-Centric Consistency (Read-Your-Writes) | AI menjelaskan masalah replikasi, perbedaan model data-centric dan client-centric| Dipakai sebagai pengetahuan pribadi diskusi kelompok untuk menentukan model konsistensi |
|  15 November 2026  | Claude | Mengunggah slide materi week 7 beserta soal Tugas 7, lalu meminta AI menandai dan menjelaskan bagian materi-materi yang masuk pada Tugas 7 | AI memetakan slide ke tiap poin tugas, menjelaskan Sequential, Eventual, dan Client-Centric Consistency (Read-Your-Writes), serta menyarankan kerangka sequence diagram | Dipakai sebagai bahan belajar dan diskusi kelompok. |