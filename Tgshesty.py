#tgs praktikum modul aray
print("")
data_mahasiswa =[]
while True :
    print("-----MANAJEMEN NILAI MAHASISWA-----")
    print("1.Tambah Data")
    print("2.Hapus Data")
    print("3.Tampilkan Data")
    print("4.Keluar")
    print("")
    pilihan = int(input("Pilih {1/2/3/4} :"))

    if pilihan == 1:
        nama= input("Masukan Nama : ")
        nilai= input("Masukan nilai: ")
        nilai=float(nilai)
        nomor= input("Masukan Nomor Mahasiswa: ")
        data_mahasiswa.append([nama,nilai,nomor])
        print("Data Mahasiswa Berhasil Ditambahkan")
        print(data_mahasiswa)

    elif pilihan ==2:
        nomor= input("Masukan Nomor Mahasiswa yang Mau Dihapus: ")
        ditemukan = False
        for i in range (len(data_mahasiswa)) :
            if data_mahasiswa[i][2]==nomor:
                del data_mahasiswa[i]
                print("Data Mahasiswa Berhasil Dihapus")
                print(data_mahasiswa)
                ditemukan = True
                break
            else :
                print("Data Mahasiswa Tidak Ditemukan")

    elif pilihan == 3:
        if len(data_mahasiswa) ==0:
            print("Data Mahasiswa Belum Dimasukkan")
        else:
            for i in range(len(data_mahasiswa)):
                for j in range(i+1, len(data_mahasiswa)):
                    if data_mahasiswa[i][2] < data_mahasiswa[j][2]:
                        data = data_mahasiswa[i]
                        data_mahasiswa[i]=data_mahasiswa[j]
                        data_mahasiswa[j]= data
            print(" ")
            print("\n=== DAFTAR MAHASISWA ===")
            print(f"{'Nomor. Mahasiswa':<15} {'Nama':<20} {'Nilai':<10}")
            
            for mhs in data_mahasiswa:
                print(f"{mhs[2]:<15} {mhs[0]:<20} {mhs[1]:<10.2f}")

           
            
    elif pilihan ==4:
        print("Program Selesai")
    else :
        print("Pilihan Tidak Valid")






