============================================================
Object-Oriented Programming (Pemrograman berorientasi Obyek)
============================================================

Pada program yang selama ini kita buat, kita mendesain program
kita berdasarkan fungsi (blok statemen yang memanipulasi data).
Hal ini disebut pemrograman *procedure-oriented*.

Ada cara lain untuk mengorganisasi program dengan menggabungkan
data dan operasi yang dibungkus dalam suatu obyek yaitu paradigma
pemrograman berorientasi obyek.

Obyek memiliki field berupa variabel obyek dan method berupa 
fungsi obyek. Keduanya disebut atribut obyek. Class juga dapat 
memiliki field class (variabel class) dan method class. Class didefinisikan dengan
keyword ``class``.


this -> self
============

Dalam deklarasi method pada class terdapat perbedaan yaitu ada parameter
pertama yang harus ditambahkan pada parameter fungsi. Parameter ini diberi nama
``self``, nilai dari parameter ini menunjuk ke obyek / instance itu sendiri.

.. note::
   programmer Java, C# dan C++ terbiasa dengan keyword ``this``. Bedanya
   untuk Python variabel ini dikirim ke method secara eksplisit.

Nilai self ini disediakan oleh Python. Contoh, ada class ``ClassSaya``
yang mempunyai instance obyek ``obyeksaya``. Ketika method dipanggil 
pada obyek ``obyeksaya.method(arg1, arg2)``, secara otomatis diubah oleh
Python menjadi ``ClassSaya.method(obyeksaya, arg1, arg2)``.


Class
=====

Berikut contoh class yang sederhana.
::

   # lat31.py

   class Orang:
       pass

   org = Orang()
   print(org)

jika dijalankan akan mengeluarkan

.. code-block:: bash
   
   <__main__.Orang instance at 0x7f67decc9bd8>

Menunjukkan variabel ``org`` adalah instance class ``Orang`` pada alamat memory ``0x7f67decc9bd8``.


Method Obyek
============

Berikut contoh deklarasi method pada class.

::

   # lat32.py

   class Orang:
       def katakanHalo(self):
           print 'Halo, apa kabar?'

   org = Orang()
   org.katakanHalo()


.. note::
   Perhatikan walaupun method ``katakanHalo`` tidak membaca parameter, masih ada ``self`` pada
   deklarasi method.

Method init
===========

Ada nama-nama method spesial pada class Python. ``__init__`` adalah salah satunya, method
ini akan dijalankan ketika obyek dibuat. Method ini berguna untuk melakukan inisialisasi.
Perhatikan garis bawah dua kali di awal dan di akhir method (*double underscore, dunder*).

::

   # lat33.py

   class Orang:
       def __init__(self, nama):
           self.nama = nama

       def katakanHalo(self):
           print 'Halo, nama saya %s, apa kabar?' % self.nama
 
   org = Orang('budi')
   org.katakanHalo()



Variabel Class dan Variabel Obyek (Instance)
============================================

Variabel Class yaitu variabel yang dimiliki oleh class, sedangkan
variabel obyek adalah variabel yang yang dimiliki oleh tiap-tiap obyek
instance dari class.

::

   # lat34.py

   class Orang:
       # variabel class, untuk menghitung jumlah orang
       total = 0
       def __init__(self, nama):
           # inisiasi data, data yang dibuat pada self merupakan variabel obyek
           self.nama = nama

           # ketika ada orang yang dibuat, tambahkan total orang
           Orang.total += 1

       def __del__(self):
           # kurangi total orang jika obyek dihapus
           Orang.total -= 1

       def katakanHalo(self):
           print 'Halo, nama saya %s, apa kabar?' % self.nama

       def total_populasi(cls):
           print 'Total Orang %s' % cls.total

       # method class
       total_populasi = classmethod(total_populasi)
 
   org = Orang('budi')
   org.katakanHalo()
   Orang.total_populasi()

   org2 = Orang('andi')
   org2.katakanHalo()
   Orang.total_populasi()

   print 'obyek dihapus'
   del org
   del org2
	
   Orang.total_populasi()   

Inheritance
===========

Salah satu keuntungan dari OOP adalan penggunaan ulang kode dan
salah satu caranya yaitu menggunakan mekanisme *inheritance* / turunan.

::

   # lat35.py
   
   # base class / superclass
   class AnggotaSekolah:
       "representasi anggota sekolah"
       def __init__(self, nama, umur):
           self.nama = nama
           self.umur = umur

           print 'membuat anggota sekolah baru: %s' % self.nama

       def info(self):
           "cetak info"
           print 'Nama: %s, Umur: %s' % (self.nama, self.umur)

   # subclass
   class Guru(AnggotaSekolah):
       "representasi guru"
       def __init__(self, nama, umur, gaji):
           AnggotaSekolah.__init__(self, nama, umur)
           self.gaji = gaji

           print 'membuat guru: %s' % self.nama

       def info(self):
           AnggotaSekolah.info(self)
           print 'Gaji: %s' % self.gaji

   # subclass
   class Siswa(AnggotaSekolah):
       "representasi siswa"
       def __init__(self, nama, umur, nilai):
           AnggotaSekolah.__init__(self, nama, umur)
           self.nilai = nilai

           print 'membuat siswa: %s' % self.nama

       def info(self):
           AnggotaSekolah.info(self)
           print 'Nilai: %s' % self.nilai


   guru = Guru('Budi', 40, 3000000)
   siswa = Siswa('Andi', 25, 75)

   # cetak baris kosong
   print

   anggota = [guru, siswa]

   for orang in anggota:
       orang.info()