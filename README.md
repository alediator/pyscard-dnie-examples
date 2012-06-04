pyscard-dnie-exaples
====================

Simple APDU commands for DNIe using pyscard. View http://opendnie.cenatic.es/wiki/index.php/Documentacion_DNIe_Comandos

## Pre requisites: Pyscard instalation ##

Pyscard is the python smartcard library you need to execute this examples

### From source ###

1. Download [latest](http://sourceforge.net/projects/pyscard/files/latest/download)
2. Download and install  python dependencies
 * [distutils](http://docs.python.org/library/distutils.html)
3. Unpackage and install pyscard:
 <pre>setup.py install</pre>

### Debian package ###

<pre>~$ sudo apt-get install python-pyscard</pre>

## Exercices DNIe ##

* GET CHIP INFO
* SELECT && GET RESPONSE

### GET CHIP INFO ###

Doc reference (spanish): http://opendnie.cenatic.es/wiki/index.php/Documentacion_DNIe_Comandos#Informaci.C3.B3n_de_control_de_fichero_.28FCI.29

This example gets the serial number of the DNIe:

<pre># define the apdus used in this script
# apdu bytes
CLA=0x90
INS=0xB8
P1=0x00
P2=0x00
LE=0x07
# apdu chip info apdu
CHIP_INFO = [CLA, INS, P1, P2, LE]</pre>

and show it in console: 

<pre>    # there is a DNIe
    if sw1 == 0x90:
        print 'serial number: ', toHexString(response)</pre>

To execute: 

<pre>~$ ./getCHIP_INFO_dnie.py 
insert a card (SIM card if possible) within 10s
connecting to C3PO LTC31 (80060327) 00 00
&gt;  90 B8 00 00 07
&lt;  ** ** ** ** ** ** ** 90 0 
serial number:  ** ** ** ** ** ** **
disconnecting from C3PO LTC31 (80060327) 00 00
disconnecting from C3PO LTC31 (80060327) 00 00
~$
</pre>


### SELECT && GET RESPONSE ###

Doc reference (spanish): 

* [SELECT](http://opendnie.cenatic.es/wiki/index.php/Documentacion_DNIe_Comandos#SELECT)
* [GET RESPONSE](http://opendnie.cenatic.es/wiki/index.php/Documentacion_DNIe_Comandos#GET_RESPONSE)

This example reads the 0x60, 0x1F path in a DNIe:

<pre>$ ./selectDNIe.py 
insert a card (SIM card if possible) within 10s
connecting to C3PO LTC31 (80060327) 00 00
&gt;  00 A4 00 00 02 60 1F
&lt;  []  61 E 
&gt;  00 C0 00 00 0E
&lt;  ** ** ** ** ** ** ** ** ** ** ** ** ** ** 90 0 
disconnecting from C3PO LTC31 (80060327) 00 00
disconnecting from C3PO LTC31 (80060327) 00 00</pre>


