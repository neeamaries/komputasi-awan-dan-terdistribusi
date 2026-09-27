# Jurnal Proses — Tugas 2

## [23 September 2026] 
- Bethari Nevyta Amaries = Menurut pendapat saya arsitektur yang cocok untuk skenario ini adalah SOA. Alasannya karena pada modul pembayaran pelanggan harus tau seketika apakah pembayaran yang dilakukan berhasil atau tidak. Hal tersebut terjadi karena modul pembayaran akan mengirimkan notifikasi ke modul pelanggan secara langsung. Namun penggunaan SOA juga memiliki kekurangan yaitu apabila salah satu modul down maka modul lain tidak dapat diases juga. 

## [24 September 2026] 
- A'ilah Nailul Fa'izah = Saya memilih Pub-Sub atau Publish-Subscribe sebagai arsitektur yang cocok untuk skenario FoodGo, modul pesanan cukup mengirim event ke message broker tanpa perlu tau siapa penerimanya. Tetapi Pub-Sub juga memiliki kekurangan dimana alurnya tidak linear sehingga sulit untuk ditelusuri saat terjadi error dan jika broker down maka seluruh komunikasi antar modul ikut terhenti.

## [27 September 2026] - Offline Meet
- Berdasarkan hasil analisis kami didapatkan kesimpulan bahwa arsitektur yang cocok untuk skenario FoodGo adalah kombinasi dari SOA dan Pub-Sub. Modul pembayaran dan pesanan menggunakan SOA karena membutuhkan komunikasi langsung dan sinkron, sedangkan modul notifikasi dan katalog resto menggunakan Pub Sub karena tidak membutuhkan komunikasi langsung dan sinkron antar modul. 

## [Tanggal]
- Opsi arsitektur yang dipertimbangkan: ...
- Kenapa akhirnya pilih [SOA/Pub-Sub]: ...
- Revisi diagram (versi 1 → versi 2, apa yang berubah dan kenapa): ...

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 23 September 2026 | Claude | Menanyakan penjelasan konsep SOA dan Publish-Subscribe secara detail, termasuk analogi dan perbandingannya | AI menjelaskan konsep umum SOA (sinkron, request-response, saling manggil langsung) dan Pub-Sub (asinkron, event-driven, lewat broker), beserta kelebihan-kekurangan masing-masing. | Memahami konsep yang dijelaskan AI mengenai gaya arsitektur dan mana yang akan dipilih untuk tiap modul FoodGo. Sebagai bahan diskusi dan keputusan kelompok. |
| 24 September 2026 | Gemini | Berikan penjelasan mengenai arsitektur SOA dan Pub-Sub, paparkan juga kelebihan serta kekurangan dari masing masing arsitektur | Menjelaskan definisi SOA (pemecahan layanan berbasis ESB) dan Pub-Sub (arsitektur pesan asinkron berbasis Message Broker). Merinci kelebihan dan kekurangan masing-masing (seperti isu SPOF dan latensi ESB pada SOA vs eventual consistency dan debugging pada Pub-Sub), serta menyajikan tabel perbandingan sifat komunikasi, pola interaksi, coupling, dan penggunaan utama | Memahami kedua arsitektur dan mengusulkan penggunaan arsitektur Pub-Sub agar modul pesanan FoodGo dapat mengirim event secara asinkron tanpa ketergantungan langsung antar-modul. |
| ... | ... | ... | ... | ... |
