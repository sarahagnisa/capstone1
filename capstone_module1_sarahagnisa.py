import math
from tabulate import tabulate
from datetime import datetime

print(f"""
      {'Nama':<10}: SARAH AGNISA SARAGIH
      {'Program':<10}: Job Connector Data Science & Machine Learning""")

print()
print("CAPSTONE MODULE 1")
print()
print('='*100)
print()

print("Python - Pengadaan Barang/Jasa")

data = {
    "NUP" : [1,2,3,4,5,6], # --> Nomor Urut Pengadaan = primary key
    "Jenis" : ["Komputer", "Komputer", "Kursi", "Kursi", "Meja", "Meja"],
    "Merek" : ["Asus", "Apple", "Informa", "Informa", "Informa", "Dekoruma"],
    "Tanggal Pengadaan" : ["31/08/2024", "31/01/2025", "31/01/2025", "14/04/2025", "14/04/2025", "14/04/2025"],
    "Nilai" : [12000000, 14000000, 850000, 850000, 1200000, 1500000]
}

def listMenu():
    print("""
      Menu Pengadaan Barang/Jasa:
      1. Tabel Barang/Jasa
      2. Penambahan Barang/Jasa
      3. Penghapusan Barang/Jasa
      4. Edit Tabel Barang/Jasa
      5. Exit Program
      """)
    
listMenu()

menu = int(input("Silahkan pilih menu yang diinginkan : "))
print()

def tabel():
    print("Tabel Barang/Jasa")
    print()
    print(tabulate(data, headers = data.keys(), tablefmt = "grid"))
    print()

def tambah():
    jenisbaru = input("Masukkan jenis barang/jasa yang ditambah : ")
    merekbaru = input("Masukkan merek barang/jasa tersebut : ")
    nilaibaru = int(input("Masukkan nilai harga barang/jasa tersebut: "))
    data["NUP"].append(data["NUP"][-1]+1)
    data["Jenis"].append(jenisbaru)
    data["Merek"].append(merekbaru)
    tanggalHariIni = datetime.now().strftime("%d/%m/%Y")
    data["Tanggal Pengadaan"].append(tanggalHariIni)
    data["Nilai"].append(nilaibaru)
    print()
    print("Data Berhasil Disimpan dan Ditambahkan!")
    print()
    tabel()
    print()

# print(type(data["NUP"])) # ini cuma memastikan jenis --> list
# print(type(data["NUP"][0])) # ini cuma memastikan jenis --> int

def hapus():
    tabel()
    nuphapus = int(input("Masukkan NUP yang akan di hapus : "))
    print()
    if nuphapus in data["NUP"]:
        index = data["NUP"].index(nuphapus)
        for x in data:
            data[x].pop(index)
            tabel()
    else:
        print("NUP tidak ditemukan")
        print()

def edit():
    tabel()
    nupedit = int(input("Masukkan NUP yang akan di edit :  "))
    print()
    if nupedit in data["NUP"]:
        index = data["NUP"].index(nupedit)
        jenisedit = input(f"{data["Jenis"][index]} --> ")
        merekedit = input(f"{data["Merek"][index]} --> ")
        tanggaledit = input(f"{data["Tanggal Pengadaan"][index]} --> ")
        nilaiedit = int(input(f"{data["Nilai"][index]} --> "))
        data["Jenis"][index] = jenisedit
        data["Merek"][index] = merekedit
        data["Tanggal Pengadaan"][index] = tanggaledit
        data["Nilai"][index] = nilaiedit
        print("Data telah berhasil diperbarui!")
        print()
        tabel()
    else:
        print("NUP tidak ditemukan")
        print()

while True:
    
    if menu == 1:
        tabel()
        menu = int(input("Silahkan pilih menu yang diinginkan : "))

    elif menu == 2:
        tambah()
        print("Apakah ingin menambah barang/jasa lagi? (y/n)")
        tambahlagi = input("> ").lower()
        while True:
            if tambahlagi == "y":
                tambah()
                print("Apakah ingin menambah barang/jasa lagi? (y/n)")
                tambahlagi = input("> ").lower()
            elif tambahlagi == "n":
                listMenu()
                menu = int(input("Silahkan pilih menu yang diinginkan : "))
                break
            else:
                print()
                print("Silahkan ketik y/n")
                tambahlagi = input("> ").lower()
            
    elif menu == 3:
        hapus()
        print("Apakah ingin menghapus barang/jasa lagi? (y/n)")
        hapuslagi = input("> ").lower()
        while True:
            if hapuslagi == "y":
                hapus()
                print("Apakah ingin menghapus barang/jasa lagi? (y/n)")
                hapuslagi = input("> ").lower()
            elif hapuslagi == "n":
                listMenu()
                menu = int(input("Silahkan pilih menu yang diinginkan : "))
                break
            else:
                print()
                print("Silahkan ketik y/n")
                hapuslagi = input("> ").lower()
    
    elif menu == 4:
        edit()
        print("Apakah ingin mengedit barang/jasa lagi? (y/n)")
        editlagi = input("> ").lower()
        while True:
            if editlagi == "y":
                edit()
                print("Apakah ingin mengedit barang/jasa lagi? (y/n)")
                editlagi = input("> ").lower()
            elif editlagi == "n":
                listMenu()
                menu = int(input("Silahkan pilih menu yang diinginkan : "))
                break
            else:
                print()
                print("Silahkan ketik y/n")
                editlagi = input("> ").lower()
    
    elif menu == 5:
        print("Exit Program")
        break
    
    else:
        menu = int(input("Masukkan angka menu yang sesuai : "))
        
