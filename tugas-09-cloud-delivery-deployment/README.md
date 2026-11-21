# Tugas 9 (Pekan 9) — Cloud Delivery & Deployment Model

**Materi terkait:** Karakteristik esensial cloud computing (NIST SP 800-145), Deployment Model (Public/Private/Hybrid/Community), Service Model (IaaS/PaaS/SaaS).

**Kelompok:** [Kelompok 5]
| Nama | NIM |
| --- | --- |
| Bethari Nevyta Amaries | 103072430016 |
| Andi Athallah Radja Maliq Muhammad | 103072430016 |
| Fathir Al Farih | 103072400002 |

# Ringkasan Rekomendasi
## 1. Rekomendasi Deployment Model
Rekomendasi: Hybrid Cloud.

- Private cloud (dikendalikan penuh negara) database inti (NIK, nama, alamat, biometrik), layanan verifikasi, manajemen kunci enkripsi, logging, dan backup/DR.
- Public cloud hanya lapisan stateless yang tidak menyimpan data sensitif, yaitu portal publik cek status dan penyangga lonjakan trafik (cloud bursting).
- Karena penggunanya ribuan instansi, segmen private dapat dirancang sebagai cloud bersama antarinstansi (mirip Community Cloud), tetapi tetap di bawah kendali negara.

Analisis berdasarkan 5 karakteristik NIST:

| Karakteristik | Penerapan | Kaitan kerahasiaan vs skalabilitas |
|---|---|---|
| On-demand self-service | Tiap instansi (dukcapil daerah, kepolisian, bank) bisa mendaftarkan akses/API key dan menyediakan sumber daya lewat portal layanan tanpa menunggu tim pusat. | Self-service dibatasi RBAC dan persetujuan berjenjang, jadi kemudahan tidak membuka akses ke data yang bukan hak instansi tersebut. |
| Broad network access | Instansi mengakses lewat API standar (HTTPS/mTLS) dari seluruh Indonesia, dan warga mengakses portal dari perangkat apa pun. | Akses luas hanya di lapisan depan (gateway/portal). Data inti tidak diekspos ke internet, hanya lewat jaringan privat/VPN pemerintah. |
| Resource pooling | Pool di private cloud dipakai bersama banyak instansi (multi-tenant), sedangkan pool di public cloud dipakai untuk portal. | Pooling data sensitif hanya terjadi di infrastruktur negara, dengan isolasi tenant dan enkripsi per tenant. Public cloud tidak menyentuh data sensitif. |
| Rapid elasticity | Saat pemilu atau pendaftaran sekolah, portal dan API stateless otomatis diperluas ke public cloud, lalu dikecilkan lagi setelah lonjakan selesai. | Adalah alasan utama memilih Hybrid, yaitu private cloud tidak perlu dibangun untuk beban puncak yang mahal dan sering menganggur, sementara data tetap aman di private. |
| Measured service | Pemakaian per instansi (request, storage, bandwidth) diukur dan dipantau. | Metering sekaligus menjadi jejak audit (siapa mengakses data siapa, kapan) untuk kepatuhan UU PDP, serta dasar alokasi biaya per instansi. |


## 2. Rekomendasi Service Model (per komponen)

| Komponen | Service Model | Lokasi | Alasan |
|---|---|---|---|
| Database inti (NIK, alamat, biometrik) | IaaS | Private | Butuh kendali penuh atas OS, konfigurasi database, enkripsi at-rest, manajemen kunci (HSM/KMS milik negara), dan lokasi fisik data. |
| Layanan verifikasi & pencocokan biometrik | PaaS (container/Kubernetes) | Private | Tim fokus ke logika aplikasi, sedangkan platform mengurus deployment dan scaling. Data biometrik tetap diproses di private. |
| API gateway & autentikasi instansi | PaaS | Private, gateway tambahan di public saat lonjakan | Mengelola ribuan klien instansi, kuota, dan otorisasi, dengan kebijakan keamanan yang konsisten. |
| Portal publik cek status | PaaS | Public | Aplikasi paling terdampak lonjakan, cocok dengan auto-scaling. Hanya menampilkan status minimal lewat API ke private, tanpa menyimpan NIK lengkap atau biometrik. |
| Backup, DR, arsip terenkripsi | IaaS | Private (situs DR terpisah milik negara) | Perlu kendali atas replikasi, retensi, dan enkripsi, dan data tidak boleh keluar dari kendali negara. |
| Logging, monitoring, audit akses | IaaS/PaaS | Private | Log akses sendiri sensitif (memuat siapa mengakses siapa), jadi tidak diserahkan ke pihak luar. |
| Aplikasi pendukung non-sensitif (email dinas, kolaborasi, helpdesk) | SaaS | Public | Tidak memuat data kependudukan, jadi layanan siap pakai lebih cepat dan murah. |

Pada IaaS dan PaaS, tanggung jawab keamanan bersifat bersama (shared responsibility). Karena berada di private cloud negara, keamanan infrastruktur menjadi tanggung jawab operator negara sendiri, sedangkan keamanan aplikasi dan data tetap tanggung jawab tim pengembang.

## 3. Risiko dan Mitigasi
Penggunaan Hybrid Cloud pada sistem data kependudukan memiliki beberapa risiko tersendiri yang perlu diperhatikan. Yang dimana pemisahan infrastruktur antara private dan public cloud dapat meningkatkan fleksibilitas dan skalabilitas, namun hal tersebut juga dapat menimbulkan tantangan dalam menjaga keamanan dan konsistensi dari data. 
| No | Risiko | Dampak | Mitigasi |
|---|---|---|---|
|1|Ketidaksinkronan data antara private cloud dan public cloud|Warga dapat menerima informasi status yang tidak sesuai dengan kondisi yang sebenarnya. Contoh : perubahan status data kependudukan sudah tercatat pada database utama, namun pada portal publik masih menampilkan data lama. Hal tersebut dapat menyebabkan kesalahan dalam proses verifikasi. |Menjadikan databse pada private cloud sebagai single source of truth. Yang dimana public cloud nantinya akan mengambil data yang diperlukan melalui API yang telah diamankan. Selain itu, penerapan mekanisme sinkronisasi yang terjadwal atau berbasis event, validasi data, dan pencatatan waktu secara berkala agar data dapat segera diperbarui.|
|2|Kebocoran data pribadi dan biometrik|Data pribadi seperti NIK, alamat, dan biometrik dapat disalahgunakan. Yang dimana apabila terjadi kebocoran akan sulit untuk ditangani karena berbeda dengan kata sandi yang dapat langsung diganti|Memastikan bahwa data sensitif tetap disimpan pada private cloud. Kemudian untuk komunikasi antarlingkungan menggunakan enkripsi TLS/mTLS, autentikasi antar server, dan pembatasan akses dengan menggunakan RBAC. Selain itu, juga dapat mengimplementasikan tokenisasi atau penyamaran NIK pada respons API, dan melakukan audit secara berkala, serta menggunakan manajemen kunci enkripsi yang telah dikendalikan oleh negara.|
|3|Terjadinya ketergantungan terhadap penyedia Public Cloud|Jika penyedia mengalami gangguan, mengubah harga layanan, ataupun menghentikan layanan tertentu, sistem akan mengalami kendala pada operasional. Hal tersebt mengakibatkan pemindahan layanan ke penyedia lain yang membutuhkan waktu dan biaya tambahan. |Menggunakan teknologi dan standar yang bersifat terbuka, seperti container dan Kubernetes sehingga splikasi dapat dipindahkan ke lingkungan lain dengan lebih mudah. Selain itu, menyiapkan dokumentasi, konfigurasi, backup, dan cara pemulihan layanan apabola penyedia mengalami gangguan.|

Berdasarkan analisis risiko di atas didapatkan bahwa penerapan hybrid cloud perlu disertai dengan pengaturan keamanan dan pengelolaan data yang jelas. Private cloud tetap menjadi tempat penyimpanan dan pengelolaan data sensitif, namun public cloud digunakan untuk mendukung layanan yang membutuhkan akses luas dan kapasitas tambahan. Dengan demikian, fleksibilitas dari hybrid cloud tetap dapat dimanfaatkan tanpa perlu mengorbankan perlindungan data pribadi masyarakat. 

## 4. Alternatif yang Ditolak
### Alternatif yang ditolak : Public Cloud Murni (Public Cloud Only) 
Model ini sebenarnya memiliki keunggulan pada sisi skalabilitas karena mampu menyediakan karakteristik resouce pooling dan rapid elasticity. Yang dimana kapasitas dari komputasi dan penyimpanan dapat ditingkatkan ataupun dikurangi sesuai dengan kebutuhan tanpa harus membangun seluruh infrastruktur secara mandiri. Selain itu, model ini juga memiliki karakteristik on demand self service yang dimana memungkinkan sumber data diseiakan secara cepat ketika terjadi lonjakan permintaan. 

Namun, model ini tidak kami pilih karena masih kurang sesuai dengan kebutuhan pengendalian data kependudukan yang memiliki sifat sensitif. Data kependudukan yang dikelola sendiri merupakan NIK, alamat, dan biometrik yang dimana bergantung pada infrastuktur serta pengelolaan penyedia eksternal. Yang dimana hal tersebut mengurangi kendali langsung negara terhadap lokasi penyimpanan, pengelolaan, dan pengaman data. 

Selain itu, dengan karakteristik resouce pooling pada public cloud memungkinkan infrastruktur digunakan bersama oleh berbagai pelanggan. Meskipun biasanya terdapat sistem isolasi antar pelanggan, namun pemerintah tetap perlu memastikan bahwa pengelolaan dan pemrosesan data sensitif memenuhi persyaratan kedaulatan data dan ketentuan perlindungan data pribadi yang ada. 

Maka dari itu, public cloud murni tidak dipilih karena keunggulan yang diberikan tidak sebanding dengan kebutuhan dalam pengendalian secara penuh terdapat data kependudukan. Sebagai penggantinya, kami memutuskan untuk menggunakan hybrid cloud yang dimana menggabungkan kendali dari private cloud untuk data sesnsitif dan fleksibilitas dari public cloud untuk layanan yang membutuhkan skalabilitas tinggi. 

## 5. Skenario Tandingan
### Bagaimana jika kantor Dukcapil di daerah terpencil (3T) tidak memiliki infrastruktur lokal untuk terhubung ke Private Cloud pusat dan koneksi internetnya sering tidak stabil?

1. **Dukcapil Daerah Sebagai Pengguna Layanan Terpusat (Tanpa Server Lokal):**
   Dalam arsitektur Hybrid Cloud ini, kantor Dukcapil daerah tidak perlu membangun atau memelihara server *private cloud* sendiri. Seluruh infrastruktur *Private Cloud* dikelola secara terpusat oleh pemerintah pusat (PDN/Kementerian Dalam Negeri) dengan pendekatan menyerupai *Community Cloud* antarinstansi. Petugas Dukcapil daerah cukup mengakses aplikasi pelayanan melalui antarmuka web ringan (*thin client*) menggunakan koneksi VPN/mTLS resmi pemerintah menuju API Gateway pusat.
2. **Penanganan Koneksi Tidak Stabil (Mode Antrean Lokal Terenkripsi):**
   Untuk daerah 3T yang jaringannya sering terputus, aplikasi petugas di daerah dilengkapi fitur *offline queuing* sementara. Saat koneksi terputus, pengajuan perubahan data atau perekaman warga disimpan sementara dalam bentuk terenkripsi menggunakan kunci publik pusat di perangkat petugas (tidak bisa dibaca dalam bentuk *plaintext*). Begitu koneksi kembali stabil, antrean data tersebut dikirim secara otomatis ke *API Gateway* di *Private Cloud* pusat untuk diverifikasi dan disimpan ke database inti, lalu data sementara di perangkat lokal langsung dihapus.
3. **Verifikasi Layanan Publik Tetap Berjalan:**
   Sementara itu, warga maupun instansi lain (seperti bank atau sekolah) tetap dapat mengecek status kependudukan melalui *Portal Publik* di *Public Cloud* yang memiliki ketersediaan tinggi dan *caching* status minimal, sehingga gangguan jaringan di satu daerah terpencil tidak melumpuhkan layanan verifikasi nasional.

## Diagram Pendukung
Diagram visual untuk arsitektur Hybrid Cloud, pemetaan *service model*, serta alur akses data dapat dilihat pada folder [`bukti/`](bukti/).

> Bagian 2 mata kuliah ini murni **analisis & desain di atas kertas** — tidak ada biaya cloud sama sekali, karena tugas berhenti di tahap rekomendasi, bukan implementasi nyata (implementasi baru mulai Tugas 11).

## Studi Kasus

Pemerintah ingin membangun **Sistem Data Kependudukan** (nama, NIK, alamat, data biometrik) yang:
- Sangat **rahasia** (data pribadi warga negara, diatur UU Perlindungan Data Pribadi).
- Diakses oleh **ribuan instansi** (dukcapil daerah, kepolisian, bank untuk verifikasi KYC) dengan pola akses yang **tidak rata** (lonjakan saat musim pemilu/pendaftaran sekolah).
- Butuh **skalabilitas** agar tidak downtime saat lonjakan akses, tapi **tidak boleh** datanya berada di infrastruktur yang tidak terkendali penuh oleh negara.

## Tugas Kelompok

1. **Rekomendasikan Deployment Model** (Public / Private / Hybrid / Community Cloud) yang paling tepat untuk sistem ini. Jelaskan alasannya berdasarkan **karakteristik NIST** (on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service) dikaitkan dengan kebutuhan kerahasiaan vs skalabilitas.
2. **Rekomendasikan Service Model** (IaaS / PaaS / SaaS) yang tepat untuk komponen-komponen berbeda dari sistem ini (boleh berbeda service model untuk komponen berbeda, mis. database inti vs portal publik untuk pengecekan status).
3. Jelaskan **minimal 2 risiko spesifik** dari pilihan kalian dan mitigasinya (mis. jika Hybrid Cloud dipilih: risiko sinkronisasi data antara private & public segment).
4. Bandingkan singkat dengan **satu alternatif yang kalian tolak** — kenapa alternatif itu kurang tepat (mis. kenapa Public Cloud murni ditolak, atau kenapa Private Cloud murni dianggap kurang skalabel).

## Struktur Submission

```
tugas-09-cloud-delivery-deployment/
├── README.md      # Analisis lengkap (isi dengan poin 1-4 di atas)
├── JURNAL.md
└── bukti/          # (opsional) diagram pendukung
```

## Rubrik Penilaian (Tugas 9)

| Komponen | Bobot | Kriteria |
|---|---|---|
| Ketepatan rekomendasi deployment model | 30% | Argumen berbasis karakteristik NIST, bukan sekadar "private cloud lebih aman" tanpa detail |
| Ketepatan rekomendasi service model | 25% | Pemetaan komponen sistem ke IaaS/PaaS/SaaS masuk akal |
| Analisis risiko & mitigasi | 25% | Risiko spesifik ke konteks data kependudukan (bukan risiko generik) |
| Perbandingan dengan alternatif yang ditolak | 20% | Argumen penolakan jelas dan berdasar |

## Batasan Penggunaan AI (Level 2)

Kebijakan **Level 2 (AI Assisted Idea Generation & Structuring)** berlaku — lihat [`../RUBRIK-UMUM.md`](../RUBRIK-UMUM.md). Boleh bertanya ke AI gambaran umum karakteristik NIST/deployment model untuk brainstorming; **tidak boleh** meminta AI menuliskan rekomendasi/analisis akhir yang tinggal ditempel ke `README.md`. Catat pemakaian AI di "Log Penggunaan AI" pada `JURNAL.md`.

- Jawaban yang terasa seperti "template" (bisa dipakai untuk sistem cloud apa saja tanpa menyebut spesifik kependudukan/data pribadi/regulasi) akan dinilai rendah pada komponen ketepatan rekomendasi.
- `README.md` wajib membahas minimal satu skenario tandingan yang kalian buat sendiri (mis. "bagaimana jika instansi daerah tidak punya infrastruktur private cloud sendiri?") beserta jawabannya.
