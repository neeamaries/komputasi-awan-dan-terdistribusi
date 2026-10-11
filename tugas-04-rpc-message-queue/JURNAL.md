# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- Jalur yang dipilih adalah keduanya (RPC dan Message Queue), alasannya adalah karena dua interaksi utama di FoodGO punya kebutuhan komunikasi yang berbeda. RPC digunakan untuk komunikasi dari modul Pesanan ke modul pembayaran, karena modul pesanan harus tau hasilnya saat itu juga untuk menentukan apakah pesanan dilanjutkan atau dibatalkan.  Message Queue digunakan untuk notifikasi pembyaran ke kurir, karena notifikasi ke kurir tidak perlu di jawab secara sinkron. Modul pembayaran cukup menitipkan pesan ke antrean lalu lanjut bekerja, sehingga tidak ada yang ikut tertahan kalau kurir sedang lambat atau mati. RPC dipilih saat hasilnya harus diketahui langsung (sinkron), sedangan Message Queue dipilih saat kabar cukup dititpkan tanpa membuat pengirimnya menunggu (asinkron).

## Kendala teknis
- Bethari Nevyta Amaries : Client crash dengan traceback `Fault` (Jalur A): setelah `cek_saldo` diubah dari `return 0` menjadi `raise ValueError`, client berhenti dengan traceback panjang karena errornya tidak ditangani, sementara server tetap hidup. Solusinya membungkus panggilan dengan `try/except xmlrpc.client.Fault`.
- Bethari Nevyta Amaries : `ModuleNotFoundError: No module named 'pika'` padahal venv aktif `pip` menunjuk ke Python global (`...\Python312\site-packages`, tampak dari pesan "Requirement already satisfied"), sedangkan `python` memakai venv. Akibatnya `pika` terpasang di tempat yang salah. Solusinya `python -m pip install -r requirements.txt`, yang memasang library ke Python yang sama dengan yang menjalankan script.
- A'ilah Nailul Fa'izah : Muncul pesan `ModuleNotFoundError: No module named 'pika'` saat menjalankan python consumer.py di terminal PowerShell. Masalah diselesaikan dengan mengaktifkan virtual environment via .\venv\Scripts\Activate.ps1 lalu memasang pustaka menggunakan pip install pika.

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: Saat modul consumer dimatikan terlebih dahulu, modul publisher dijalankan sebanyak 3 kali. Yang dimana pada tiap run mengirimkan 3 pesan, dan jika di run 3 kali artinya mengirimkan 9 pesan. Kemudian setelah di run Modul publisher mengirim tanpa menunggu, yang membuat 9 pesan yang telah dikirimkan sebelumnya tersimpan pada antrean `pembayaran berhasil`. Setelah itu modul consumer dinyalakan, yang membuat semua pesan diterima secara berurutan dan antrean menjadi kosong kembali. Saat modul publisher dijalankan sekali lagi ketika modul consumer sedang berjalan, 3 pesan baru langsung diterima tanpa masuk ke antrean terlebih dahulu.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 10 Oktober 2026 | Claude | Menanyakan konsep di balik TODO pada `client.py` (ServerProxy, panggilan RPC sinkron, pengukuran waktu) | AI menjelaskan konsep client stub, sifat blocking panggilan RPC, dan ide menambah jeda di server agar bukti blocking terlihat, tanpa menuliskan isi TODO | Menuliskan kode `client.py` dan `server.py`, lalu menambahkan `time.sleep(3)` di server untuk membuktikan client menunggu |
| 10 Oktober 2026  | Claude | Menanyakan kenapa hasil saldo dua client berbeda dan kenapa waktu tempuh 5 detik padahal sleep.time yang ditambahkan 3 detik | AI menjelaskan saldo disimpan bersama di server sehingga pembayaran client kedua melihat saldo yang sudah berkurang, dan mengajukan dugaan soal jeda localhost di Windows | Penjelasan dipakai untuk pemahaman pribadi |
| 10 Oktober 2026 | Claude | Menanyakan cara mengatasi error saat setup (requirements.txt tidak ditemukan, docker compose gagal, ModuleNotFoundError: pika) | AI menjelaskan penyebab (salah folder, pip menunjuk ke Python global) dan menyarankan cd ke folder mq serta python -m pip install | Perbaikan dijalankan sendiri di laptop dan dicatat di bagian Kendala teknis |

