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

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

---

## Pitfall 2: [nama pitfall] — ditulis oleh [nama]

(ulangi struktur di atas)

## Kesimpulan Kelompok

[Ringkasan: jika FoodGo memperbaiki ketiga pitfall ini, apa arsitektur yang disarankan secara garis besar? Kaitkan dengan Tugas 2.]
