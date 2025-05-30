def input_data():
    jumlah = int(input("Masukkan jumlah praktikan: "))
    data = []

    for i in range(jumlah):
        print("\nPraktikan ke-", i+1)
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai Pretest: "))
        postest = float(input("Nilai Postest: "))
        tugas = float(input("Nilai Tugas/Makalah: "))
        bonus = float(input("Nilai Bonus: "))
        nilai_akhir = 0
        peringkat = 0
        data.append([nama, nim, pretest, postest, tugas, bonus, nilai_akhir, peringkat])

    return data

def hitung_rata_rata(data):
    total_pretest = 0
    total_postest = 0
    total_tugas = 0
    n = 0

    for i in data:
        total_pretest = total_pretest + i[2]
        total_postest = total_postest + i[3]
        total_tugas = total_tugas + i[4]
        n = n + 1

    rata_pre = total_pretest / n
    rata_post = total_postest / n
    rata_tugas = total_tugas / n

    return rata_pre, rata_post, rata_tugas

def hitung_nilai_akhir(data):
    for i in data:
        nilai = 0.25 * i[2] + 0.25 * i[3] + 0.5 * i[4] + i[5]
        i[6] = nilai  

def hitung_rata_nilai_akhir(data):
    total = 0
    jumlah = 0
    for i in data:
        total = total + i[6]
        jumlah = jumlah + 1
    return total / jumlah

def urutkan_nilai_akhir(data):
    n = len(data)
    for i in range(n):
        for j in range(n - 1):
            if data[j][6] < data[j + 1][6]:
                data[j], data[j + 1] = data[j + 1], data[j]

def beri_peringkat(data):
    for i in range(len(data)):
        data[i][7] = i + 1

def tampilkan_tabel(data, rata2_nilai):
    print("\n=== TABEL NILAI PRAKTIKAN ===")
    print(f"{'Nama':<16} {'NIM':<12} {'Nilai Akhir':<15} {'Peringkat':<10}")
    print("-" * 60)
    for i in data:
        print(f"{i[0]:<16} {i[1]:<12} {i[6]:<15} {i[7]:<10}")
    print("-" * 60)
    print("Rata-rata Nilai Akhir:", rata2_nilai)


data = input_data()
r1, r2, r3 = hitung_rata_rata(data)
hitung_nilai_akhir(data)
rata2_akhir = hitung_rata_nilai_akhir(data)
urutkan_nilai_akhir(data)
beri_peringkat(data)
tampilkan_tabel(data,rata2_akhir)



