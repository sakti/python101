=============
Struktur Data
=============

Struktur Data adalah struktur yang dapat menyimpan dan mengorganisasikan kumpulan data.
Berikut struktur data yang ada dalam Python.

List
====

List adalah struktur data yang menyimpan koleksi data terurut, anda dapat
menyimpan sequence / rangkaian item menggunakan list.

Item dalam list ditutup menggunakan kurung siku ``[]`` (list literal).
Setelah list dibuat anda bisa menambah, mengurangi, dan mencari item pada
list. Karena kita dapat menambah dan mengurangi item, list bersifat ``mutable``.

Pengenalan singkat obyek dan class
----------------------------------

List adalah contoh penggunaan obyek dan class. Ketika kita menggunakan variabel
``i`` dan mengisinya dengan nilai integer ``5``, sama dengan kita membuat obyek 
(instance) ``i`` dari class (tipe) ``int``. Anda dapat membaca ``help(int)`` untuk
membaca dokumentasi class integer.

Class mempunyai method, fungsi yang didefinisikan dalam class. Anda bisa
menggunakan method ini pada obyek class tersebut. Sebagai contoh, Python
menyediakan method ``append`` untuk class list. ``contoh_list.append('item 1')``
akan menambahkan string ``'item 1'`` kedalam list ``contoh_list``. Perhatikan
notasi titik untuk mengakses method pada obyek.

Class juga mempunyai field yang sama halnya variabel yang digunakan hanya
untuk class. Anda bisa menggunakan variabel / nama ini pada obyek class tersebut.

::

   # lat25.py

   daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']

   print 'saya punya %s barang yang akan dibeli' % len(daftar_belanja)

   print 'barang tersebut:'
   for barang in daftar_belanja:
       print barang,

   print 'saya harus membeli beras'
   daftar_belanja.append('beras')
   print 'daftar belanja sekarang :', daftar_belanja

   print 'saya akan mengurutkan daftar belanja saya'
   daftar_belanja.sort()
   print 'daftar belanja setelah diurutkan', daftar_belanja

   print 'barang yang harus saya beli pertama', daftar_belanja[0]
   barang_pertama = daftar_belanja[0]

   del daftar_belanja[0]

   print 'saya membeli', barang_pertama
   print 'daftar belanja sekarang:', daftar_belanja

Tuple
=====

Tuple mirip dengan list namun tuple bersifat immutable (tidak bisa diubah
setelah didefinisikan).

Tuple dibuat dengan menspesifikasikan item tuple dipisahkan menggunakan
tanda koma dan opsional diapit dengan tanda kurung.

::

   # lat26.py

   kebun_binatang = ('ular python', 'gajah', 'pinguin')
   print 'jumlah binatang yang ada di kebun binatang :', len(kebun_binatang)

   kebun_binatang_baru = 'monyet', 'unta', kebun_binatang
   print 'jumlah kandang di kebun binatang baru:', len(kebun_binatang_baru)
   print 'binatang yang ada di kebun bintatang baru:', kebun_binatang_baru
   print 'binatang dari kebun binatang lama:', kebun_binatang_baru[2]
   print 'binatang terakhir dari kebun binatang lama:', kebun_binatang_baru[2][2]

   jumlah_binatang = len(kebun_binatang_baru) - 1 + len(kebun_binatang_baru[2])

   print 'jumlah binatang yang ada di kebun binatang baru :', jumlah_binatang

Dictionary
==========

Dictionary seperti buku alamat, dengan buku alamat anda bisa mencari 
alamat atau detail kontak hanya menggunakan nama orang yang anda cari.
Kita mengasosiasikan ``key`` (nama) dengan ``value`` (detail). Catatan 
``key`` harus bersifat unik, anda tidak bisa menemukan informasi yang 
tepat jika ada dua orang yang mempunyai nama yang sama dalam 
buku alamat anda.

Anda hanya bisa menggunakan obyek immutable (seperti string) untuk
``key``/ kunci dictionary. Anda bisa menggunakan obyek mutable atau immutable
untuk ``value`` dalam dictionary.

Dictionary dispesifikasikan menggunakan pasangan ``key`` dan ``value`` diapit
menggunakan kurung kurawal, ``{key1: value1, key2: value2}``.

::

   # lat27.py

   # ba, singkatan buku alamat
   ba = {'guido': 'guido@python.org',
       'brandon': 'brandon@rhodesmill.org',
       'spammer': 'spammer@domain.com'}

   print 'alamat email guido:', ba['guido']

   # menghapus item
   del ba['spammer']

   print 'ada %s kontak di buku alamat' % len(ba)

   for nama, email in ba.items():
       print '%s, email: %s' % (nama, email)
   
   # tambah entri
   ba['jacob'] = 'jacob@jacobian.org'

   if 'jacob' in ba:
       print 'Email jacob di', ba['jacob']

Sequence
========

List, tuple dan string adalah contoh dari sequence. Kita dapat melakukan
tes keanggotaan, operasi index(akses, slicing), dan iterasi pada sequence.

::

   # lat28.py

   daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
   nama = 'budi'

   print 'Barang 0 =', daftar_belanja[0]
   print 'Barang 1 =', daftar_belanja[1]
   print 'Barang 2 =', daftar_belanja[2]
   print 'Barang 3 =', daftar_belanja[3]

   print 'Barang -1 =', daftar_belanja[-1]
   print 'Barang -2 =', daftar_belanja[-2]

   print 'Karakter 0 =', nama[0]

   # slicing pada list
   print 'Barang 1 ke 3:', daftar_belanja[1:3]
   print 'Barang 2 ke terakhir:', daftar_belanja[2:]
   print 'Barang 1 ke -1:', daftar_belanja[1:-1]
   print 'Barang dari awal ke akhir:', daftar_belanja[:]

   # slicing pada string
   print 'Karakter 1 ke 3:', nama[1:3]
   print 'Karakter 2 ke terakhir:', nama[2:]
   print 'Karakter 1 ke -1:', nama[1:-1]
   print 'Karakter dari awal ke akhir:', nama[:]   



Set
===

Set adalah koleksi obyek yang tidak terurut. Digunakan ketika
keberadaan obyek pada koleksi lebih penting daripada urutan dan berapa kali
obyek muncul pada koleksi.

::

   # lat29.py
   negara = set(['brazil', 'rusia', 'indonesia'])

   print 'indonesia' in negara
   print 'amerika' in negara

   negara2 = negara.copy()
   negara2.add('korea')

   print negara2.issuperset(negara)

   negara.remove('rusia')

   print negara2 & negara
   print negara2.intersection(negara)


Referensi
=========

Jika anda membuat obyek dan mengisinya ke variabel, variabel hanya
me *refer* ke obyek dan tidak merepresentasikan obyek itu sendiri.
Nama variabel menunjuk ke bagian memori komputer dimana obyek disimpan.
Hal ini dinamakan **binding** antara nama ke obyek.

::

   # lat29.py

   daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']
   print 'assignment biasa'
   daftar_saya = daftar_belanja

   del daftar_belanja[0]

   print 'daftar belanja:', daftar_belanja
   print 'daftar saya:', daftar_saya

   print 'copy obyek daftar belanja menggunakan slice [:]'
   daftar_saya = daftar_belanja[:] # membuat copy

   del daftar_saya[0]

   print 'daftar belanja:', daftar_belanja
   print 'daftar saya:', daftar_saya



String
======

Tipe atau class String mempunyai method-method untuk memudahkan operasi string.

::

   # lat30.py

   nama = 'Indonesia'

   if nama.lower().startswith('ind'):
       print 'Nama diawal dengan "ind"'
   if 'ne' in nama:
       print 'Nama berisi string "ne"'
   if nama.find('done') != -1:
       print 'Nama berisi string "done"'

   pembatas = ', '
   daftar_belanja = ['apel', 'mangga', 'wortel', 'pisang']

   print pembatas.join(daftar_belanja)