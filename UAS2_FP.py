import re
import os
os.system('cls')
# isi barang
nama_barang = ['beras','gula','tepung','minyak']
jumlah_barang = [3,4,16,32]
harga_barang = [50000,11000,12000,14000]
tanggal_kadaluarsa = ['12-12-2023','10-10-2024','02-06-2023','07-10-2024']
nama_pembeli = []

def show():
   for i in range(len(nama_barang)):
      print('\n','nama barang    :', nama_barang[i],'\n','jumlah(stok barang)    :' ,jumlah_barang [i] ,'\n', 'harga    :' , harga_barang[i],'\n', 'tanggal kadaluarsa     :', tanggal_kadaluarsa[i])
   Menu()

def price ():
   harga_barang2x = list(map(lambda x,n =10: (x-1000)*n , harga_barang)) #mapping
   for i in range(len(nama_barang)):
      print('\n','nama barang    :', nama_barang[i],'\n','jumlah     : 10', '\n', 'harga    :', harga_barang2x[i], '\n', 'Tanggal kadaluarsa    :', tanggal_kadaluarsa[i],'\n')
   Menu()

def few_item ():
   filter_data = list(filter(lambda x : int (x) < 5, jumlah_barang)) # filtering
   print(filter_data)
   print ('jumlah barang    =', len(filter_data))
   for i in range (len(jumlah_barang)):
      if jumlah_barang[i] < 5 :
         print('\n','nama barang    :', nama_barang[i],'\n','jumlah(stok barang)    :' ,jumlah_barang [i] ,'\n', 'harga    :' , harga_barang[i],'\n', 'tanggal kadaluarsa     :', tanggal_kadaluarsa[i])
   Menu()

def sorted_item():
   tampung = []
   for i in range (len(jumlah_barang)):
      tampung2 = [harga_barang[i], nama_barang[i]]
      tampung.append(tampung2)
   tampung3 = sorted(tampung,reverse =False)
   for i in range(len(tampung3)):
      print('Nama Barang   :', tampung[i][1], 'Harga  :', tampung3[i][0])
   Menu()

def sorted_item_reversed():
   tampung = []
   for i in range (len(jumlah_barang)):
      tampung2 = [harga_barang[i],nama_barang[i]]
      tampung.append(tampung2)
   tampung3 = sorted (tampung,reverse = True)
   for i in range (len(tampung3)):
      print(   'Nama Barang   :', tampung3[i][1],' Harga    :', tampung3[i][0])
   Menu()

def palindrom(x):
   return True if len(x) <= 1\
       else palindrom(x[1:-1]) if x[0]==x[-1]\
         else False

def diskon_palindrom(nama_pembeli):
   if palindrom(nama_pembeli) :
      harga_barang2x = list (map(lambda x: x*(50/100), harga_barang)) #mapping
      for i in range (len(nama_barang)):
         print('\n', 'Nama Barang   :' , nama_barang[i], '\n', 'Jumlah  : 10','\n','Harga      :', harga_barang2x[i], '\n','Tanggal Kadaluarsa     :', tanggal_kadaluarsa[i],'\n')
   else:
      print ('Maaf tidak ada diskon buat anda')
   Menu()

def cek(nFormat, text, n, form):
   if nFormat:
      Input = input(f'{text[n]} : ') 
      newFormat = re.search(form[n], Input), cek(newFormat, text, n-1, form[n-1])
   else: isi_data()

def isi_data():
   jumlah_input = input('jumlah input : ')
   for i in range(int(jumlah_input)):
      nama = input('nama barang : ')
      jumlah = input('jumlah barang : ')
      harga = input('harga barang : ')
      tanggal = input('tanggal kadaluarsa : ')
      format = [re.search('\w+', nama), re.search('\d+', harga), re.search('\d+', jumlah), re.search('\d\d-\d\d-\d\d\d\d', tanggal)]
      isi_data() if None in format else nama_barang.append(nama),jumlah_barang.append(jumlah), harga_barang.append(harga),tanggal_kadaluarsa.append(tanggal),Menu()

def Menu():
      print('''
      ========================== M E N U =========================
      |                                                           |
      | 1. Menampilkan barang                                     |
      |-----------------------------------------------------------|
      | 2. Jumlah barang yang stocknya kurang dari 5              |
      |-----------------------------------------------------------|
      | 3. Barang sesuai urutan sesuai harga (dari kecil ke besar)|
      |-----------------------------------------------------------|
      | 4. Barang sesuai urutan sesuai harga (dari besar ke kecil)|
      |-----------------------------------------------------------|
      | 5. Diskon palindrom (event)                               |
      |-----------------------------------------------------------|
      | 6. Harga Grosir                                           |
      |-----------------------------------------------------------|
      | 7. Input Barang                                           |
      |-----------------------------------------------------------|
      | 8. Keluar                                                 |
      =============================================================
      ''')
      menu = int(input('Masukkan kode nomer menu : ')) 
      nama_pembeli=input('masukan nama anda : ')    
      show() if menu==1 else few_item() if menu==2 else sorted_item() if menu==3 else sorted_item_reversed() if menu==4 else diskon_palindrom(nama_pembeli) if menu==5 else price() if menu ==6  else isi_data() if menu==7 else print('semoga harimu menyenangkan') if menu==8 else Menu()
Menu()

