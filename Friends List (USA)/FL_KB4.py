# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x235FDEF8, 0xff51ff57)
tcp.pokemem(0x235FDEFC, 0xff45ff52)
tcp.pokemem(0x235FDF00, 0xff54ff59)
tcp.pokemem(0x235FDF04, 0xff55ff49)
tcp.pokemem(0x235FDF08, 0xff4fff50)
tcp.pokemem(0x235FDF0C, 0x0000ff41)
tcp.pokemem(0x235FDF10, 0xff53ff44)
tcp.pokemem(0x235FDF14, 0xff46ff47)
tcp.pokemem(0x235FDF18, 0xff48ff4a)
tcp.pokemem(0x235FDF1C, 0xff4bff4c)
tcp.pokemem(0x235FDF20, 0x00000000)
tcp.pokemem(0x235FDF24, 0xff5aff58)
tcp.pokemem(0x235FDF28, 0xff43ff56)
tcp.pokemem(0x235FDF2C, 0xff42ff4e)
tcp.pokemem(0x235FDF30, 0xff4d0000)
tcp.pokemem(0x235FDF34, 0xff01ff1f)
tcp.pokemem(0x235FDF38, 0x27762777)
tcp.pokemem(0x235FDF3C, 0x27782779)
tcp.pokemem(0x235FDF40, 0x277a277b)
tcp.pokemem(0x235FDF44, 0x277c277d)
tcp.pokemem(0x235FDF48, 0x277e277f)
tcp.pokemem(0x235FDF4C, 0xffe520af)
tcp.pokemem(0x235FDF50, 0x210a25a1)
tcp.pokemem(0x235FDF54, 0x25a225b2)
tcp.pokemem(0x235FDF58, 0x25b325b7)
tcp.pokemem(0x235FDF5C, 0x25bc25bd)
tcp.pokemem(0x235FDF60, 0x25c125c6)
tcp.pokemem(0x235FDF64, 0x25c725c9)
tcp.pokemem(0x235FDF68, 0x25cb25ce)
tcp.pokemem(0x235FDF6C, 0x26012600)
tcp.pokemem(0x235FDF70, 0x26022603)
tcp.pokemem(0x235FDF74, 0x260e261c)
tcp.s.close()
print("Hacked Keyboard 4 applied for Friend List!")
