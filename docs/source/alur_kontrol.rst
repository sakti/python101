============
Alur Kontrol
============

Di dalam program yang kita lihat hingga saat ini, selalu saja urutan statemen
yang dijalankan oleh Python berurutan dari atas ke bawah. Bagaimana jika 
Anda ingin mengubah alur kerjanya? Sebagai contoh Anda ingin 
program untuk mengambil keputusan dan bertindak secara berbeda tergantung
pada kondisi yang ada. Sebagai contoh, misalnya mencetak 'Selamat Pagi' 
atau 'Selamat Sore' tergantung waktu yang ada saat itu?

Sebagaimana yang Anda sudah bisa tebak, ini dapat dilakukan lewat statemen 
alur kontrol. Ada tiga macam statemen alur kontrol di Python - 
``if``, ``for`` dan ``while``.


Statemen If
===========

Statemen ``if`` digunakan untuk mengecek kondisi: jika kondisi ``if`` 
bernilai benar, maka kita akan menjalankan satu blok statemen 
(disebut ``if-block``), jika tidak akan diteruskan dengan statemen  ``else`` 
kita gunakan untuk memproses blok statemen yang lain 
(dinamakan ``else-block``). Bagian ``else`` tersebut sifatnya tidak wajib atau
opsional.

Kita dapat menambahkan kondisi dalam ``else-block`` mengunakan ``elif``.

.. code-block:: python
   :emphasize-lines: 11,12,14,16
   :linenos:
   
   # lat9.py

   nomor_acak = 7
   print 'tebak nomor acak dari 1 - 10'

   # ``raw_input`` digunakan untuk mendapatkan input dari pengguna
   # ``int`` digunakan untuk konversi tipe data ``str`` ke ``int``
   tebakan = int(raw_input('Tebakan anda (bil bulat): '))

   if tebakan == nomor_acak:
       print 'Selamat! tebakan anda benar'
       print 'tapi tidak ada hadiah untuk anda :('
   elif tebakan < nomor_acak:
       print 'tebakan anda terlalu kecil'
   else:
       print 'tebakan anda terlalu besar'

   print 'selesai'

.. note::
   Baris 11-12 adalah ``if-block``, baris 14 adalah ``elif-block``, dan 
   baris 16 adalah ``else-block``.

Bagaimana program ini bekerja?

Program ini akan meminta inputan tebakan dari pengguna berupa bilangan. 
Untuk mendapatkan inputan ini kita gunakan fungsi ``raw_input``. Keluaran
dari fungsi ini adalah string yang diinputkan oleh user, oleh karena itu kita
harus melakukan konversi ke tipe data int. Untuk konversi ini kita gunakan
fungsi ``int``. Hasil dari inputan pengguna yang sudah dikonversi disimpan
dalam variabel tebakan.

Sebelumnya program telah menentukan bilangan acak yang disimpan dalam 
variabel ``nomor_acak``. Setelah mendapatkan input dari pengguna, program
masuk kedalam alur kontrol ``if``. Jika tebakan dan nomor acak sama maka
tampilkan pesan berhasil, jika tebakan kurang dari nomor acak maka tampilkan
pesan tebakan terlalu kecil, dan terakhir berarti tebakan terlalu besar.

.. note::
   Cek modul ``random`` pada bab library standar untuk menghasilkan nomor acak.

Statemen While
==============

Statemen while merupakan statemen untuk perulangan, ``block`` kode akan dijalankan
terus menerus selama kondisi benar. Statemen while dapat mempunyai bagian ``else``
(opsional).

::

   # lat10.py
   # acak looping

   nomor_acak = 77
   berjalan = True

   print 'tebak nomor acak dari 1 - 100'

   while berjalan:
       tebakan = int(raw_input('Tebakan anda (bil bulat): '))

       if tebakan == nomor_acak:
           print 'Selamat! tebakan anda benar'
           print 'tapi tidak ada hadiah untuk anda :('
           berjalan = False
       elif tebakan < nomor_acak:
           print 'tebakan anda terlalu kecil'
       else:
           print 'tebakan anda terlalu besar'
   else:
       print 'selesai'

Perulangan diatas berhenti jika ``berjalan`` (kondisi) bernilai ``False``. 
``True`` dan ``False`` merupakan obyek bertipe boolean, dan nilai ``True`` 
sama dengan nilai ``1``, nilai ``False`` sama dengan nilai ``0``.

::
   
   >>> True == 1
   True
   >>> False == 0
   True

Obyek dapat dinilai atau dikonversi ke nilai boolean

::
   
   >>> bool('nama')
   True
   >>> bool('')
   False
   >>> bool(0)
   False
   >>> bool(-5)
   True



Perulangan For (For Loop)
=========================

Statemen perulangan ``for ... in ... `` merupakan statemen perulangan
selain ``while``. Statemen ini melakukan *iterasi* dari rangkaian obyek,
berjalan melalui tiap item yang ada pada rangkaian / sequence. 
Apa itu rangkaian / sequence? rangkaian yaitu koleksi item yang terurut.


::
   
   # lat11.py

   for i in range(1, 6):
       print i
   else:
       print 'Perulangan sudah selesai'


Program ini akan mencetak rangkaian / sequence bilangan, dari 1 sampai 5.
Kita membuat rangkaian bilangan ini menggunakan fungsi *builtin* ``range``.
Apa yang kita lakukan yaitu memanggil fungsi ``range`` dengan dua parameter,
range akan mengembalikan rangkaian bilangan dari parameter pertama sampai
batas parameter kedua (eksklusif). Sebagai contoh ``range(1, 6)`` menghasilkan 
rangkaian ``[1, 2, 3, 4, 5]``.

Jika kita memanggil ``range`` dengan parameter ketiga, yaitu parameter
jumlah langkah. Contoh ``range(1, 6, 2)`` mengembalikan rangkaian 
``[1, 3, 5]``.

Bagian ``else`` adalah opsional dan akan selalu dijalankan kecuali jika ada
statemen ``break``.


Statemen Break
==============

Statemen ``break`` digunakan untuk keluar dari perulangan, misalnya keluar
dari perulangan walaupun kondisi perulangan masih ``True`` atau rangkaian
/ sequence belum diiterasi seluruhnya.

::
   
   # lat12.py

   while True:
       data = raw_input('Masukkan sesuatu : ')
       if data == 'keluar':
           break
       print 'Inputan pengguna "%s"' % data
   print 'Selesai'

Program ini akan terus meminta inputan pengguna dan akan berhenti ketika
pengguna menginputkan ``keluar``.

::
   
   # lat13.py

   for i in range(1, 11):
       print i
       if i == 5:
           break
   else:
       print "Tidak dijalankan karena break"

Bagian ``else`` tidak akan dijalankan karena perulangan tidak berhenti
secara normal.


Statemen Continue
=================

Statemen ``continue`` digunakan untuk melewati statemen yang ada dalam blok
perulangan dan *continue* / melanjutkan ke iterasi berikutnya.

::
   
   # lat14.py
   
   for i in range(1, 11):
       if i % 2 == 0:
           # skip bilangan genap
           continue
       print i
