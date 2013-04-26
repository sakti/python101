==================================
Library Standar (Standard Library)
==================================

Module getpass
==============

Mendapatkan password pengguna tanpa *echo* kembali ke pengguna.

::
   
   # contoh penggunaan modul getpass

   import getpass

   password = getpass.getpass()
   print 'Password anda : ', password

   password = getpass.getpass(prompt='Inputkan password anda :')
   print 'Password anda : ', Password


Modul random
============

Modul ``random`` menyediakan *fast pseudorandom number generator* 
berdasarkan algoritma *Mersenne Twister*.

::
   
   # contoh penggunaan modul random

   import random
   
   print 'bilangan random antara 0<= n < 1.0 : ', random.random()
   print 'bilangan random antara 0<= n < 1.0 : ', random.random()
   print 'bilangan random antara 0<= n < 1.0 : ', random.random()

   # random integer
   print 'bilangan random antara 1<= n <= 100 : ', random.randint(1, 100)
   print 'bilangan random antara 1<= n <= 100 : ', random.randint(1, 100)
   print 'bilangan random antara 1<= n <= 100 : ', random.randint(1, 100)



Modul datetime
==============

Modul ``datetime`` berisi fungsi dan class untuk operasi tanggal dan waktu.

::
   
   # contoh penggunaan module datetime

   import datetime
   import time

   sekarang = datetime.datetime.now()

   tanggal = sekarang.date()
   waktu = sekarang.time()

   print 'Hari : ', tanggal.day
   print 'Bulan : ', tanggal.month
   print 'Tahun : ', tanggal.year
   print 'Jam : ', waktu.hour
   print 'Menit : ', waktu.minute
   print 'Detik : ', waktu.second

   time.sleep(5)

   sekarang2 = datetime.datetime.now()

   delta = sekarang2 - sekarang

   print 'selisih detik : ', delta.total_seconds()


Modul math
==========

Modul ``math`` berisi fungsi-fungsi matematika.

::
   
   # contoh penggunaan modul math

   import math

   # konstanta
   print 'pi = ', math.pi
   print 'e = ', math.e

   # faktorial, n!
   for i in range(1, 11):
       print '%s! = %s' % (i, math.factorial(i))

   # pangkat
   print '2 pangkat 12 = ', math.pow(2, 12)

   # akar kuadrat
   print 'akar kuadrat 10 = ', math.sqrt(10)

   # logaritma
   print 'log 8 = ', math.log(8)
   print 'log 8 basis 10 = ', math.log(8, 10)
   print 'log 8 basis 10 = ', math.log10(8)

   # trigonometri
   print 'sin 90 derajat = ', math.sin(math.radians(90))

Modul sys
=========

Modul ``sys`` digunakan untuk mengakses konfigurasi interpreter pada saat 
runtime dan berinteraksi dengan ``environment`` sistem operasi.
::
   
   # contoh penggunaan modul sys / System-specific Configuration

   import sys

   # argumen terminal
   print sys.argv
   # versi python
   print 'versi python: ', sys.version
   # platform
   print 'platform : ', sys.platform
   # letak python interpreter
   print 'executable : ', sys.executable
   # byteorder
   print 'byteorder : ', sys.byteorder

   # module yang diimport
   print 'modul yang diimport : ', sys.modules
   # module built-in
   print 'modul built-in : ', sys.builtin_module_names

   # path import
   print 'path import : ', sys.path



PYMOTW (Python Module of The Week)
==================================

Masih ada banyak modul yang ada di Python. Untuk menjelajahi
modul-modul yang tersedia di Python anda dapat membaca
`Python Module of The Week`_ yang membahas modul python satu per satu.



.. _Python Module of The Week: http://pymotw.com/2/