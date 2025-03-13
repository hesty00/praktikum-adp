print("Tugas ADP : pemesanan makanan online")

#TAMPILAN 1
#DAFTAR PAKET MAKANAN(daftar paket & harga makanan)

print('                     DAFTAR MENU                       ')
print('_'*56) #tutup atas
print('| Paket |               Isi             |    Harga     |')
print('_'*56) 
print('|   A   |    Ikan Bakar & Teh           |   Rp.22.000  |')
print('|   B   |    Ikan Goreng & Teh          |   Rp.22.000  |')
print('|   C   |    Nasi Goreng & Lemon Tea    |   Rp.20.000  |')
print('|   D   |    Sate Ayam & Kopi           |   Rp.23.000  |')
print('|   E   |    Bakmi Rebus & Es Campur    |   Rp.23.000  |')
print('_'*56) #tutup bawah
print()
print()
#TAMPILAN 2
#1 INPUT DATA DIRI(nama,no telp,alamat)

print("DATA DIRI PELANNGAN")
nama = input("Nama Anda : ")
no_telfon = input("Nomor Telfon Anda : ")
alamat = input("Alamat Pengiriman Anda : ")
print()

#2 MEMILIH JUMLAH & PAKET(ketentuan biaya)
#  a.pajak 10% dari total harga
print("Setiap Pembelian Akan Mendapat Pajak 10%")
Beli = input("PILIH PAKET MENU (A, B, C, D, E),  :")
Jumlah_item = int(input("Jumlah Pesanan :"))
if Beli == "A" :
   Menu = ("Ikan Bakar & Teh")
   Harga_per_item = 22000
elif Beli == "B":
   Menu = ("Ikan Goreng & Teh")
   Harga_per_item = 22000
elif Beli == "C":
   Menu = ("Nasi Goreng & Lemon Tea")
   Harga_per_item = 20000
elif Beli == "D":
   Menu = ("Sate Ayam & Kopi")
   Harga_per_item = 23000
elif Beli == "E":
   Menu = ("Bakmi Rebus & Es Campur ")
   Harga_per_item = 23000
else :
   Harga_per_item = print("pilihan paket tidak tersedia")
print()
Total_Harga = Jumlah_item*Harga_per_item 
Pajak = Total_Harga * 0.10
Bayar = Total_Harga + Pajak 
print(f"Harga Makanan Yang Harus Di Bayar : Rp {Bayar}")

#  b.biaya pengiriman
#    total harga < Rp.150.000 biaya pengiriman Rp.25.000
#    total harga>=Rp.150.000 biaya pengiriman Rp.0
print()
print()
print("TOTAL PEMBAYARAN & BIAYA PENGIRIMAN")
if Bayar < 150000 :
   biaya_pengiriman = 25000
   Total = Bayar + biaya_pengiriman
   print(Bayar, "Total Harga Yang Harus Di Bayar : Rp {Total}")
else :
   biaya_pengiriman = 0
   Total = Bayar + biaya_pengiriman
   print(Bayar, "Total Harga Yang Harus Di Bayar : Rp {Total}")
print()
TOTAL_AKHIR = biaya_pengiriman + Pajak + Total_Harga,
print()
print()

#3 MENAMPILKAN STRUK PEMBAYARAN
#detail pembayaran


print('               STRUK PEMBAYARAN               ')
print("Nama Anda                  :",nama)
print("Nomor Telepon Anda         :", no_telfon)
print("Alamat Anda                :", alamat)
print()
print("DETAIL PESANAN , "
"\nPaket                      :", Beli ,"\nDengan Menu                :", Menu)
print("Jumlah Pesanan Anda        :", Jumlah_item)
print()
print("Total Harga                :", Total_Harga)
print("Pajak                      :", Pajak)
print("Biaya Pengiriman           :", biaya_pengiriman)
print()
print("TOTAL AKHIR                :", TOTAL_AKHIR)
print()


