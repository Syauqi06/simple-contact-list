import pandas as pd

kontak = pd.DataFrame(columns=["Nama", "Nomor", "Email"])

def tambah_kontak():
    global kontak
    nama = input("Masukan nama: ")
    nomor = input("Masukan nomor telepon: ")
    email = (input("Masukan email: "))
    kontak_baru = pd.DataFrame([[nama, nomor, email]], columns = ["Nama", "Nomor", "Email"])
    kontak = pd.concat([kontak, kontak_baru], ignore_index=True)
    print("Kontak berhasil ditambah")

def tampil_kontak():
    if kontak.empty:
        print("Belum ada kontak yang tersimpan")
    else:
        print("\nDaftar Kontak:")
        print(kontak.rename_axis(None).set_index(pd.Index(range(1, len(kontak) + 1))))

def cari_kontak():
    keyword = input("Masukan nama atau nomor yang ingin anda cari: ")
    cari = kontak[
        kontak["Nama"].str.contains(keyword, case=False, na=False) |
        kontak["Nomor"].str.contains(keyword, case=False, na=False)
    ]
    if not cari.empty:
        print("\nHasil Pencarian:")
        print(cari)
    else:
        print("Kontak tidak ditemukan")

def hapus_kontak():
    global kontak
    nama_hapus = input("Masukan nama kontak yang ingin dihapus: ")
    if not kontak[kontak["Nama"] == nama_hapus].empty:
        kontak.drop(kontak[kontak["Nama"] == nama_hapus].index, inplace=True)
        print("Kontak berhasil dihapus")
    else:
        print("Kontak tidak ditemukan")

    
def main():
    while True:
        print("\n" + 16* "=")
        print("1. Tambah Kontak")
        print("2. Daftar Kontak")
        print("3. Cari Kontak")
        print("4. Hapus Kontak")
        print("5. Keluar")
        pilih = input("Pilih menu (1-5): ")
        if pilih == "1":
            tambah_kontak()
        elif pilih == "2":
            tampil_kontak()
        elif pilih == "3":
            cari_kontak()
        elif pilih == "4":
            hapus_kontak()
        elif pilih == "5":
            print("Out")
            break
        else:
            print("Input yang bener kocak")

if __name__ == "__main__":
    main()