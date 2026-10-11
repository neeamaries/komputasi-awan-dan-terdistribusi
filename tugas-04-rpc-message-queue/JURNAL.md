# Jurnal Proses — Tugas 4

## Jalur yang dipilih
- Jalur yang dipilih adalah keduanya (RPC dan Message Queue), alasan: Karena dua interaksi utama di FoodGO punya kebutuhan komunikasi yang berbeda. RPC digunakan untuk komunikasi dari modul Pesanan ke modul pembayaran, karena modul pesanan harus tau hasilnya saat itu juga untuk menentukan apakah pesanan dilanjutkan atau dibatalkan.  Message Queue digunakan untuk notifikasi pembyaran ke kurir, karena kabar ini tidak perlu di jawab langsung. Modul pembayaran cukup menitipkan pesan ke antrean lalu lanjut bekerja, sehingga tidak ada yang ikut tertahan kalau kurir sedang lambat atau mati. RPC dipilih saat hasilnya harus diketahui langsung, sedangan Message Queue dipilih saat kabar cukup dititpkan tanpa membuat pengirimnya menunggu.

## Kendala teknis
- Error saat setup (mis. koneksi RabbitMQ ditolak, port bentrok): 
- A'ilah Nailul Fa'izah : Muncul pesan `ModuleNotFoundError: No module named 'pika'` saat menjalankan python consumer.py di terminal PowerShell. Masalah diselesaikan dengan mengaktifkan virtual environment via .\venv\Scripts\Activate.ps1 lalu memasang pustaka menggunakan pip install pika.

## Uji "pesan tidak hilang" (khusus Jalur B)
- Langkah uji: matikan consumer → jalankan publisher → nyalakan consumer
- Hasil yang diamati: Saat modul kurir (consumer) dimatikan, modul pembayaran (publisher) dijalankan 3 kali. Modul pembayaran mengirim 3 peson dengan total ada 9 pesan. Modul pembayaran selesai mengirim tanpa menunggu siapa pun dan kesembilan pesan tersimpan di antrean `pembayaran berhasil`. setelah modul kurir dinyalakan kembali, semua pesan diterima secara berurutan sampai antrean kosong. Saat modul pembayaran dijalankan sekali lagi ketika modul kurur sedang hidup, 3 pesan baru langsung diterima tanpa menumpuk.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 10 Oktober 2026 | Claude | Menanyakan konsep di balik TODO pada `client.py` (ServerProxy, panggilan RPC sinkron, pengukuran waktu) | AI menjelaskan konsep client stub, sifat blocking panggilan RPC, dan ide menambah jeda di server agar bukti blocking terlihat, tanpa menuliskan isi TODO | Menuliskan kode `client.py` dan `server.py`, lalu menambahkan `time.sleep(3)` di server untuk membuktikan client menunggu |
| 10 Oktober 2026  | Claude | Menanyakan kenapa hasil saldo dua client berbeda dan kenapa waktu tempuh 5 detik padahal sleep.time yang ditambahkan 3 detik | AI menjelaskan saldo disimpan bersama di server sehingga pembayaran client kedua melihat saldo yang sudah berkurang, dan mengajukan dugaan soal jeda localhost di Windows | Penjelasan dipakai untuk pemahaman pribadi |
| 10 Oktober 2026 | Claude | Menanyakan cara mengatasi error saat setup (requirements.txt tidak ditemukan, docker compose gagal, ModuleNotFoundError: pika) | AI menjelaskan penyebab (salah folder, pip menunjuk ke Python global) dan menyarankan cd ke folder mq serta python -m pip install | Perbaikan dijalankan sendiri di laptop dan dicatat di bagian Kendala teknis |
| ... | ... | ... | ... | ... |

