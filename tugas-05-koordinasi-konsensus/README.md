# Tugas 5 (Pekan 5) — Koordinasi & Konsensus

**Materi terkait:** Physical/Logical Clock, Election Algorithm (Bully/Raft).

**Kelompok:** [Kelompok 5]

| Nama | NIM |
|---|---|
| [Bethari Nevyta Amaries] | [103072430016] |
| [A'ilah Nailul Fa'izah] | [103072400042] |

## Studi Kasus

Terjadi konflik urutan waktu pada pesanan FoodGo (dua server mencatat urutan pesanan berbeda karena jam tidak sinkron), dan sistem membutuhkan satu **"Node Leader"** untuk mengelola antrean pesanan pusat agar tidak terjadi konflik pemrosesan ganda.

## Implementasi Bully Algorithm

### Alur Pesan
- `ELECTION`: dikirim sebuah node kepada node ber-ID lebih besar sebagai tanda bahwa pemilihan leader dimulai
- `OK`: balasan dari node ber-ID lebih besar yang masih aktif. Node pengirim `ELECTION` berhenti mencalonkan diri, sedangkan node yang membalas melanjutkan pemilihan ke node di atasnya
- `COORDINATOR`: pengumuman dari node terpilih kepada seluruh node bahwa dirinya adalah leader
- `PING`: pemeriksaan yang dikirim setiap node (selain leader) ke leader setiap 3 detik untuk memastikan leader masih aktif

Pada start normal, setiap node memulai pemilihan dengan mengirim `ELECTION` ke node yang ID-nya lebih besar. Node 5 tidak memiliki node di atasnya sehingga menjadi leader dan mengirim `COORDINATOR` ke node lainnya.

### Keputusan Desain
- Langsung menjadi leader tanpa menunggu : jika tidak ada satu pun node ber-ID lebih besar yang dapat dihubungi, node langsung menyatakan diri sebagai leader tanpa menunggu 2 detik, karena tidak ada balasan yang perlu ditunggu.
- Penggunaan `threading.Event` : begitu balasan `OK` diterima, masa tunggu langsung dihentikan sehingga node dapat segera beralih menunggu pengumuman `COORDINATOR`.
- Pemeriksaan `PING` berkala : setiap 3 detik, node mengirim `PING` ke leader. Jika koneksi gagal, leader dianggap mati dan node memulai pemilihan baru.
- Pemilihan dijalankan di thread terpisah : setiap pemilihan berjalan terpisah dari penanganan pesan masuk dan pemeriksaan leader berkala, karena pemilihan harus menunggu balasan hingga 2 detik. Konsekuensinya, beberapa pemilihan dapat berjalan bersamaan (dibahas pada bagian kelemahan).

## Hasil Pengujian

### Skenario 1: Start normal
Kelima node dijalankan di terminal terpisah. Setiap node memulai pemilihan dengan mengirim `ELECTION` ke node yang lebih besar. Pada log node 1, `ELECTION` terkirim ke node 2, 3, 4, dan 5, dan keempatnya membalas `OK`. Node 5 tidak memiliki node di atasnya sehingga langsung menjadi leader dan mengirim `COORDINATOR` ke node 1, 2, 3, dan 4. Node 1 sampai 4 mencatat node 5 sebagai leader.

### Skenario 2: Leader mati
Saat node 5 dimatikan. Node 1, 2, 3, dan 4 mendeteksinya karena `PING` tidak mendapat balasan. Node 4 tidak dapat menghubungi node 5, sehingga langsung menyatakan diri sebagai leader dan mengirim `COORDINATOR`. Node 1, 2, dan 3 kemudian mencatat node 4 sebagai leader baru. Deteksi mengikuti jadwal `PING` setiap 3 detik, ditambah waktu percobaan koneksi yang gagal (batas 1 detik). Waktu pastinya tidak diukur karena log tidak mencantumkan jam.

Pengujian dilanjutkan dengan mematikan leader secara berurutan:
1. Node 4 dimatikan: node 3 tidak dapat menghubungi node 4 maupun node 5, sehingga node 3 menjadi leader.
2. Node 3 dimatikan: node 2 tidak dapat menghubungi node 3, 4, dan 5, sehingga node 2 menjadi leader.

### Pengamatan Tambahan
- Pesan berulang : pesan `ELECTION` dan `COORDINATOR` diterima berkali-kali. Contohnya, log node 1 mencatat 16 kali `COORDINATOR` dari node 5 pada start normal. Penyebabnya, setiap node memulai pemilihan saat menyala dan setiap `ELECTION` yang masuk memicu pemilihan baru. Karena node 5 tidak memiliki node di atasnya, setiap pemilihan itu berakhir dengan pengumuman `COORDINATOR` ke semua node.
- Pengiriman ke node yang sudah mati : setelah node 5 mati, node 4 tetap mencoba mengirim `COORDINATOR` ke node 5 dan mencatat "Gagal mengirim COORDINATOR ke node 5", sedangkan pengiriman ke node lain tetap berjalan.

## Analisis
### Kenapa FoodGo Butuh Leader
Pada studi kasus, dua server mencatat urutan pesanan yang berbeda karena jam keduanya tidak sinkron, sehingga pesanan berisiko diproses dua kali. Leader menjadi satu pihak yang mengelola antrean pesanan pusat dan menentukan urutan pesanan, sehingga semua server mengikuti urutan yang sama dan setiap pesanan hanya diproses sekali. Jika leader mati, pemilihan leader baru diperlukan agar antrean tetap berjalan.

### Kenapa Bully, dan Perbandingannya dengan Raft
Bully dipilih karena sederhana dan sesuai untuk kelompok kecil yang jumlah dan ID node-nya sudah diketahui sejak awal. Aturannya mudah dipahami, node dengan ID tertinggi yang masih aktif selalu menjadi leader. Hal ini terlihat pada pengujian: leader berpindah dari node 5 ke node 4, 3, lalu 2 saat leader dimatikan satu per satu.

Raft bekerja dengan peran follower, candidate, dan leader. Leader dipilih melalui suara mayoritas, lalu mengirim sinyal berkala (heartbeat) untuk menunjukkan bahwa ia masih aktif. Setiap node juga memiliki batas waktu tunggu yang sedikit berbeda agar pemilihan tidak terjadi bersamaan. Secara umum, Raft lebih aman dan lebih tahan terhadap gangguan jaringan, tetapi implementasi dan pengujiannya jauh lebih rumit. 

### Kelemahan
1. Jumlah pesan meningkat : saat leader mati, node 1, 2, 3, dan 4 sama-sama mendeteksinya dan memulai pemilihan sendiri. Akibatnya node 4 menerima `ELECTION` dari node 1, 2, dan 3 berkali-kali, dan pesan `OK` serta `COORDINATOR` ikut berlipat.
2. Pemilihan berulang tanpa pemeriksaan : setiap `ELECTION` yang masuk selalu memicu pemilihan baru tanpa mengecek apakah pemilihan sedang berjalan. Akibatnya, pesan yang sama dikirim berulang dan log sulit dibaca.
3. Penilaian mati berdasarkan satu percobaan koneksi : node yang tidak menjawab dalam 1 detik langsung dianggap mati. Jika sebuah node hanya lambat, node tersebut dapat dianggap mati dan memicu pemilihan baru padahal leader masih aktif.

## Struktur Submission

```
tugas-05-koordinasi-konsensus/
├── README.md      # Analisis: kenapa perlu leader, kenapa Bully (vs Raft), hasil 2 skenario
├── JURNAL.md
├── src/
│   └── node.py
└── bukti/          # Log/screenshot skenario start normal & leader mati
```

## Rubrik Penilaian (Tugas 5)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi Bully Algorithm benar | 35% | Election, OK, COORDINATOR message bekerja sesuai aturan algoritma |
| Bukti skenario leader mati → re-election | 30% | Log jelas menunjukkan leader baru terpilih otomatis |
| Analisis (kenapa perlu leader, trade-off Bully vs Raft) | 20% | Dikaitkan ke masalah urutan pesanan di skenario FoodGo |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI tentang gambaran umum algoritma election; **tidak boleh** meminta AI menuliskan isi `# TODO` di `src/node.py` (logika `on_message`, `start_election`, `declare_leader`, `monitor_leader`). Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `README.md` wajib menjelaskan kenapa Bully Algorithm selalu memilih node ber-ID tertinggi yang masih hidup, dan apa kelemahannya dibanding algoritma lain (mis. jumlah pesan yang dikirim saat election, single point of failure sebelum leader baru terpilih) — bukan sekadar definisi generik.
