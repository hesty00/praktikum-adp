from termcolor import colored

def print_papan(papan, posisi_menang=None):
    print()
    for i in range(3):
        baris_elems = []
        for j in range(3):
            sel = papan[i][j]
            if posisi_menang and (i, j) in posisi_menang:
                baris_elems.append(colored(str(sel), "red", attrs=["bold"]))
            else:
                baris_elems.append(str(sel))
        baris = " | ".join(baris_elems)
        if i < 2:
            print(" " + baris+ "\n-----------")
        else:
            print(" " + baris)
    print()

def untuk_posisi_menang(posisi_pemain):
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
    ]
    for line in lines:
        if all(posisi_pemain[r][c] for r,c in line):
            return line
    return None

def play_game():
    nama_x = input("Masukkan nama pemain X: ")
    nama_o = input("Masukkan nama pemain O: ")

    hasil_akhir = {}

    papan = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    posisi_x = [[False]*3 for _ in range(3)]
    posisi_o = [[False]*3 for _ in range(3)]

    lokasi = [str(i) for i in range(1, 10)]
    total = 0
    menang = None
    posisi_menang= None

    print_papan(papan)

    while True:
        # Cek kemenangan X
        posisi_menang = untuk_posisi_menang(posisi_x)
        if posisi_menang:
            print_papan(papan, posisi_menang)
            print(f"{nama_x} (X) menang!")
            hasil_akhir["Pemenang"] = nama_x
            break

        # Cek kemenangan O
        posisi_menang= untuk_posisi_menang(posisi_o)
        if posisi_menang:
            print_papan(papan, posisi_menang)
            print(f"{nama_o} (O) menang!")
            hasil_akhir["Pemenang"] = nama_o
            break

        # Cek seri
        if total == 9:
            print_papan(papan)
            print("Hasil Seri!")
            hasil_akhir["Pemenang"] = "Seri"
            break

        if total % 2 == 0:
            si_pemain = "X"
            nama = nama_x
            posisi_si_pemain = posisi_x
        else:
            si_pemain = "O"
            nama = nama_o
            posisi_si_pemain = posisi_o

        valid_input = False
        while not valid_input:
            data = input(f"{nama} ({si_pemain}), pilih posisi (1-9): ")
            if data not in lokasi:
                print("Posisi sudah terisi atau tidak valid! Coba lagi.")
                continue
            try:
                posisi = int(data)
                if posisi < 1 or posisi > 9:
                    print("Masukkan angka antara 1 sampai 9!")
                    continue
            except ValueError:
                print("Input harus berupa angka antara 1 sampai 9!")
                continue
            valid_input = True

        lokasi.remove(data)
        total += 1

        baris = (posisi - 1) // 3
        kolom = (posisi - 1) % 3
        papan[baris][kolom] = si_pemain
        posisi_si_pemain [baris][kolom] = True

        print_papan(papan)

    input("Tekan ENTER untuk melanjutkan ke sesi berikutnya...")

    with open("pemenang.txt", "a") as file:
        file.write(f"Pemenang: {hasil_akhir['Pemenang']}\n")

    print("\n" + "=" * 30 + "\n")
    
if __name__ == "__main__":
    while True:
        play_game()
        ulang = input("Apakah Anda ingin bermain lagi? (y/n): ")
        if ulang.lower() != "y":
            print("Terima kasih sudah bermain!")
            break