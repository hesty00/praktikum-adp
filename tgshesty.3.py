#tgs modul 4
# reservasi tiket konser 

print("Selamat Datang di Sistem Reservasi Tiket Konser")
print()
print("Layout Kursi :")
print()

print("--------------------------")
for i in range (6):
    print("|",end =" ")
    for j in range (1,6) :
        Kursi = {i*5 +j}
        print(f"{i*5 +j:>2} |" , end =" ") 
    print()
print("--------------------------")

print()
print("Harga Tiket :")
print()
print("VVIP    : Rp.1.000.000.00")
print("VIP     : Rp.950.000.00")
print("Regular : Rp.850.000.00")
print("Ekonomi : Rp.800.000.00")
print()

Kursi_Terisi = [False] * 30

a = int(input("Masukkan Jumlah Tiket Yang Ingin Dipesan: "))
print()

if a > 30:
    print("Maksimal Tiket Adalah 30")
    a +=1 
else:
    for k in range(1, a + 1):
        print(f"-----PEMESANAN KE-{k}-----")
        print("Masukkan Data Diri")
        nama = input("Nama Anda: ")
        password = input("Masukkan Password : ")
        kategori_tiket = input("Kategori Tiket (VVIP/VIP/Regular/Ekonomi): ")
        if kategori_tiket == "VVIP":
            harga = 1000000
            print("Harga: Rp.1.000.000,00")
            baris_mulai, baris_akhir = 0, 1 
        elif kategori_tiket == "VIP":
            harga = 950000
            print("Harga: Rp.950.000,00")
            baris_mulai, baris_akhir = 2, 4 
        elif kategori_tiket == "REGULAR":
            harga = 850000
            print("Harga: Rp.850.000,00")
            baris_mulai, baris_akhir = 5, 14 
        elif kategori_tiket == "EKONOMI":
            harga = 800000
            print("Harga: Rp.800.000,00")
            baris_mulai, baris_akhir = 15, 29
        else:
            print("Kategori tiket tidak valid.")
            continue
        print()

        print("Status Kursi:")
        for i in range(6): 
            for j in range(5): 
                kursi = i * 5 + j
                if Kursi_Terisi[kursi]:
                    print(f" X", end=" ") 
                else:                   
                    if baris_mulai <= i <= baris_akhir:
                        print(f"{kursi + 1}", end=" ") 
            print()
        while True:
            pilihan_kursi = int(input(f"Masukkan nomor kursi (1-30): ")) - 1
            if baris_mulai <= pilihan_kursi // 5 <= baris_akhir:
                Kursi_Terisi[pilihan_kursi] = True
                print(f"Kursi nomor {pilihan_kursi + 1} dipesan.")
                break
            else:
                print(f"Kursi nomor {pilihan_kursi + 1} tidak tersedia untuk {kategori_tiket}.")

        
        print()
        print("---STRUK PEMESANAN TIKET---")
        print()
        print("NAMA          : {nama}.")
        print("KATEGORI TIKET: {kategori_tiket}.")
        print("PASSWORD      : {password}.")
        print("KURSI         : {pilihan_kursi}.")
        print()
        print("----------SELESAI----------")
        print()

        if k == a :
            print("Pemesanan Anda Selesai")
            break
    k +=1

print()
print("--Status Kursi Setelah Pemesanan:--")
for i in range(6):
    for j in range(5):
        kursi = i * 5 + j
        if Kursi_Terisi[kursi]:
            print(f" X", end=" ")  
        else:
            if baris_mulai <= i <= baris_akhir:
                print(f"{kursi + 1}", end=" ")
            else:
                print("  ", end=" ")
    print()
print("Pemesanan selesai!")
print()


