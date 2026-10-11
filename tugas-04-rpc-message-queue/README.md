# Tugas 4 (Pekan 4) — Komunikasi Antar Komponen

**Materi terkait:** Remote Procedure Call (RPC), Message-Oriented Middleware (MOM)/Message Queue.

**Kelompok:** [Kelompok 5]

| Nama | NIM |
|---|---|
| [Bethari Nevyta Amaries] | [103072430016] |
| [A'ilah Nailul Fa'izah] | [103072400042] |

## Hasil Analisis
### Jalur A: RPC (Sinkron)
- Bukti Client Menunggu
Server diberi jeda 3 detik agar terlihat bahwa client benar-benar menunggu jawaban dari server. Pada terminal client, waktu tunggu saat melakukan pengecekan saldo tercatat sekitar 5,03 - 5,06 detik. Selama proses tersebut berjalan, client tidak langsung melanjutkan ke langkah berikutnya namun menunggu respon dari server baru melanjutkan ke proses pembayaran. 

Waktu yang yang tercatat lebih lama dibandingkan time.sleep yang diberikan karena waktu tersebut juga menghitung waktu komunikasi RPC dan proses lainnya selama fungsi tersebut berjalan. 

- Keputusan: user tidak ditemukan
Pada percobaan pertama, nilai 0 digunakan untuk menandakan bahwa user id tidak ditemukan. Namun, berdasarkan hasil analisis kami hal tersebut membuat client tidak dapat membedakan akun yang tidak ditemukan dengan akun yang benar - benar memiliki saldo 0. Oleh karena itu, pada user id yang tidak ditemukan kami mengembalikan error agar client dapat membedakan kedua kondisi tersebut. 

### Jalur B: Message Queue (Asinkron)
- Hasil Pengujian 
Publisher mengirim pesan berisi data user, jumlah pembayaran, dan waktu ke antrean `pembayaran_berhasil`. Kemudian pada modul consumer menerima dan memproses pesan satu per satu sesuai dengan urutan antrean. Setelah seluruh antrean selesai diproses, modul consumer akan memberikan acknowledgement (ACK) ke RabbitMQ sebagai tanda bahwa pesan sudah selesai diproses. 

- Uji "pesan tidak hilang"
Pengujian dilakukan dengan menjalankan modul publisher sebanyak 3 kali, yang dimana pada setiap run-nya mengirimkan 3 pesan. Ketika modul consumer dimatikan terlebih dahulu, pesan yang dikirimkan tersimpan di antrean `pembayaran_berhasil` yang berstatus Ready sebanyak 9. Kemudian setelah modul consumer dijalankan, seluruh pesan yang ada di antrean akan diproses sesuai urutan dan antrean akan menjadi kosong kembali. Pada saat modul publisher dijalankan kembali ketika modul consumer sedang berjalan, seluruh pesan yang baru masuk ke antrean akan langsung diproses oleh modul consumer sehingga antrean tetap kosong. 

### Analisis Pemilihan Pola Komunikasi
- Kenapa RPC cocok untuk Pesanan ke Pembayaran
Karena membutuhkan jawaban pada saat itu juga. Sebelum pesanan dilanjutkan atau dibatalkan, sistem harus memastikan dulu uang pembeli cukup. Kalau belum bayar atau uangnya kurrang, pesanan tidak boleh dilanjutkan.

- Kenapa MQ cocok untuk Pembayaran ke Kurir
Karena bagian ini hanya kabar satu arah. Pembeli sudah selesai membyara, jadi pembyaran tidak perlu menunggu kurir siap atau membuka aplikasinya. Kabar pesanan cukup dititipkan di antrean supaya kurir bisa membacanya kapan pun sedang aktif.

- Apa yang terjadi kalau dipakai di skenario yang salah
- Jika Message Queue dipakai untuk Pesanan ke Pembayarran, alur belanja jadi membingungkan. pembeli harus menunggu tanpa kejelasan apakah transaksinya diterima atau ditolak, karena pesanan dikirim tanpa langsung meminta jawaban soal saldo.
- JIka RPC dipakai untuk pembayaran ke kurir, kedua modul bisa jadi saling bergantung. Kalau kurir sedang susah sinyal, aplikasinya mati, atau lambat merespon, proses pembayaran pembeli ikut macet dan tertahan, padahal uangnya sudah siap dipotong

- Trade-off
- RPC : Mudah dipahami dan hasilnya langsung didapat saat itu juga, tetapi kalau pihak penerima lambat atau bermasalah, pihak pengirim juga ikut terjebak menunggu.
- Message Queue : Fleksible dan aman karena pengirim bisa langsugn lanjut bekerja tanpa takut pesan hilang saat penerima sedang tidak aktif, tetapi butuh perantara tambahan dan kita tidak langsung tau kapan pesan itu selesai dikerjakan.

## Studi Kasus

Modul **Pembayaran** dan modul **Pesanan** FoodGo harus berkomunikasi secara reliabel. Untuk beberapa operasi (mis. cek status saldo) respons dibutuhkan **seketika** (sinkron). Untuk operasi lain (mis. kirim notifikasi "pembayaran berhasil" ke modul kurir) sistem **tidak boleh menunggu** — modul pembayaran harus tetap responsif walau modul kurir sedang sibuk/down (asinkron).

## Pilihan Tugas

Kelompok **wajib memilih salah satu jalur** di bawah (boleh mengerjakan keduanya untuk nilai eksplorasi tambahan, tapi minimal satu harus selesai penuh dengan bukti jalan):

### Jalur A — RPC (Sinkron)

Skeleton di folder `rpc/` memakai `xmlrpc` — bagian dari Python standard library, **tidak perlu install apa pun**.

- `rpc/server.py`: mensimulasikan modul Pembayaran, expose fungsi `cek_saldo(user_id)` dan `proses_pembayaran(user_id, jumlah)` lewat RPC.
- `rpc/client.py`: mensimulasikan modul Pesanan yang memanggil fungsi RPC di atas dan menunggu hasilnya.

Jalankan (dua terminal terpisah, di laptop yang sama):
```bash
python3 rpc/server.py      # terminal 1
python3 rpc/client.py      # terminal 2
```

### Jalur B — Message Queue / MOM (Asinkron)

Skeleton di folder `mq/` memakai **RabbitMQ** yang dijalankan **lokal lewat Docker** (image resmi RabbitMQ, gratis, tidak perlu daftar akun apa pun) + library Python `pika`.

```bash
cd mq
docker compose up -d           # jalankan broker RabbitMQ lokal
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 consumer.py            # terminal 1: jalankan dulu consumer (modul kurir)
python3 publisher.py           # terminal 2: kirim event (modul pembayaran)
```

- `mq/publisher.py`: mensimulasikan modul Pembayaran yang mem-publish event `pembayaran_berhasil` tanpa menunggu balasan.
- `mq/consumer.py`: mensimulasikan modul Kurir/Notifikasi yang subscribe dan memproses event tersebut kapan pun siap.

Dashboard manajemen RabbitMQ (untuk lihat antrean secara visual) otomatis aktif di `http://localhost:15672` (login default `guest`/`guest`) — sertakan screenshot dashboard ini sebagai bukti tambahan.

## Tugas Kelompok

1. Lengkapi bagian `# TODO` di jalur yang dipilih.
2. Buktikan program benar-benar berjalan (screenshot 2 terminal berdampingan, atau video).
3. Untuk Jalur B, matikan dulu `consumer.py`, jalankan `publisher.py` beberapa kali, lalu nyalakan `consumer.py` — buktikan pesan **tetap diproses** (tidak hilang) karena antrean menyimpannya. Ini adalah inti pembelajaran *asynchronous decoupling*.
4. Tulis analisis: kenapa jalur ini (RPC atau MQ) cocok untuk skenario yang kalian pilih, dan apa yang terjadi jika dipakai untuk skenario yang salah (mis. RPC dipakai untuk notifikasi kurir → modul pembayaran ikut lambat kalau kurir down).

## Struktur Submission

```
tugas-04-rpc-message-queue/
├── README.md      # Analisis: kenapa sinkron/asinkron, hasil uji "pesan tidak hilang"
├── JURNAL.md
├── rpc/            # Jalur A (jika dikerjakan)
├── mq/             # Jalur B (jika dikerjakan)
└── bukti/
```

## Rubrik Penilaian (Tugas 4)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Implementasi berjalan (minimal 1 jalur) | 35% | RPC call sukses dapat balasan, ATAU pesan MQ sukses dikonsumsi |
| Bukti *asynchronous decoupling* (khusus Jalur B) / bukti sinkron blocking (Jalur A) | 25% | Skenario consumer mati lalu nyala lagi (B), atau bukti client menunggu response (A) |
| Analisis pemilihan pola komunikasi | 25% | Justifikasi tepat berdasarkan kebutuhan sinkron vs asinkron di skenario |
| Proses & kontribusi kelompok | 15% | `JURNAL.md`, commit history |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya konsep umum RPC/message queue ke AI; **tidak boleh** meminta AI menuliskan isi `# TODO` di `rpc/server.py`, `rpc/client.py`, `mq/publisher.py`, atau `mq/consumer.py`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- `JURNAL.md` wajib menjelaskan apa yang terjadi pada request RPC jika server mati di tengah proses (Jalur A), atau ke mana pesan "hilang sementara" tersimpan saat consumer mati (Jalur B) — jawaban generik/hafalan istilah tanpa mengaitkan ke hasil percobaan sendiri akan dinilai rendah.
