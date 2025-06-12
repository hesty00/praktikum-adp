import os
import time
from termcolor import colored

def buat_bendera():
    tiang = "║"
    lebar_bendera = 40
    tinggi_bendera = 10
    tinggi_tiang_total = 15
    jarak_tiang = 3
    batas_merah_putih = 5
    lebar_celah = 3 

    while True:
        for putih in range(lebar_bendera + lebar_celah):  
            os.system("cls")

            for baris in range(tinggi_bendera):
                print(tiang + " " * jarak_tiang, end="")
                putih_baris =putih  - baris

                for kolom in range(lebar_bendera):
                    if putih_baris <= kolom < putih_baris + lebar_celah:
                        print(" ", end="")
                    else:
                        if baris < batas_merah_putih:
                            print(colored(" ", on_color="on_red"), end="")
                        else:
                            print(colored(" ", on_color="on_white"), end="")
                print()

            for _ in range(tinggi_tiang_total - tinggi_bendera):
                print(tiang)

            time.sleep(0.07)

buat_bendera()
