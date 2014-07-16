===================
Cryptography Course
===================

:Author: Marco Massenzio (m.massenzio@gmail.com)
:Date: 2014-07-07
:Version: 0.1

A number or crypto utilities and problems solutions for the `Coursera Cryptography course`_

Week 1
======

Programming problem solved!
See ``week1.py``

Week 2
======

Installation of PyCrypto
------------------------

A viable alternative appears to be just using ``pip``[#]_::

    $ pip install pycrypto

failing that, follow below.

Download the ``tar.gz`` file from the `PyCrypto download page`_ and untar somewhere
on your hard drive::

    $ tar xvfz pycrypto-2.6.1.tar.gz

Before installing, make sure you have the necessary Python headers::

    $ sudo apt-get install python-dev

then build, activate the virtualenv and install::

    $ python setup.py build
    $ workon crypto
    $ python setup.py install

Afterwards you can run the tests (I got an error, but afterwards, using the library
it all seemed to work well)::

    $ python setup.py test
    running test
    ...........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................SelfTest: You can ignore the RandomPool_DeprecationWarning that follows.
    ..........E...................
    ======================================================================
    ERROR: test_negative_number_roundtrip_mpzToLongObj_longObjToMPZ (Crypto.SelfTest.Util.test_number.MiscTests)
    Test that mpzToLongObj and longObjToMPZ (internal functions) roundtrip negative numbers correctly.
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "build/lib.linux-x86_64-2.7/Crypto/SelfTest/Util/test_number.py", line 283, in test_negative_number_roundtrip_mpzToLongObj_longObjToMPZ
        k = number._fastmath.rsa_construct(n, e)
    AttributeError: 'NoneType' object has no attribute 'rsa_construct'

    ----------------------------------------------------------------------
    Ran 1033 tests in 103.965s

You can now use PyCrypto in your project::

    >>> from Crypto.Cipher import AES
    >>> from Crypto import Random
    >>> key = '140b41b22a29beb4061bda66b6747e14'.decode('hex')
    >>> iv = Random.new().read(AES.block_size)
    >>> enc = AES.new(key, AES.MODE_CBC, iv)
    >>> cipher = enc.encrypt('This is a secret message... shh!')
    >>> xmit_msg = '{iv}{cipher}'.format(iv=iv, cipher=cipher)
    >>> xmit_msg
    '\xabW%\xc7\x96lKP\x01\x92\x06\xe7$<\xa4X\xa4/L\x95\x977\x1c\x7f\x05W2\xc8\x1dj\xaa\x1c\x97\t)\t\xde\x95\\$h\xcb\xc5r;\xe9\x84\xea'

    >>> new_enc = AES.new(key, AES.MODE_CBC, xmit_msg[:AES.block_size])
    >>> new_enc.decrypt(xmit_msg[AES.block_size:])
    'This is a secret message... shh!'

The `PyCrypto apidocs`_ and this `StackOverflow CTR question`_ have proven
to be helpful in solving the given question.

Programming Assignment
----------------------

Solved in ``week2-1.py``


**Notes and Links**

.. [#] Pip worked on Mac OSX (Mavericks, 10.9.4 - no XCode); the roundabout way worked on Linux Ubuntu 14.04

.. _Coursera Cryptography course: https://class.coursera.org/crypto-011
.. _PyCrypto download page: https://www.dlitz.net/software/pycrypto/
.. _PyCrypto apidocs: https://www.dlitz.net/software/pycrypto/api/current/
.. _StackOverflow CTR question: http://stackoverflow.com/questions/11656045/pycrypto-incrementing-ctr-mode
