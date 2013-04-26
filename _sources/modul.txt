=====
Modul
=====

Anda dapat menggunakan kode ulang dalam program menggunakan fungsi. 
Bagaimana cara menggunakan fungsi yang ada di file .py yang berbeda?
jawabnya adalah modul. 

File latihan yang sudah anda buat dari ``lat1.py`` sampai
``lat21.py`` merupakan modul. Untuk menggunakan fungsi atau variabel
yang ada di file tersebut kita dapat melakukan ``import``.

::
   
   >>> import lat21
   >>> print lat21.katakan('A', 10)
   AAAAAAAAAA

Selain modul ``.py`` kita dapat membuat modul dengan bahasa pemrograman C.

Byte-compiled (file .pyc)
=========================

Setelah mencoba modul ``lat21`` (tanpa ``.py``). Anda akan menemukan 
file ``lat21.pyc`` pada direktori yang sama.

Jika anda melakukan ``import`` suatu modul, modul tersebut akan di
*interpret* terlebih dahulu. Untuk optimisasi python akan membuat file
byte-compiled modul tersebut dalam file ``.pyc`` sehingga import
modul tidak harus melakukan *compile*.


Statemen from ... import
========================

Anda dapat mengakses fungsi, variabel atau class dalam modul
menggunakan berbagai cara.

::
   
   # lat22.py

   import lat21
   from lat21 import katakan
   from lat21 import katakan as hi

   print lat21.katakan('a', 10)
   print katakan('a', 20)
   print hi('a', 30)

Nama Modul
==========

Setiap module memiliki nama, anda bisa mengakses nama ini
menggunakan variabel ``__nama__``. Kita dapat tahu apakah
modul ini dijalankan *standalone* atau di *import* oleh
modul lain.

Jika modul kita dijalankan *standalone* maka isi variabel
``__nama__`` berisi ``__main__``

::
   
   # lat23.py

   if __name__ == '__main__':
       # akan dijalankan jika dieksekusi secara langsung
       # bukan import
       print 'nama mudul ini : ', __name__

       import lat21
       print 'nama modul yang di import : ', lat21.__name__

Fungsi dir
==========

Untuk melihat isi dalam suatu modul kita dapat menggunakan
fungsi builtin ``dir``.

::
   
   >>> import sys
   >>> dir(sys)
   ['__displayhook__', '__doc__', '__egginsert', '__excepthook__', '__name__', '__package__', '__plen', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_mercurial', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'last_traceback', 'last_type', 'last_value', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'py3kwarning', 'pydebug', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions']

Package
=======

Sekarang anda dapat mengamati struktur program Python. Variabel
ada di dalam fungsi. Fungsi dan variabel global ada dalam modul.
Bagaimana caranya mengorganisasikan modul? jawabannya adalah 
*Package*.

*Package* adalah direktori yang berisi modul python dan file
spesial ``__init__.py``. File ``__init__.py`` menandakan bahwa
direktori ini merupakan *package* Python.

Untuk latihan kali ini, kita buat direktori lat24. Direktor ini
berisi


__init__.py

::
   
   # __init__.py
   print "di jalankan ketika package di import"

kata.py

::

   # kata.py
   def balik_huruf(kata):
       return kata[::-1]

nomor.py
::

   # nomor.py
   def lebih_besar(a, b):
       if a > b:
           return a
       else:
           return b


Pada direktori latihan kita buat file ``lat24tes.py``.

::

   # lat24tes.py
   from lat24 import kata
   from lat24 import nomor

   print kata.balik_huruf('selamat datang')
   print nomor.lebih_besar(10, 18)