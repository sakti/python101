================
Input dan Output
================

Akan ada situasi dimana program yang anda buat harus berinteraksi
dengan pengguna. Sebagai contoh program anda ingin mendapatkan inputan
pengguna kemudian mencetak hasil operasi program. Kita dapat melakukannya
menggunakan fungsi ``raw_input`` dan statemen ``print``.

Selain itu salah satu input/output yang umum yaitu operasi file. Kemampuan
untuk membuat, membaca dan menulis file.

Input dari Pengguna
===================

::

   # lat36.py

   def balik_string(teks):
       return teks[::-1]

   def apakah_palindrom(teks):
       return teks == balik_string(teks)

   inputan = raw_input('Masukkan teks: ')

   if apakah_palindrom(inputan):
       print 'Ya, inputan berupa palindrom'
   else:
       print 'Tidak, inputan bukan palindrom'

File
====

Anda bisa membuka dan menggunakan file untuk membaca atau
menulis dengan membuat ``file`` obyek.

::

   # lat37.py

   teks = """ini adalah isi dari file
   yang akan ditulis
   menggunakan python"""

   # membuka dengan mode tulis
   f = open('coba.txt', 'w')
   f.write(teks)
   f.close()

   # default membuka file dengan mode baca
   f = open('coba.txt')
   while True:
       baris = f.readline()
       if len(baris) == 0:
           # EOF
           break
       print baris,
   f.close()

Pickle
======

Python menyediakan modul ``pickle`` untuk menyimpan obyek Python kedalam file dan
membaca obyek Python dari file.

::

   # lat38.py

   import pickle

   daftar_belanja_file = 'daftar.data'
   daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
   
   # membuka file penyimpanan obyek dengan mode tulis binary
   f = open(daftar_belanja_file, 'wb')

   # dump obyek ke file
   pickle.dump(daftar_belanja, f)
   f.close()

   # hapus daftar_belanja dari memori
   del daftar_belanja

   # membaca dari file
   f = open(daftar_belanja_file, 'rb')
   daftar_tersimpan = pickle.load(f)
   print daftar_tersimpan