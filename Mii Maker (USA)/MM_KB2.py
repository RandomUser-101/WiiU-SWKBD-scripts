# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x26F82138, 0xe03fe040)
tcp.pokemem(0x26F8213C, 0xe041e042)
tcp.pokemem(0x26F82140, 0xe043e044)
tcp.pokemem(0x26F82144, 0xe045e046)
tcp.pokemem(0x26F82148, 0xe047e048)
tcp.pokemem(0x26F8214C, 0xe049e04a)
tcp.pokemem(0x26F82150, 0xe04be04c)
tcp.pokemem(0x26F82154, 0xe04de04e)
tcp.pokemem(0x26F82158, 0xe04fe050)
tcp.pokemem(0x26F8215C, 0xe051e052)
tcp.pokemem(0x26F82160, 0xe053e054)
tcp.pokemem(0x26F82164, 0xe055e056)
tcp.pokemem(0x26F82168, 0xe057e058)
tcp.pokemem(0x26F8216C, 0xe059e05a)
tcp.pokemem(0x26F82170, 0xe05be05c)
tcp.pokemem(0x26F82174, 0xe05de05e)
tcp.pokemem(0x26F82178, 0xe05fe060)
tcp.pokemem(0x26F8217C, 0xe061e062)
tcp.pokemem(0x26F82180, 0xe063e064)
tcp.pokemem(0x26F82184, 0xe065e066)
tcp.pokemem(0x26F82188, 0xe067e068)
tcp.pokemem(0x26F8218C, 0xe069e06a)
tcp.pokemem(0x26F82190, 0xe06be06c)
tcp.pokemem(0x26F82194, 0xe06de06e)
tcp.pokemem(0x26F82198, 0xe06fe070)
tcp.pokemem(0x26F8219C, 0xe071e072)
tcp.pokemem(0x26F821A0, 0xe073e074)
tcp.pokemem(0x26F821A4, 0xe075e076)
tcp.pokemem(0x26F821A8, 0xe077e078)
tcp.pokemem(0x26F821AC, 0xe079e07a)
tcp.pokemem(0x26F821B0, 0xe07be07c)
tcp.pokemem(0x26F821B4, 0xe07de07e)
tcp.s.close()
print("Hacked Keyboard 2 applied for Mii Maker!")
