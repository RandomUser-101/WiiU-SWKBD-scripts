# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x26F8E638, 0xff51ff57)
tcp.pokemem(0x26F8E63C, 0xff45ff52)
tcp.pokemem(0x26F82640, 0xff54ff59)
tcp.pokemem(0x26F82644, 0xff55ff49)
tcp.pokemem(0x26F82648, 0xff4fff50)
tcp.pokemem(0x26F8264C, 0x0000ff41)
tcp.pokemem(0x26F82650, 0xff53ff44)
tcp.pokemem(0x26F82654, 0xff46ff47)
tcp.pokemem(0x26F82658, 0xff48ff4a)
tcp.pokemem(0x26F8265C, 0xff4bff4c)
tcp.pokemem(0x26F82660, 0x00000000)
tcp.pokemem(0x26F82664, 0xff5aff58)
tcp.pokemem(0x26F82668, 0xff43ff56)
tcp.pokemem(0x26F8266C, 0xff42ff4e)
tcp.pokemem(0x26F82670, 0xff4d0000)
tcp.pokemem(0x26F82674, 0xff01ff1f)
tcp.pokemem(0x26F82678, 0x27762777)
tcp.pokemem(0x26F8267C, 0x27782779)
tcp.pokemem(0x26F82680, 0x277a277b)
tcp.pokemem(0x26F82684, 0x277c277d)
tcp.pokemem(0x26F82688, 0x277e277f)
tcp.pokemem(0x26F8268C, 0xffe520af)
tcp.pokemem(0x26F82690, 0x210a25a1)
tcp.pokemem(0x26F82694, 0x25a225b2)
tcp.pokemem(0x26F82698, 0x25b325b7)
tcp.pokemem(0x26F8269C, 0x25bc25bd)
tcp.pokemem(0x26F826A0, 0x25c125c6)
tcp.pokemem(0x26F826A4, 0x25c725c9)
tcp.pokemem(0x26F826A8, 0x25cb25ce)
tcp.pokemem(0x26F826AC, 0x26012600)
tcp.pokemem(0x26F826B0, 0x26022603)
tcp.pokemem(0x26F826B4, 0x260e261c)
tcp.s.close()
print("Hacked Keyboard 4 applied for Mii Maker!")
