# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x235FE3F8, 0x004D0061)
tcp.pokemem(0x235FE3FC, 0x00650065)
tcp.pokemem(0x235FE400, 0x00000042)
tcp.pokemem(0x235FE404, 0x00790000)
tcp.pokemem(0x235FE408, 0x00000000)
tcp.pokemem(0x235FE40C, 0x00000052)
tcp.pokemem(0x235FE410, 0x0061006E)
tcp.pokemem(0x235FE414, 0x0064006F)
tcp.pokemem(0x235FE418, 0x006D0000)
tcp.pokemem(0x235FE41C, 0x00000000)
tcp.pokemem(0x235FE420, 0x00550073)
tcp.pokemem(0x235FE424, 0x00650072)
tcp.pokemem(0x235FE428, 0x005F0031)
tcp.pokemem(0x235FE42C, 0x00300031)
tcp.pokemem(0x235FE430, 0x00000000)
tcp.pokemem(0x235FE434, 0x00000000)
tcp.pokemem(0x235FE438, 0x00000000)
tcp.pokemem(0x235FE43C, 0x00000000)
tcp.pokemem(0x235FE440, 0x00000000)
tcp.pokemem(0x235FE444, 0x00000000)
tcp.pokemem(0x235FE448, 0x00000000)
tcp.pokemem(0x235FE44C, 0x00000000)
tcp.pokemem(0x235FE450, 0x00000000)
tcp.pokemem(0x235FE454, 0x00000000)
tcp.pokemem(0x235FE458, 0x00000000)
tcp.pokemem(0x235FE45C, 0x00000000)
tcp.pokemem(0x235FE460, 0x00000000)
tcp.pokemem(0x235FE464, 0x00000000)
tcp.pokemem(0x235FE468, 0x00000000)
tcp.pokemem(0x235FE46C, 0x00000000)
tcp.pokemem(0x235FE470, 0x00000000)
tcp.pokemem(0x235FE470, 0x00000000)
tcp.pokemem(0x235FE474, 0x00000000)
tcp.s.close()
print("Credits keyboard applied for Friend List!")
