Vending Machine
################
:Author: David Boyd
:Term: 2017/12
:Status: COMPLETE

This program simulates a vending machine.

Features
=========

	- Set and edit products.
	- Set and edit product prices.
	- Run vending machine simulation as a customer.
	- Save vending machine data as JSON files.
	- Import saved JSON files for implementation.

DOS vs UNIX
===========

This program was originall written on a Windows machine and as such, uses a
Windows/DOS-style line endings (CR+LF).  Furthermore, it uses libraries that
are meant for a Windows environment.  However, if you were to run this code on
a Linux system, it'll require Unix-style line endings (LF).  To convert these
files in a Linux environment:

.. code:: Bash

	sudo apt-get install -y dos2unix
	dos2unix /PATH/TO/YOUR/WINDOWS_FILE

Now the program will run in a Linux environment.  If you want to convert back
to dos:

.. code:: Bash

	unix2dos /PATH/TO/YOUR/LINUX_FILE
