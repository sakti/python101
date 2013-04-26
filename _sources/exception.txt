===================
Eksepsi (Exception)
===================

Eksepsi terjadi ketika ada sesuatu yang terduga muncul dalam program.
Misalnya program anda akan membaca suatu file, namun file tersebut tidak ada.
Hal seperti ini ditangani dengan ``exception``

Syntax Error
============

Syntax error, atau dikenal juga sebagai parsing error, adalah error ketika
Python memparsing program anda.

::
   
   >>> Print 'halo'
     File "<stdin>", line 1
     Print 'halo'
               ^
   SyntaxError: invalid syntax
   >>> while True print 'Hello world'
     File "<stdin>", line 1
     while True print 'Hello world'
                    ^
   SyntaxError: invalid syntax


Exception
=========

Kita akan mencoba / **try** membaca input dari pengguna. Tekan
``Ctrl-d`` apa yang akan terjadi.

::
   
   >>> teks = raw_input('Ketikkan sesuatu: ')
   Ketikkan sesuatu: Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   EOFError

Python mengeluarkan eksepsi ``EOFError`` yang berarti menemukan simbol
*end of file* (direpresentasikan oleh ``Ctrl-d``) ketika program berharap
tidak akan ada.

Penanganan Exception
====================

Kita dapat menangani eksepsi menggunakan statemen ``try ... except``. Sederhananya
kita letakkan statemen yang mungkin mengeluarkan eksepsi kedalam ``try-block``, dan
letakan kode penanganan eksepsi kedapam ``except-block``.

::

   # lat39.py
   
   try:
       teks = raw_input('Ketikkan sesuatu: ')
   except EOFError:
       print '\nKenapa sudah EOF?'
   except KeyboardInterrupt:
       print '\nAnda membatalkan operasi'
   else:
       print 'Anda mengetikkan "%s"' % teks


Mengeluarkan Exception
======================

Anda dapat mengeluarkan eksepsi menggunakan statemen ``raise`` dengan
menyediakan obyek eksepsi.

Anda dapat membuat eksepsi sendiri dengan membuat class turunan ``Exception``.

::

   # lat40.py

   class InputPendekError(Exception):
       "exception jika input terlalu pendek"

       def __init__(self, panjang, minimal):
           Exception.__init__(self)
           self.panjang = panjang
           self.minimal = minimal
   

   try:
       teks = raw_input('Ketikkan sesuatu: ')
       panjang = len(teks)
       minimal_panjang = 3

       if panjang < minimal_panjang:
           raise InputPendekError(panjang, minimal_panjang)
   except EOFError:
       print '\nKenapa sudah EOF?'
   except KeyboardInterrupt:
       print '\nAnda membatalkan operasi'
   except InputPendekError as e:
       print 'input terlalu pendek: panjang input: %s, minimal: %s' % (e.panjang, e.minimal)
   else:
       print 'Anda mengetikkan "%s"' % teks

Try ... Finally
===============

Ketika anda membaca file dari program anda. Bagaimana anda memastikan
file akan ditutup baik ada eksepsi maupun tidak. Anda bisa menggunakan
blok ``finally`` pada blok ``try``.

::

   # lat41.py

   import time
   
   try: 
       f = open('coba.txt')
       while True:
           baris = f.readline()
           if len(baris) == 0:
               # EOF
               break
           print baris,
           time.sleep(2) # delay 2 detik
   except KeyboardInterrupt:
       print '\nAnda membatalkan operasi'
   finally:
       f.close()
       print '\nfile ditutup.'


Statemen with
=============

Mendapatkan *resource* pada blok ``try`` dan melepasnya pada blok ``finally``
merupakan pola yang umum ditemukan. Oleh karena itu, anda dapat menggunakan
menggunakan statemen ``with`` yang menyediakan mekanisme diatas secara otomatis.

::

   # lat42.py
   
   with open('coba.txt') as f:
       for baris in f:
           print baris,
