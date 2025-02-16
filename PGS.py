# Import Labraries
import os
from prettytable import PrettyTable 
from datetime import datetime

# File Path:

database_games_file_path = "D:\Purwadhika\Capston\Project_1\Pirates_Games_Database.txt"

# Value Database 
database_games = []

# Fungsi Membaca Database mengguna

def load_database_games():
    global database_games
    if os.path.exists(database_games_file_path):
        with open(database_games_file_path, 'r') as file:
            lines = file.readlines()
            database_games = [line.strip().split(',') for line in lines] 
            for list in database_games:
                list[0] = int(list[0])

# Fungsi untuk mengubah isi dari Database

def save_database_games():
    with open(database_games_file_path, 'w') as file:
        for list in database_games:
            file.write(','.join(map(str, list)) + '\n')


# Fungsi output Menu Utama

def menu_utama():
    print("\n    <<<<====Welcome to====>>>>")
    print("\n<<<<====Pirates Games Store====>>>>")
    print("1. Daftar Games")
    print("2. ADD Data Games")
    print("3. Update Data Games")
    print("4. Delete Data Games")
    print("5. Order Games")
    print("6. Exit")
    print("<<<<<<<<<<<<<<<<<<<<.>>>>>>>>>>>>>>>>>>>>")

# Fungsi Menu 1 "Daftar Games"

def list_games():
    print("\n=====>>>>> Daftar Games <<<<<=====")
    print("1. Daftar Games")
    print("2. Cari Berdasarkan Games ID")
    print("3. Cari Berdasarkan Genre")
    print("4. Kembali ke Menu Utama")
    print('<<<<<<<<<<<<<<<--------->>>>>>>>>>>>>>>\n')
    sub_menu = input("Pilih nomor menu 1-4: ")

    if sub_menu == '1':
        menampilkan_list(database_games)
        return list_games()
    elif sub_menu == '2':
        cari_id_games = games_id("Masukan ID Games: ", is_integer=True) 
        matching_lists = [list for list in database_games if list[0] == int(cari_id_games)]
        menampilkan_list(matching_lists)
        return list_games()
    elif sub_menu == '3':
        print("\n<<<Daftar Genre>>>")
        unique_genres = set(list[2] for list in database_games)
        for genre in unique_genres:
            print(f"- {genre}")
        print("<<<<<<----------->>>>>>")
        genre_games_input = genre_games("Masukkan Genre Games: ", daftar_genre)
        matching_lists = [list for list in database_games if list[2].lower() == genre_games_input.lower()]
        menampilkan_list(matching_lists)
        return list_games()
    elif sub_menu == '4':
        return
    else:
        print("Error! Tolong hanya memasukan angka menu 1-4")
        return list_games()

def menampilkan_list(lists):
    if not lists:
        print("List tidak ditemukan")
        return list_games()
        
# Output dalam bentuk PrettyTable
    table = PrettyTable()
    table.field_names = ["Games ID", "Name", "Genre", "Reales Date", "Type"]

    for list in lists:
        if len(list) == len(table.field_names):
            table.add_row(list)

    print(table)

# Fungsi menu 2 "Add Data Games"

def menambah_data_games() :
    print("\n<<<<---Add Data Games--->>>>")
    print("1. Masukan Data Games Baru")
    print("2. Kembali ke Menu Utama")
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')
    sub_menu = input("Pilih nomor menu 1-2: ")

    if sub_menu == '1' :
        return tambah_games()
    elif sub_menu == '2' :
        return
    else :
        print("Error! Tolong hanya memasukan angka menu 1-2")
        return menambah_data_games()

def tambah_games():
    print("\n<<<<---Menambah Data Games--->>>>")
    Games_ID = games_id("Masukan Games ID: ", is_integer=True)

    if any(list[0] == Games_ID for list in database_games):
        print("Games ID sudah ada! Tidak dapat menambahkan ID serupa.")
        return menambah_data_games()

    Name = nama_games("Masukan Nama Games: ")
    Genre_Games = tambah_genre("Masukan Genre Games : ")
    Reales_Date = reales_date_games("Masukkan tanggal rilis (DD-MM-YYYY): ")
    Type_Games = type_games("Masukan type games (Exclusive/Reguler): ")
    
    list = [Games_ID, Name, Genre_Games, Reales_Date, Type_Games]

    print("\nGame yang ditambahkan pada Daftar Games:")
    menampilkan_list([list])
    Konfirmasi_input = input("Apakah ada yakin ingin menambakan game ini? (ketik ya untuk konfirmasi): ").lower()

    if Konfirmasi_input == 'ya':
        database_games.append(list)
        save_database_games()
        print("Game berhasil ditambahkan!")
        return menambah_data_games()
    else:
        print("Game gagal ditambahkan")
        return menambah_data_games()

# Fungsi menu 3 "Update Data Games"

def update_data_games() :
    print("\n=========Update Data Games=========")
    print("1. Update Data Games yang sudah ada")
    print("2. Kembali ke Menu utama")
    print('*************************************\n')
    sub_menu = input("pilih nomor menu 1-2: ")

    if sub_menu == '1' :
        return update_games()
    elif sub_menu == '2' :
        return
    else :
        print("Error! Tolong hanya memasukan angka menu 1-2")
        return update_data_games()
    
def update_games():
    print("\n*******Update Data Games*******")
    cari_id_games = games_id("Masukan Games ID untuk memperbaharui data: ", is_integer=True)
    matching_lists = [list for list in database_games if list[0] == int(cari_id_games)]

    if not matching_lists:
        print("Tidak ada Games ID didalam Daftar Games. Tolong input ID yang benar!")
        return update_data_games()
    
    menampilkan_list(matching_lists)
    Konfirmasi_input = input("Apakah anda yakin akan memperbaharui data game ini? (ketik ya untuk konfirmasi): ").lower()

    if Konfirmasi_input != 'ya':
        print('Memperbaharui data dibatalkan!')
        return update_data_games()

    elif Konfirmasi_input == 'ya':
        id_games = [list[0] for list in database_games]
        id_baru = input("Masukan ID Games yang baru: ")
        if int(id_baru) in id_games :
            print('Tidak dapat memperbaharui ke ID yang sudah ada dalam Database')
            return update_games()
        nama_baru = nama_games("Masukan nama Game yang baru: ")
        genre_baru = tambah_genre("Masukan genre games : ")
        tanggal_rilis_baru = reales_date_games("Masukan Tanggal rilis yang baru (DD-MM-YYYY): ")
        type_game_baru = type_games("Masukan type games (Exclusive/Reguler): ")

        updated_list = [id_baru, nama_baru, genre_baru, tanggal_rilis_baru, type_game_baru]
       
        print("\nBerikut data Game yang sudah diperbaharui:")
        menampilkan_list([updated_list])
    Konfirmasi_input = input("Apakah anda yakin untuk memperbaharui data Game ini? (ketik ya untuk konfirmasi): ").lower()

    if Konfirmasi_input == 'ya':
        database_games.remove(matching_lists[0])
        database_games.append(updated_list)
        save_database_games()
        print("Data Game sudah diperbaharui!.")
        return update_data_games()
    else:
        print("Memperbaharui data dibatalkan")
        return update_data_games()

# Fungsi menu 4 "Delete Data Games"
    
def delete_data_games() :
    print("\n-------------Delete Data Games-------------")
    print("1. Hapus Data Games yang sudah ada")
    print("2. Kembali ke Menu Utama")
    print('---------------------------------------\n')
    sub_menu = input("Pilih nomor menu 1-2: ")

    if sub_menu == '1' :
        return delete_game()
    elif sub_menu == '2' :
        return
    else :
        print("Error! Tolong hanya memasukan angka menu 1-2")
        return delete_data_games()
    
def delete_game():
    print("\n========Delete Data Games========")
    cari_id_games = games_id("Masukan ID Game yang akan dihapus: ", is_integer=True)
    matching_lists = [list for list in database_games if list[0] == int(cari_id_games)]

    if not matching_lists:
        print("Tidak ada ID didalam Daftar Games!")
        return delete_data_games()
    
    menampilkan_list(matching_lists)
    Konfirmasi_input = input("Apakah anda yakin akan menghapus Game ini? (ketik 'ya' untuk konfirmasi): ").lower()

    if Konfirmasi_input == 'ya':
        database_games.remove(matching_lists[0])
        print("Data Game telah dihapus!")
        return delete_data_games()
    else:
        print("Data Game gagal dihapus!")
        return delete_data_games()

# Fungsi menu 5 "Order Games"

def menu_order_games() :
    print("\n<<<<--- Order Games --->>>>")
    print("1. Order Games")
    print("2. Kembali ke Menu Utama")
    print('********************************\n')
    sub_menu = input("Pilih nomor menu 1-2: ")

    if sub_menu == '1' :
        return order_games()
    elif sub_menu == '2' :
        return
    else :
        print("Error! Tolong hanya memasukan angka menu 1-2")
        return menu_order_games()

def order_games():
    print("\n<<<<--- Order Games --->>>>")
    
    if not database_games:
        print("Belum ada game yang tersedia untuk diorder.")
        return
    
    menampilkan_list(database_games)
    
    print("\n*****Harga Game*****")
    print("- Game Exclusive: Rp100.000")
    print("- Game Reguler: Rp50.000")

    keranjang_pembelian = []
    id_dalam_keranjang = set ()
    total_harga = 0
    
    while True:
        try:
            Games_ID = input("Masukkan Games ID yang ingin diorder (0 untuk selesai): ").strip()
            
            if Games_ID == "0":
                if not keranjang_pembelian:
                    print("Anda belum memilih game. Silakan pilih minimal satu game.")
                    continue
                break
            
            if not (Games_ID.isdigit() and len(Games_ID) == 5):
                print("Error! Input salah! Tolong input hanya berisi 5 digit angka!")
                continue
            
            Games_ID = int(Games_ID)
            
            if Games_ID in id_dalam_keranjang:
                print(f"Game '{Name}' sudah ada dalam keranjang")
                continue
            
            matching_list = next((list for list in database_games if list[0] == Games_ID), None)
            
            if matching_list:
                Name, Type_Games = matching_list[1], matching_list[4]
                
                if Type_Games.lower() == "exclusive" :
                    harga = 100000 
                else :
                    harga = 50000
                
                keranjang_pembelian.append((Name, Type_Games, harga))
                id_dalam_keranjang.add(Games_ID)
                total_harga += harga
                print(f"Game '{Name}' berhasil ditambahkan ke daftar order.")
            else:
                print("Games ID tidak ditemukan! Silakan coba lagi!")

        except ValueError:
            print("Masukkan angka yang valid untuk Games ID!")


    print("\nGame yang Anda pesan:")
    for game in keranjang_pembelian:
        print(f"- {game[0]} ({game[1]}) - Rp{game[2]:,}")
    
    print(f"\nTotal harga: Rp{total_harga:,}")

    while True:
        try:
            pembayaran = int(input("Masukkan jumlah pembayaran: Rp"))
            if pembayaran < total_harga:
                print("Uang yang dimasukkan kurang! Silakan masukkan jumlah yang cukup.")
            else:
                kembalian = pembayaran - total_harga
                print(f"\nPembayaran berhasil! Kembalian Anda: Rp{kembalian:,}")
                print("==Terima kasih telah melakukan order!==\n")
                return menu_order_games()
        except ValueError:
            print("**Masukkan angka yang valid untuk pembayaran**")

# Fungsi input dalam Database Games

def games_id(prompt, is_integer=True):
    while True:
        try:
            value = input(prompt)
            if value.isdigit and len(value) == 5 and int(value) >= 0 :
                    return int(value)
            else:
                raise ValueError("Error! Harus berisikan 5 digit angka!")
        except ValueError:
            print("Error! Input salah!. Tolong input hanya berisikian 5 digit angka!")

def genre_games(prompt, daftar_genre):
    daftar_genre = [genre.lower() for genre in daftar_genre]
    while True:
        try:
            value = input(prompt).strip()
            if value.lower() in daftar_genre:
                return value
            else:
                raise ValueError("Error! Genre yang dicari tidak ada pada daftar genre!")
        except ValueError as g:
            print(g)

daftar_genre = ["Action RPG","Action Adventure","First Person Shooter","Open World"]

def tambah_genre(prompt):
    while True:
        try:
            velue = input(prompt).strip()
            if velue:
                daftar_genre.append(velue)
                return velue
            else:
                raise ValueError("Error! Genre games tidak boleh kosong, minimal 1 karakter.")
        except ValueError as e:
            print(e)

def reales_date_games(prompt):
    while True:
        try:
            date_input = input(prompt)
            valid_date = datetime.strptime(date_input, "%d-%m-%Y")
            return valid_date.strftime("%d-%m-%Y")
        except ValueError:
            print("Error! Tanggal tidak ditemukan. Format tanggal harus DD-MM-YYYY!")

def type_games(prompt):
    while True:
        type_input = input(prompt).lower()
        if type_input in ["exclusive", "reguler"]:
            return type_input
        else:
            print("Error! Tipe harus 'exclusive' atau 'reguler'.")

def nama_games(prompt):
    while True:
        try:
            name = input(prompt).strip()
            if len(name) > 0:
                return name
            else:
                raise ValueError("Error! Harus memasukan minimal 1 karakter.")
        except ValueError as i:
            print(i)

# Funsi Menu Utama

load_database_games()

while True:
    menu_utama()
    pilih_menu = input("Pilih nomor menu 1-6: ")

    if pilih_menu == '1':
        list_games()
    elif pilih_menu == '2':
        menambah_data_games()
        save_database_games()
    elif pilih_menu == '3':
        update_data_games()
        save_database_games()
    elif pilih_menu == '4':
        delete_data_games()
        save_database_games()
    elif pilih_menu == '5':
        menu_order_games()
    elif pilih_menu == '6':
        print('''Terima Kasih telah berkunjung di Pirate Game Store!''')
        break
    else:
        print("Error! Tolong hanya memasukan angka menu 1-6")