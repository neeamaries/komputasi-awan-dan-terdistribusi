"""
Tugas 4 - Jalur A: RPC Client (simulasi modul Pesanan)
Jalankan server.py di terminal lain terlebih dahulu.
"""

import xmlrpc.client
import time


def main():
    # TODO 1: buat ServerProxy ke http://localhost:8000
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000")  # ganti dengan xmlrpc.client.ServerProxy(...)

    print("Memanggil cek_saldo('user1') ... menunggu respons sinkron")
    start = time.time()
    # TODO 2: panggil proxy.cek_saldo("user1") dan cetak hasilnya + waktu tempuh
    #         (buktikan client BENAR-BENAR menunggu sampai server membalas)
    try:
        saldo = proxy.cek_saldo("user_x")
        print(f"Saldo: {saldo}")
    except xmlrpc.client.Fault as e:
        print(f"[ERROR RPC] {e.faultString}")
    print(f"Waktu tempuh: {time.time() - start:.2f} detik (client menunggu sampai server membalas)")

    print("Memanggil proses_pembayaran('user1', 20000) ...")
    # TODO 3: panggil proxy.proses_pembayaran("user1", 20000) dan cetak hasilnya
    try:
        hasil = proxy.proses_pembayaran("user1", 20000)
        print(f"Status: {hasil['status']}")
        print(f"Saldo akhir: {hasil['saldo_akhir']}")
    except xmlrpc.client.Fault as e:
        print(f"[ERROR RPC] {e.faultString}")



if __name__ == "__main__":
    main()
