# Tugas 1 — Analisis Pitfall FoodGo

**Kelompok:** [nama kelompok]

| Nama | NIM | Kontribusi |
|---|---|---|
| [Bethari Nevyta Amaries] | [103072430016] | [pitfall/bagian yang dikerjakan] |
| [A'ilah Nailul Fa'izah] | [103072400042] | [pitfall/bagian yang dikerjakan] |

## Pitfall 1: Bandwidth is Infinite — ditulis oleh Bethari Nevyta Amaries

**Bukti di skenario:** "Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama."

**Kenapa ini keliru:** Dengan mengasumsikan bahwa bandwidth tidak terbatas merupakan hal yang tidak tepat. Karena pada skenario menyatakan bahwa server yang menangani seluruh modul mengalami kewalahan saat trafik naik. Hal ini dikarenakan server yang menangani seluruh modul hanya memiliki bandwidth yang terbatas. Sehingga saat terjadi lonjakan trafik, server tidak mampu menangani seluruh request yang masuk.

**Dampak ke FoodGo:** Karena FoodGo tidak menyiapkan bandwidth yang cukup pada saat menangani lonjakan trafik, maka pada saat jam makan siang / promo menyebabkan request yang melebihi kapasitas bandwidth. Hal tersebut menyebabkan server menjadi down dan crash karena overload, akhirnya request yang masuk tidak dapat ditangani dengan baik dan mengakibatkan seluruh sistem menjadi tidak dapat diakses. 

**Solusi desain awal:** Maka solusi yang dapat dilakukan adalah menambahkan kapasitas bandwidth pada server yang akan menangani seluruh modul. Sehingga pada saat terjadi lonjakan trafik, server dapat menangani seluruh request yang masuk dengan baik dan tidak mengalami overload. Selain itu dapat juga dengan melakukan rate limiting pada request yang masuk, sehingga server dapat menangani request yang masuk dengan baik dan tidak mengalami overload. 

**Trade-off:** Apabila mengimplementasikan rate limiting, maka akan berpengaruh pada user experience. Karena apabila request yang masuk melebihi kapasitas bandwidth, maka request yang masuk akan ditolak dan user akan gagal dalam mengakses layanan. 

---

## Pitfall 2: The Network is Reliable — ditulis oleh A'ilah Nailul Fa'izah

**Bukti di skenario:** "Tim menemukan bahwa kode mereka menulis asumsi seperti # network is always reliable, no need for retry dan tidak ada timeout sama sekali pada pemanggilan antar service"

**Kenapa ini keliru:** Jaringan tidak selalu stabil dan rentan mengalami gangguan. Router/switch bisa saja mengalami gangguan, koneksi terputus atau paket data bisa hilang di tengah pengiriman. Gangguan ini memiliki peluang tinggi terjadi pada saat trafik melonjak, dalam kasus ini jam makan siang atau terdapat promo. Tanpa adanya retry, request yang gagal bisa saja tidak terdeteksi atau tidak dapat diperbaiki oleh sistem, sehingga transaksi yang gagal di tengah jalan bisa hilang.

**Dampak ke FoodGo:** Pada saat jam makan siang atau sedang terjadi promo, request dari modul pesanan ke modul pembayaran bisa saja mengalami kegagalan pada saat pengiriman yang disebabkan oleh koneksi terputus, karena tidak ada retry maka sistem yang gagal terkirim bisa hilang begitu saja sehingga tidak ada upaya perbaikan otomatis.

**Solusi desain awal:** Menerapkan retry dengan exponential backoff yang dimana jika terjadi kegagalan pada panggilan ke modul pembayaran, maka akan di coba ulang beberapa kali dengan jeda yang lebih lama dan tidak langsung dianggap gagal permanen. Menambahkan idempotency key pada setiap transaksi agar ketika request di ulang oleh sistem maupun user, sistem akan mengetahui apakah transaksinya adalah transaksi yang sama jika iya, sistem tidak akan memprosesnya dua kali.


**Trade-off:** Logika retry dan idempotency key butuh implementasi dan pengujian ekstra sehingga kompleksitas kode bertambah. Setiap request perlu mengecek idempotency key sebelum diproses yang dapat menyebabkan latensi bisa saja naik.

---

## Pitfall 3: Design Failure (Arsitektur Monolitik) — ditulis oleh Bethari Nevyta Amaries

**Bukti di skenario:** "Saat trafik naik, satu server yang menangani semua modul (pesanan, pembayaran, notifikasi kurir) kewalahan karena semuanya berjalan di satu proses monolitik yang sama."

**Kenapa ini keliru:** Asumsi bahwa arsitektur monolitik merupakan pilihan yang tepat untuk sistem FoodGo adalah tidak benar. Karena arsitektur monolitik menggabungkan seluruh fungsi menjadi satu progress yang berjalan secara beriringan. Hal tersebut mengakibatkan apabila salah satu fungsi membutuhkan banyak resource, maka akan mempengaruhi proses dari fungsi lainnya. 

**Dampak ke FoodGo:** Salah satu dampak  yang terjadi pada FoodGo adalah ketika trafic meningkat pada fungsi pembayaran, fungsi lainnya seperti fungsi pesanan dan notifikasi kurir akan ikut terhambat karena resource yang digunakan untuk fungsi satu dan lainnya saling terhubung. Sehingga hal ini akan mengakibatkan proses yang berjalan menjadi lambat dan tidak efisien.  

**Solusi desain awal:** Mengubah arsitektur monolitik menjadi arsitektur microservice. Yang dimana setiap fungsi dijalankan melalui resource yang berbeda. Sehingga apabila salah satu fungsi membutuhkan resource yang lebih banyak, maka tidak akan mempengaruhi fungsi lainnya. 

**Trade-off:** Apabila arsitektur monolitik diubah menjadi arsitektur microservice, maka akan berpengaruh pada biaya operasional dan kompleksitas sistem. Karena setiap fungsi dijalankan menggunakan resource yang berbeda, maka akan membutuhkan biaya operasional yang lebih tinggi dan tingkat kompleksitas yang lebih tinggi juga.

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
