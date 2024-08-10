import csv
import os

# Inisialisasi data barang
barang = {
    '001': {'nama': 'Beras 5kg', 'harga': 67000},
    '002': {'nama': 'Gula', 'harga': 15000},
    '003': {'nama': 'Minyak Goreng', 'harga': 18000},
    '004': {'nama': 'Mie', 'harga': 3100},
    '005': {'nama': 'Susu', 'harga': 15000},
    '006': {'nama': 'Soda', 'harga': 6500},
    '007': {'nama': 'Teh', 'harga': 11000},
    '008': {'nama': 'Keripik Kentang', 'harga': 22500},
    '009': {'nama': 'Permen', 'harga': 8000},
    '010': {'nama': 'Biskuit', 'harga': 10000}
}

# Cek apakah file transaksi.csv sudah ada, jika belum, buat file baru
if not os.path.exists('transaksi.csv'):
    with open('transaksi.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID Barang', 'Nama Barang', 'Harga', 'Jumlah', 'Subtotal'])

# Fungsi untuk menampilkan daftar barang
def tampilkan_daftar_barang():
    print("Daftar Barang:")
    print("ID\tNama Barang\tHarga")
    for id_barang, data in barang.items():
        print(f"{id_barang}\t{data['nama']}\t\t{data['harga']}")

# Fungsi untuk melakukan penjualan
def penjualan():
    total_harga = 0
    total_barang_terjual = 0
    transaksi = []

    while True:
        tampilkan_daftar_barang()

        id_barang = input("Masukkan ID Barang yang ingin dibeli (0 untuk selesai): ")

        if id_barang == '0':
            break

        if id_barang in barang:
            jumlah = int(input("Masukkan Jumlah: "))
            subtotal = barang[id_barang]['harga'] * jumlah
            transaksi.append({'ID Barang': id_barang, 'Nama Barang': barang[id_barang]['nama'], 'Harga': barang[id_barang]['harga'], 'Jumlah': jumlah, 'Subtotal': subtotal})
            total_harga += subtotal
            total_barang_terjual += jumlah
        else:
            print("ID Barang tidak valid. Silakan coba lagi.")

    return transaksi, total_harga, total_barang_terjual

# Fungsi untuk menampilkan detail transaksi
def tampilkan_detail_transaksi(transaksi, total_barang_terjual, total_harga):
    print("\nDetail Transaksi:")
    print("ID\tNama Barang\tHarga\tJumlah\tSubtotal")
    for item in transaksi:
        print(f"{item['ID Barang']}\t{item['Nama Barang']}\t\t{item['Harga']}\t{item['Jumlah']}\t{item['Subtotal']}")
    print(f"\nJumlah Barang Terjual: {total_barang_terjual}")
    print(f"Total Pendapatan: {total_harga}\n")

# Fungsi untuk menyimpan transaksi ke dalam file CSV
def simpan_transaksi(transaksi):
    with open('transaksi.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for item in transaksi:
            writer.writerow([item['ID Barang'], item['Nama Barang'], item['Harga'], item['Jumlah'], item['Subtotal']])

# Fungsi untuk melakukan sorting transaksi berdasarkan ID Barang (Bubble Sort)
def bubble_sort(transaksi):
    n = len(transaksi)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if transaksi[j]['ID Barang'] > transaksi[j + 1]['ID Barang']:
                transaksi[j], transaksi[j + 1] = transaksi[j + 1], transaksi[j]

# Program Utama
while True:
    print("\n===== Program Kasir =====")
    print("1. Penjualan")
    print("2. Lihat Daftar Barang")
    print("3. Lihat Transaksi (Sortir berdasarkan ID Barang)")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        transaksi, total_harga, total_barang_terjual = penjualan()
        tampilkan_detail_transaksi(transaksi, total_barang_terjual, total_harga)
        simpan = input("Apakah ingin menyimpan transaksi? (y/n): ").lower()
        if simpan == 'y':
            simpan_transaksi(transaksi)
            print("Transaksi berhasil disimpan.")
    elif pilihan == '2':
        tampilkan_daftar_barang()
    elif pilihan == '3':
        # Membaca isi file transaksi.csv dan melakukan sorting
        with open('transaksi.csv') as file:
            reader = csv.DictReader(file)
            transaksi = []
            for row in reader:
                transaksi.append({key.strip(): value for key, value in row.items()})
            
            # Debugging: Print all keys in the first transaction
            if transaksi:
                print("Keys in the first transaction:", transaksi[0].keys())

            bubble_sort(transaksi)
            total_barang_terjual = sum(int(item['Jumlah']) for item in transaksi)
            total_harga = sum(int(item['Subtotal']) for item in transaksi)
            tampilkan_detail_transaksi(transaksi, total_barang_terjual, total_harga)
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
