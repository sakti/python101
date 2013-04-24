===========
Pendahuluan
===========

Selamat datang di Workshop Python 101. Setelah workshop ini diharapkan anda bisa menggunakan 
bahasa pemrograman Python untuk memecahkan masalah di kehidupan sehari-hari (yang bisa dipecahkan
dengan pemgrograman tentunya).


Persiapan
---------

Untuk dapat mengikut workshop ini pastikan Python interpreter sudah terinstall di komputer anda.
Versi python yang digunakan untuk tutorial ini adalah versi 2.7.*.


Terdapat dua versi python yang saat ini ada versi 2 vs versi 3. Ada beberapa perbedaan syntax dan operasi ``IO``. Untuk `library` tambahan Python versi 3 masih kurang daripada versi 3. Jika anda sudah menguasai python 2 akan lebih mudah untuk bermigrasi ke versi 3.

.. note::
   
   `Python 2.x is the status quo, Python 3.x is the present and future of the language`



Pengguna Windows
````````````````
Untuk pengguna MS Windows. Python interpreter dapat di download di `Python.org Download`_. Kemudian pilih *individual releases*. Ada beberapa alternatif python installer untuk Windows 
(ActiveState, Enthougt). Untuk workshop ini gunakan default installer dari python.org.


.. figure:: /_static/img/python_on_windows.png
   :alt: python on windows
   :scale: 100%
   :class: centered

   Python di Windows


.. note::
   
   Jika menemukan kesalahan
   ``'python' is not recognized as an internal or external command, operable program or batch file.``

   cek ``windows PATH environment variable``

   .. figure:: /_static/img/python_path_windows.png
      :alt: python on windows
      :scale: 100%
      :class: centered


Pengguna Linux
``````````````
Pada umumnya distro linux sudah menyertakan Python secara default. Pastikan default python interpreter
menunjuk ke python versi 2.*:

::

    $ python --version
    Python 2.7.3


.. figure:: /_static/img/python_on_linux.png
   :alt: python on linux
   :scale: 100%
   :class: centered

   Python di Linux

Pengguna Mac OS X
`````````````````

Mac OS X secara default menyertakan Python interpreter.

.. figure:: /_static/img/python_on_mac.png
   :alt: python on mac
   :scale: 100%
   :class: centered

   Python di Mac OS X



Editor Teks
-----------

Anda bebas menggunakan editor teks kesayangan anda.

Vim
```

.. figure:: /_static/img/vim-python.png
   :alt: Edit python menggunakan vim
   :scale: 100%
   :class: centered

   Edit program python menggunakan Vim


Emacs
`````

.. figure:: /_static/img/emacs-python.png
   :alt: Edit python menggunakan emacs
   :scale: 100%
   :class: centered

   Edit program python menggunakan Emacs



SublimeText 2
`````````````

.. figure:: /_static/img/sublimetext2_python.png
   :alt: Edit python menggunakan Sublime Text
   :scale: 100%
   :class: centered

   Edit program python menggunakan Sublime Text2x

.. _Python.org Download: http://www.python.org/download/windows/