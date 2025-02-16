# **Pirates-Games-Store-Program**

**Pirates-Games-Store-Program** adalah aplikasi berbasis teks yang memungkinkan user untuk mengelola database game serta user dapat order game by game ID. 

## Program ini berisikan:

1. **Daftar Game**, Program ini berisikan 3 sub menu yang dimana:
    - user dapat menampilkan kesuluran data
    - user dapat mencari data berdasarkan Game ID
    - user dapat mencari data berdasarkan genre games
3. **Add Data Game**, Program ini diperuntukan untuk menambahkan data game baru pada database
4. **Update Data Game**, Program ini diperuntukan untuk memperbaharui data game yang berada pada database
5. **Delete Dara Game**, Program ini diperuntukan untuk menghapus data game yang yang berada pada database
6. **Order Game**, program ini diperuntukan untuk user yang ingin membeli atau memesan game berdasarkan Game ID yang tertera pada daftar game

Data game disimpan dalam file Priates_Games_Database.txt dengan format txt sederhana.
  
## Persyaratan Penggunaan Program
1. **SistemPython 3.x***
2. **File database_games.txt untuk menyimpan data game**

## Import Labraries dalam Python
1. **OS**, agar python dapat membaca file yang ada pada perangkat
2. **PrettyTable**, untuk menampilkan Database dengan output table yang rapih
3. **Datetime**, untuk mengimport data real tanggal berdasarkan Masehi

## Fromat Data dalam Priates_Games_Database.txt
setiap game disimpan pada format berikut:

    Games ID, Nama, Genre, Tanggal Rilis, Tipe

Contoh:

    |-- 83270,Assassins Creed Odyssey,Action RPG,05-10-2018,Exclusive
    |-- 58569,Batman: Arkham City,Action Adventure,18-10-2011,Reguler


## Struktur dalam Project ini
repository-Pirates-Games-Store_program:

    │-- PGS.py                            --> File utama Program Pirates Games Store berbasis Python
    │-- Pirates_Games_Database.txt        --> File penyimpanan Database
    │-- README.txt                        --> Dokumentasi isi dari Program Pirates Games Store
    |-- Flowchart Pirates Games Store.pdf --> Flowchart yang saya gunakan dalam project program in
