# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x15A650F8, 0xe03fe040)
tcp.pokemem(0x15A650FC, 0xe041e042)
tcp.pokemem(0x15A65100, 0xe043e044)
tcp.pokemem(0x15A65104, 0xe045e046)
tcp.pokemem(0x15A65108, 0xe047e048)
tcp.pokemem(0x15A6510C, 0xe049e04a)
tcp.pokemem(0x15A65110, 0xe04be04c)
tcp.pokemem(0x15A65114, 0xe04de04e)
tcp.pokemem(0x15A65118, 0xe04fe050)
tcp.pokemem(0x15A6511C, 0xe051e052)
tcp.pokemem(0x15A65120, 0xe053e054)
tcp.pokemem(0x15A65124, 0xe055e056)
tcp.pokemem(0x15A65128, 0xe057e058)
tcp.pokemem(0x15A6512C, 0xe059e05a)
tcp.pokemem(0x15A65130, 0xe05be05c)
tcp.pokemem(0x15A65134, 0xe05de05e)
tcp.pokemem(0x15A65138, 0xe05fe060)
tcp.pokemem(0x15A6513C, 0xe061e062)
tcp.pokemem(0x15A65140, 0xe063e064)
tcp.pokemem(0x15A65144, 0xe065e066)
tcp.pokemem(0x15A65148, 0xe067e068)
tcp.pokemem(0x15A6514C, 0xe069e06a)
tcp.pokemem(0x15A65150, 0xe06be06c)
tcp.pokemem(0x15A65154, 0xe06de06e)
tcp.pokemem(0x15A65158, 0xe06fe070)
tcp.pokemem(0x15A6515C, 0xe071e072)
tcp.pokemem(0x15A65160, 0xe073e074)
tcp.pokemem(0x15A65164, 0xe075e076)
tcp.pokemem(0x15A65168, 0xe077e078)
tcp.pokemem(0x15A6516C, 0xe079e07a)
tcp.pokemem(0x15A65170, 0xe07be07c)
tcp.pokemem(0x15A65174, 0xe07de07e)
tcp.s.close()
print("Hacked Keyboard 2 applied for Mii Maker!")
