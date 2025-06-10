
DATA_FILE = "data_keuangan.txt"

def buat_file_jika_belum_ada():
    f = open(DATA_FILE, "a")
    f.close()


def load_data():
    buat_file_jika_belum_ada()
    data = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = {}
            parts = line.split(";")
            for part in parts:
                if "=" in part:
                    key, value = part.split("=", 1)
                    if key == "jumlah":
                        value = int(value)
                    item[key] = value
            if item:
                data.append(item)
    return data

def save_data(data):
    with open(DATA_FILE, "w") as f:
        for item in data:
            parts = []
            for k, v in item.items():
                parts.append(f"{k}={v}")
            line = ";".join(parts)
            f.write(line + "\n")

def tampilkan_data(data):
    if not data:
        print("\n Belum ada data keuangan.\n")
    else:
        print("\n📋 Data Keuangan:")
        print("-" * 60)
        for i, item in enumerate(data):
            print(f"{i+1}. Tanggal     : {item['tanggal']}")
            print(f"   Keterangan : {item['keterangan']}")
            print(f"   Jumlah     : Rp {item['jumlah']:,}")
            print(f"   Tipe       : {item['tipe']}")
            print("-" * 60)
        print()

def tambah_data(data, tanggal, keterangan, jumlah, tipe):
    if isinstance(jumlah, int) and tipe in ["pemasukan", "pengeluaran"]:
        data.append({
            "tanggal": tanggal,
            "keterangan": keterangan,
            "jumlah": jumlah,
            "tipe": tipe
        })
        save_data(data)
        print(" Data berhasil ditambahkan!\n")
    else:
        print("Input tidak valid.\n")

def hapus_data(data, nomor):
    if 0 <= nomor - 1 < len(data):
        keterangan_dihapus = data[nomor - 1]['keterangan']
        del data[nomor - 1]
        save_data(data)
        print(f"Data '{keterangan_dihapus}' berhasil dihapus.\n")
    else:
        print("Nomor data tidak ditemukan.\n")

def hanya_angka(s):
    angka = "0123456789"
    for char in s:
        if char not in angka:
            return False
    return True

data = load_data()

tanggal = input("Masukkan tanggal (YYYY-MM-DD): ").strip()
keterangan = input("Masukkan keterangan: ").strip()
jumlah_input = input("Masukkan jumlah (angka): ").strip()
tipe = input("Masukkan tipe (pemasukan/pengeluaran): ").strip().lower()

if hanya_angka(jumlah_input) and tipe in ["pemasukan", "pengeluaran"]:
    jumlah = int(jumlah_input)
    tambah_data(data, tanggal, keterangan, jumlah, tipe)
else:
    print("⚠ Input tidak valid. Jumlah harus angka dan tipe harus benar.\n")

tampilkan_data(data)

hapus = input("Ingin menghapus data? (y/n): ").strip().lower()
if hapus == "y":
    nomor_input = input("Masukkan nomor data yang ingin dihapus: ").strip()
    if hanya_angka(nomor_input):
        nomor = int(nomor_input)
        hapus_data(data, nomor)
        tampilkan_data(data)
    else:
        print("Nomor tidak valid.\n")
