# Jurnal Proses — Tugas 9

## Diskusi deployment model
- Opsi yang dipertimbangkan dan kenapa akhirnya memilih salah satu: ...
  - **Public Cloud murni** : sangat skalabel dan elastis, tapi data sensitif (NIK, biometrik) berada di infrastruktur yang tidak dikendalikan penuh oleh negara. Ditolak karena bertentangan dengan kebutuhan kedaulatan data dan UU PDP.
  - **Private Cloud murni** : kendali penuh dan keamanan tinggi, tapi biaya tinggi dan kurang elastis saat terjadi lonjakan akses (pemilu / pendaftaran sekolah).
  - **Hybrid Cloud** : dipilih sebagai solusi tengah. Data inti dan layanan sensitif tetap di Private Cloud (kendali negara), sedangkan portal publik dan penanganan lonjakan trafik diletakkan di Public Cloud (cloud bursting).

- Alasan akhir memilih Hybrid:
  - Memenuhi kebutuhan **kerahasiaan** (data sensitif tidak keluar dari kendali negara).
  - Tetap mendapatkan **rapid elasticity** dari public cloud saat lonjakan.
  - Karakteristik NIST (terutama rapid elasticity + measured service) lebih optimal dibanding private murni, tanpa mengorbankan keamanan seperti public murni.

## Diskusi service model per komponen
- Database inti (NIK, alamat, biometrik) → **IaaS di Private Cloud**  
  Butuh kendali penuh atas OS, enkripsi, lokasi data, dan manajemen kunci (HSM/KMS milik negara).

- Layanan verifikasi & pencocokan biometrik → **PaaS (container/K8s) di Private Cloud**  
  Tim fokus ke logika aplikasi, platform mengurus scaling & deployment. Data biometrik tetap diproses di private.

- API Gateway & autentikasi instansi → **PaaS** (utama di Private, bisa diperluas ke Public saat lonjakan).

- Portal publik cek status → **PaaS di Public Cloud**  
  Paling terdampak lonjakan, hanya menampilkan status minimal, tidak menyimpan data sensitif.

- Backup, DR, arsip terenkripsi → **IaaS di Private Cloud** (situs DR terpisah milik negara).

- Logging, monitoring, audit akses → **IaaS/PaaS di Private Cloud**  
  Log akses sendiri bersifat sensitif.

- Aplikasi pendukung non-sensitif (email dinas, helpdesk, dll) → **SaaS di Public Cloud**.

## Log Penggunaan AI (Level 2)

> Wajib diisi sesuai kebijakan Level 2 di [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Tulis "Tidak memakai AI" pada baris pertama jika memang tidak dipakai. Hanya untuk brainstorming ide/outline — bukan untuk kode/analisis/teks akhir.

| Tanggal | Tool AI | Prompt yang diberikan | Ringkasan saran/ide AI | Bagaimana diolah jadi tulisan/kode sendiri |
|---|---|---|---|---|
| 21 Nov 2026 | Grok | Jelaskan perbedaan Public, Private, Hybrid Cloud dalam konteks data kependudukan yang sensitif | AI menjelaskan kelebihan-kekurangan masing-masing model dan menyarankan Hybrid sebagai opsi tengah | Ide Hybrid diambil, lalu dikembangkan sendiri dengan tabel karakteristik NIST dan pemetaan ke kebutuhan UU PDP serta lonjakan akses |
| 21 Nov 2026 | Grok | Apa saja risiko spesifik Hybrid Cloud untuk sistem data kependudukan? | AI menyebutkan risiko sinkronisasi data, kebocoran, dan vendor lock-in | Risiko disesuaikan menjadi 3 poin spesifik (ketidaksinkronan, kebocoran biometrik, ketergantungan public cloud) + mitigasi yang lebih konkret |
