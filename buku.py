buku = []

def tampil_data():
    if len(buku) <= 0:
        print("Data Masih Kosong")
    else:
        print("Daftar Buku:")
        for i in range(len(buku)):
            print(f"{i}. {buku[i]}")

def tambah_data():
    buku_baru = input("Masukkan Judul Buku: ")
    buku.append(buku_baru)
    print("Data berhasil ditambahkan.")

def edit_data():
    if len(buku) <= 0:
        print("Data Masih Kosong")
    else:
        tampil_data()
        try:
            i = int(input("Inputkan ID buku yang ingin diubah: "))
            if 0 <= i < len(buku):
                judul_baru = input("Masukkan Judul Baru: ")
                buku[i] = judul_baru
                print("Data berhasil diubah.")
            else:
                print("ID tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

def hapus_data():
    if len(buku) <= 0:
        print("Data Masih Kosong")
    else:
        tampil_data()
        try:
            i = int(input("Inputkan ID buku yang ingin dihapus: "))
            if 0 <= i < len(buku):
                buku.pop(i)  # Lebih sederhana dan efisien
                print("Data berhasil dihapus.")
            else:
                print("ID tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

def tampil_menu():
    print("\n" + "="*8 + " Menu " + "="*8)
    print("[1] Tampil Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("[5] Keluar")
    try:
        menu = int(input("Pilih Menu: "))
        print("\n")
        if menu == 1:
            tampil_data()
        elif menu == 2:
            tambah_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            hapus_data()
        elif menu == 5:
            print("Terima kasih! Program selesai.")
            exit()
        else:
            print("Pilihan tidak valid. Masukkan angka 1-5.")
    except ValueError:
        print("Input harus berupa angka.")

if __name__ == "__main__":
    while True:
        tampil_menu()