# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x24AB9F38, 0xff51ff57)
tcp.pokemem(0x24AB9F3C, 0xff45ff52)
tcp.pokemem(0x24AB9F40, 0xff54ff59)
tcp.pokemem(0x24AB9F44, 0xff55ff49)
tcp.pokemem(0x24AB9F48, 0xff4fff50)
tcp.pokemem(0x24AB9F4C, 0x0000ff41)
tcp.pokemem(0x24AB9F50, 0xff53ff44)
tcp.pokemem(0x24AB9F54, 0xff46ff47)
tcp.pokemem(0x24AB9F58, 0xff48ff4a)
tcp.pokemem(0x24AB9F5C, 0xff4bff4c)
tcp.pokemem(0x24AB9F60, 0x00000000)
tcp.pokemem(0x24AB9F64, 0xff5aff58)
tcp.pokemem(0x24AB9F68, 0xff43ff56)
tcp.pokemem(0x24AB9F6C, 0xff42ff4e)
tcp.pokemem(0x24AB9F70, 0xff4d0000)
tcp.pokemem(0x24AB9F74, 0xff01ff1f)
tcp.pokemem(0x24AB9F78, 0x27762777)
tcp.pokemem(0x24AB9F7C, 0x27782779)
tcp.pokemem(0x24AB9F80, 0x277a277b)
tcp.pokemem(0x24AB9F84, 0x277c277d)
tcp.pokemem(0x24AB9F88, 0x277e277f)
tcp.pokemem(0x24AB9F8C, 0xffe520af)
tcp.pokemem(0x24AB9F90, 0x210a25a1)
tcp.pokemem(0x24AB9F94, 0x25a225b2)
tcp.pokemem(0x24AB9F98, 0x25b325b7)
tcp.pokemem(0x24AB9F9C, 0x25bc25bd)
tcp.pokemem(0x24AB9FA0, 0x25c125c6)
tcp.pokemem(0x24AB9FA4, 0x25c725c9)
tcp.pokemem(0x24AB9FA8, 0x25cb25ce)
tcp.pokemem(0x24AB9FAC, 0x26012600)
tcp.pokemem(0x24AB9FB0, 0x26022603)
tcp.pokemem(0x24AB9FB4, 0x260e261c)
tcp.s.close()
print("Hacked Keyboard 4 applied for Miiverse!")