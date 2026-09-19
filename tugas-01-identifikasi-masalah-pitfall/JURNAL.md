# Jurnal Proses — Tugas 1

> Isi jurnal ini selama proses diskusi berlangsung, bukan ditulis ulang rapi di akhir. Tulis dengan gaya bebas — poin diskusi, kebuntuan, perubahan pikiran.

## [18 September 2026] - Offline Meet
- Peserta: Bethari Nevyta Amaries, A'ilah Nailul Fa'izah
- Poin diskusi: Membahas pitfall yang ditemukan pada skenario FoodGo, Melakukan pembagian tugas dalam menganalisis pitfall yang ditemukan, Menganalisis pitfall sesuai pembagian tugas yang ditentukan .

- Perbedaan pendapat (jika ada): Menurut Aila pitfall yang sesuai dengan kalimat ketiga adalah "The Network is Reliable" sedangkan menurut Nevy pitfall yang sesuai adalah latency is zero. Setelah melakukan diskusi, ternyata pitfall yang lebih sesuai adalah "The Network is Reliable" karena jika mengacu pada skenario tidak ada pembahasan mengenai latecy. 

## [19 September 2026] - Online Meet
- Peserta : Bethari Nevyta Amaries, A'ilah Nailul Fa'izah
- Poin diskusi : Melakukan diskusi mengenai pitfall ketiga, mencatat log penggunaan AI sejak hari pertama, dan mengisi kesimpulan kelompok. 

## [Tanggal diskusi 2]
- ...

## Review Silang
- A'ilah Nailul Fa'izah mengomentari analisis Bethari Nevyta Amaries:
    - Pitfall #1 "Bandwidth is Infinite" :
    Menurut saya pemilihan bukti sudah cocok karena langsung menyorot kondisi saat jam sibuk promo. Solusi rate limiting yang diajukan juga masuk akal buat menahan lonjakan trafik.
        
    Tetapi bagian 'Kenapa ini keliru' dan 'Dampak' rasanya masih agak tertukar antara masalah jaringan (bandwidth) dengan kemampuan mesin server mengolah data. Server yang crash karena menjalankan semua fungsi sekaligus itu lebih condong ke isu keterbatasan CPU/RAM (resource exhaustion). Kalau bicara murni bandwidth, titik masalahnya ada pada pipa kirim-terima datanya yang sesak. Jadi solusinya menurutku nggak cuma sekadar memperbesar bandwidth, tapi bisa diakali dengan kompresi data atau pasang cache/CDN.

    - Pitfall #3 "Design Failure (Arsitektur Monolitik)" :
    Menurut saya poin utamanya sudah tepat, penjelasan mengenai tidak adanya batasan resource antar-modul di monolitik sudah menggambarkan kenapa modul pembayaran yang padat bisa ikut bikin fitur pesanan dan notifikasi kurir terseret lambat.

    Dari saya sendiri jika modulnya ingin dipecah jadi microservices, sebaiknya menggunakan komunikasi asinkron agar modulnya tidak saling tunggu secara sikron dan terpicunya masalah latensi  baru.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 18 September 2026 | Claude | Apa itu Pitfall? Dan jelaskan "the network is reliable", "latency is zero", "bandwidth is infinite", "the network is secure", "topology doesn't change", "there is one administrator", "transport cost is zero", "the network is homogeneous" dan single point of failure karena arsitektur monolitik. | AI menjelaskan mengenai apa itu "The 8 Fallacies of Distributed Computing" dan contoh dari masing masing fallacy. Selain itu AI juga menjelaskan kelemahan dari arsitektur monolitik. | Memahami konsep dan penjelasan yang diberikan dan mengkaitkannya dengan skenario pada FoodGo sehingga dapat menganalisis pitfall yang ada pada skenario yang diberikan |
| 18 September 2026 | Claude | Jelaskan konsep umum dari arsitektur monolitik dan single point of failure (SPOF) | AI menjelaskan definisi umum dari kedua istilah dan logika kenapa proses yang digabungnmnejadi satu itu rawan gagal seacara bersamaan | Menganalisis dan mengkaitkannya dengan FoodGo dan memberikan alasan kekeliruan sesuai pemahaman pribadi  |
| 18 September 2026 | Gemini | Uraikan lebih detail mengenai pitfall jika mengacu pada file materi | Menjelaskan definisi pitfall (Fallacies of Distributed Computing) sebagai jebakan asumsi keliru dan tersembunyi yang membuat arsitektur tampak sederhana di awal namun rentan rusak dan memicu patching, serta merinci 8 poin asumsi keliru mengenai karakteristik jaringan (keandalan, keamanan, homogenitas, topologi, latensi nol, bandwidth tak terbatas, biaya transport nol, dan satu administrator). | Menghubungkan konsep 8 fallacies tersebut ke dalam analisis studi kasus aplikasi FoodGo |
| 18 September 2026 | Claude | Dampak the network is reliable apa saja pada kasus lonjakan server/sistem pada aplikasi Online | Menjelaskan 7 dampak berantai kegagalan jaringan yaitu silent failure, duplikasi transaksi, inkonsistensi data, cascading failure, penipisan sumber daya server, minimnya visibilitas diagnostik, hingga penurunan retensi pengguna, serta memetakan strategi mitigasi fault tolerance berbasis controlled retry, idempotency key, dan circuit breaker. | Memfilter 7 poin dari AI dan memilih fokus pada isu silent failure seperti transaksi hilang di tengah jalan akibat ketiadaan retry saat lonjakan trafik jam makan siang/promo. |
| ... | ... | ... | ... | ... |
