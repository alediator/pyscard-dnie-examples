#! /usr/bin/env python
"""
Sample script that tries to execute a GET CHALLENGE command in a DNIe.

__author__ = "http:www.emergya.es"

Copyright 2012 Emergya
Author: Alejandro Diaz Torres, mailto:adiaz@emergya.com

This file is part of pyscard-dnie-exaples.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest
from smartcard.CardConnectionObserver import ConsoleCardConnectionObserver
from smartcard.Exceptions import CardRequestTimeoutException
from smartcard.util import toHexString, toBytes

# define the apdus used in this script
GET_RESPONSE = [0x00, 0xC0, 0x00, 0x00]
# apdu bytes
CLA=0x00
INS=0x84
P1=0x00
P2=0x00
# LE get challenge (challenge length)
LE=0x08
# apdu get challenge
GET_CHALLENGE = [CLA, INS, P1, P2, LE]

# expected response
SW1_EXPECTED=0x90 

# request any card type
cardtype = AnyCardType()

try:
    # request card insertion
    print 'insert a card (SIM card if possible) within 10s'
    cardrequest = CardRequest(timeout=10, cardType=cardtype)
    cardservice = cardrequest.waitforcard()


    # attach the console tracer
    observer = ConsoleCardConnectionObserver()
    cardservice.connection.addObserver(observer)

    # connect to the card and perform a few transmits
    cardservice.connection.connect()

    # select by path 2
    apdu = GET_CHALLENGE

    response, sw1, sw2 = cardservice.connection.transmit(apdu)

    # there is a DNIe
    if sw1 == SW1_EXPECTED:
	print 'Challenge is', toHexString(response)

    else:
        print 'no DNIe'

except CardRequestTimeoutException:
    print 'time-out: no card inserted during last 10s'

except:
    import sys
    print sys.exc_info()[1]

import sys
if 'win32' == sys.platform:
    print 'press Enter to continue'
    sys.stdin.read(1)
