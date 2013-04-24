=====
Dasar
=====

Dasar-dasar bahasa pemrograman Python.


Menggunakan Python sebagai kalkulator
=====================================

Program Python dapat dijalankan dengan beberapa mode. Jika kita mengeksekusi
Python interpreter tanpa argument script Python yang telah kita buat, Python interpreter
akan masuk ke mode interaktif (REPL_, read-eval-print loop).



.. code-block:: bash

   $ python
   Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
   [GCC 4.6.3] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 
   >>> 




Kita dapat memanfaatkan Python dengan mode interaktif sebagai kalkulator.


.. code-block:: bash
    
   $ python
   Python 2.7.3 (default, Aug  1 2012, 05:14:39) 
   [GCC 4.6.3] on linux2
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 1 + 1
   2
   >>> 40 * 2
   80
   >>> 40 / 5
   8
   >>> 9 - 10
   -1
   >>> 2 + 3 + 4 + 5
   14
   >>> 2 ** 32
   4294967296

Operasi aritmatika
------------------

Berikut table operasi aritmatika yang ada di Python:

======= =======================================
Operasi Keterangan
======= =======================================
\+      Menambahkan dua obyek
\-      Mengurangi obyek dengan obyek yang lain
\*      Perkalian
\*\*      Pangkat
/       Pembagian
//      Pembagian bulat ke bawah
%       Sisa hasil bagi (modulus)
======= =======================================


**Contoh**

Pembagian, perhatikan perbedaan antara bilangan bulat dan pecahan / desimal.

::
   
   >>> 10 / 3
   3
   >>> 10.0 / 3
   3.3333333333333335
   >>> 10 / 3.0
   3.3333333333333335
   >>> 10.0 / 3.0
   3.3333333333333335
   >>> 10.0 // 3.0
   3.0
   >>> 10.0 // 3
   3.0

Sisa hasil bagi.

::
   
   >>> 10 % 3
   1
   >>> 2 % 3
   2 
   >>> -5 % 4
   3
   >>> -5 % -4
   -1

.. note::

   mode eksekusi lain:

   **\-m**
   Mengeksekusi module, contoh: ``python -m SimpleHTTPServer`` untuk membuat
   webserver statis

   **\-c**
   Mengeksekusi command dari pameter yang diterima, contoh: 
   ``python -c 'import this'`` untuk menampilkan `Zen of Python`_.

Halo Dunia!
===========

Program pertama yaitu program yang jika dijalankan akan mengeluarkan hasil
teks berupa ``Halo Dunia!``.

::
   
   # lat1.py
   print 'Halo Dunia!'


Anda bisa membuat file ``lat1.py`` menggunakan teks editor pilihan anda.


.. note:: 
   Untuk catatan, anda sebaiknya menset teks editor anda agar untuk indentasi
   menggunakan spasi / space sebanyak 4. Standar PEP (Python Enhancement Proposal)
   menyarankan agar indentasi selalu konsisten. 

Setelah file ``lat1.py`` disimpan, anda dapat menjalankannya melalui terminal.


.. code-block:: bash
   
   $ python lat1.py
   Halo Dunia!

Jika anda menggunakan SublimeText2 anda dapat menjalankannya menggunakan menu. 
``Tools -> Build``, untuk linux anda dapat menggunakan shortcut ``Ctrl+b``.

.. figure:: /_static/img/lat1.py.png
   :alt: Running program python menggunakan SublimeText2
   :scale: 100%
   :class: centered

   Running program python menggunakan SublimeText2
    


Komentar
========

Komentar adalah teks apapun yang diawali dengan tanda ``#``, digunakan untuk 
memberikan catatan kepada pembaca kode. 
Anda dapat melihat kembali ``lat1.py`` untuk memberikan keterangan nama file
kita dapat memberikan komentar.


Berikut file latihan 2, perhatikan statemen print terakhir tidak akan dieksekusi
karena berupa komentar.
::
   
   # lat2.py
   # lat2.py adalah nama file ini
   # program ini akan menampilkan 'Halo Indonesia!'
   # kemudian akan menampilkan 'Halo Jakarta!'

   print 'Halo Indonesia!'
   print 'Halo Jakarta!'

   # print 'Teks ini tidak akan dicetak.'



Konstanta Literal
=================

Salah satu contoh konstanta literal yaitu bilangan seperti ``5``, ``1.23``, atau
string seperti ``'hari senin'`` atau ``"hari jum'at"``. Hal ini disebut literal atau
harfiah karena anda bisa menggunakan nilai ini secara langsung. Bilangan ``2`` selalu
merepresentasikan dirinya sendiri, dinamakan konstanta karena nilainya tidak dapat
diubah.

Dalam latihan 2, ``'Halo Indonesia!'`` dan ``'Halo Jakarta!'`` merupakan string literal.

Bilangan
========

Di Python bilangan dibagi menjadi dua tipe utama - integer (bulat) dan float (pecahan).
Salah satu contoh dari integer yaitu ``2`` yang merupakan bilangan bulat.
Contoh untuk float yaitu ``3.23`` dan ``52.3e-4``. Notasi ``e`` mengindikasikan pangkat
10. Untuk kasus ini ``52.3e-4`` berarti 52.3 * 10 \ :sup:`-4`.

String
======

String adalah rangkaian karakter. Anda bisa menuliskan string literal dengan beberapa cara:

- *Single Quote*

  Contoh: ``'Halo Bandung!'``, ``'Hari Jum\'at'``.
- *Double Quote*

  Contoh: ``"Halo Surabaya!"``, ``"Hari Jum'at"``. Perhatikan tanda quote ``'`` harus
  di *escape* pada single quote. Selain itu tidak ada perbedaan antara single
  quote dan double quote, anda bebas untuk memilih.
- *Triple Quote*

  Python mendukung multi-line string atau string dengan baris lebih dari satu. Anda
  dapat dengan bebas menuliskan single quote ``'`` dan double quote ``"`` dalam 
  string literal yang diapit dengan triple quote. Contoh:
  ::

     """Ini adalah contoh multi-line string
     saya tambahkan single quote ' dan double
     quote ", tanpa perlu meng-escape \\ terlebih dahulu"""

  Contoh lain:
  ::

     '''Ini adalah contoh multi-line string
     saya tambahkan single quote ' dan double
     quote ", tanpa perlu meng-escape \\ terlebih dahulu'''

  Perhatikan perbedaan antara dua contoh diatas.

Immutable
---------

String bersifat immutable yang berarti setelah string dibuat, string tersebut tidak
bisa diubah. 

Format String
-------------

Terkadang kita ingin membuat string dari informasi lain, untuk hal ini kita dapat
menggunakan format string.

::
   
   # lat3.py
   # format string menggunakan operator '%' dan method format

   print '%s pergi ke %s' % ('ibu', 'pasar')
   print '{0} pergi ke {1}'.format('ibu', 'pasar')
   
   print 'jumlah total: %10.3f' % 10.3333
   print 'jumlah total: {0:10.3f}'.format(10.3333)

.. note::
   Operator ``%`` jika digunakan untuk string bukan berarti modulus melainkan
   string format.

Variabel
========

Hanya menggunakan konstanta literal saja cukup membosankan, kita membutuhkan cara
untuk menyimpan dan memanipulasi informasi. Untuk hal ini kita bisa menggunakan
variabel, seperti namanya variabel dapat diisi dengan bermacam-macam nilai, anda dapat
menyimpan apapun menggunakan variabel. Variabel adalah sebagian dari memori komputer
anda yang digunakan untuk menyimpan informasi. Berbeda dengan konstanta literal, 
anda membutuhkan cara untuk mengakses variabel ini, oleh karena itu kita memberi
nama kepada variabel.

Nama Pengenal
-------------
Berikut aturan penamaan variabel dalam python.

- Karakter pertama harus berupa karakter alfabet (huruf besar atau huruf kecil ASCII,
  atau unicode) atau underscore ``_``.
- Karakter selanjutnya dapat berupa alfabet (huruf besar atau huruf kecil ASCII, atau
  unicode), underscore ``_`` atau digit (0-9).
- Nama variabel bersifat case-sensitif. Sebagai contoh, namaMhs dan namamhs adalah
  variabel yang berbeda.


::
   
   # lat4.py
   # menggunakan variabel

   a = 10
   b = 20
   c = 30

   total = a + b + c

   nama = 'ibu'
   tempat = 'kantor'
   
   print 'jumlah total = %s' % total
   print '%s pergi ke %s' % (nama, tempat)

Tipe Data
=========

Variabel dapat menyimpan nilai dengan berbagi tipe disebut dengan tipe data. Bilangan
dan string adalah tipe dasar, yang sudah dibahas sebelumnya. Pada latihan berikutnya
akan dibahas tipe data yang lain.

Anda menggunakan ``type`` untuk menentukan tipe data variabel / obyek yang ada.

::

   >>> type(1)
   <type 'int'>
   >>> type(3.2)
   <type 'float'>
   >>> type(2 ** 1000)
   <type 'long'>
   >>> type('abc')
   <type 'str'>
   >>> type('a')
   <type 'str'>


Obyek
=====

Semua yang ada dalam Python adalah obyek / object. Obyek memiliki field yang memiliki
nilai tertentu dan method untuk operasi tertentu.

Untuk melihat field dan method yang ada dalam suatu obyek kita dapat gunakan fungsi
builtin ``dir``.

::
   
   >>> dir('abc')
   ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
   >>> 'abc'.upper
   <built-in method upper of str object at 0x7fe601a1f800>
   >>> 'abc'.upper()
   'ABC'

Selain dapat melihat isi obyek anda dapat mengakses dokumentasi object menggunakan
``help``.

::
   
   >>> help(str)
   Help on class str in module __builtin__:

   class str(basestring)
    |  str(object) -> string
    |  
    |  Return a nice string representation of the object.
    |  If the argument is a string, the return value is the same object.
    |  
    |  Method resolution order:
    |      str
    |      basestring
    |      object
   ...

   >>> help(str.upper)
   Help on method_descriptor:

   upper(...)
       S.upper() -> string
       
       Return a copy of the string S converted to uppercase.


Penulisan Program Python
========================

Berikut cara menulis program Python.

- Buka teks editor pilihan anda, seperti: vim, emacs, gedit, notepad++, sublimetext2.
- Ketikkan kode program seperti contoh yang ada (hindari copy-paste).
- Simpan sesuai nama yang ada.
- Untuk menjalankan program gunakan terminal / command line, 
  ketik ``python namaprogram.py``.

.. note::
   Untuk pengguna sublimetext2 anda dapat menjalakan program python 
   menggunakan shortcut ``Ctrl+b``.


Baris Logis dan Fisik
---------------------

Baris fisik adalah apa yang anda lihat ketika anda melihat program. Baris logis 
adalah apa yang Python lihat sebagai statemen tunggal. Python mengasumsikan
bahwa setiap baris fisik sesuai dengan baris logic.

Sebagai contoh baris logis seperti statemen ``print 'Halo Dunia!'``, jika anda
menulis sebagai satu baris maka baris logis sesuai dengan baris fisik.

.. note::
   Anda dapat menulis ``print 'Halo Dunia!'`` menjadi dua baris, contoh:
   ::

      print \
      'Halo Dunia!'

   Anda juga dapat membuat beberapa baris logis menjadi satu baris fisik, contoh:
   ::

      nama = 'budi'; print nama

Secara implisit, Python menyarankan menggunakan satu statemen tiap baris untuk 
menjadikan kode menjadi lebih mudah dibaca.

Indentasi
---------

Karakter spasi penting untuk bahasa pemrogramman Python. Lebih tepatnya **spasi
diawal baris** atau indentasi. Spasi diawal (spasi atau tab) baris logis digunakan
untuk menentukan level indentasi, yang akan mempengaruhi pengelompokan statemen.

Statemen yang mempunyai level indentasi sama masuk dalam satu kelompok yang disebut
**block**. Hal ini akan digunakan pada bab berikutnya.

::
   
   # lat5.py
   # error indentasi

   a = 10
   b = 20
   c = 30

    total = a + b + c

   nama = 'ibu'
   tempat = 'kantor'
   
   print 'jumlah total = %s' % total
   print '%s pergi ke %s' % (nama, tempat)

.. _REPL: http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop
.. _Zen of Python: http://www.python.org/dev/peps/pep-0020/