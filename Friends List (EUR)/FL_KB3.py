# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x235FE3F8, 0xe080e081)
tcp.pokemem(0x235FE3FC, 0xe082e083)
tcp.pokemem(0x235FE400, 0xe084e085)
tcp.pokemem(0x235FE404, 0xe086e087)
tcp.pokemem(0x235FE408, 0xe088e089)
tcp.pokemem(0x235FE40C, 0xe08ae08b)
tcp.pokemem(0x235FE410, 0xe08ce08d)
tcp.pokemem(0x235FE414, 0xe08ee08f)
tcp.pokemem(0x235FE418, 0xe090e091)
tcp.pokemem(0x235FE41C, 0xe092e093)
tcp.pokemem(0x235FE420, 0xe094e095)
tcp.pokemem(0x235FE424, 0xe096e097)
tcp.pokemem(0x235FE428, 0xe098e099)
tcp.pokemem(0x235FE42C, 0x00000000)
tcp.pokemem(0x235FE430, 0x00000000)
tcp.pokemem(0x235FE434, 0x00000009)
tcp.pokemem(0x235FE438, 0x25812582)
tcp.pokemem(0x235FE43C, 0x25832584)
tcp.pokemem(0x235FE440, 0x25852586)
tcp.pokemem(0x235FE444, 0x25872588)
tcp.pokemem(0x235FE448, 0x2589534d)
tcp.pokemem(0x235FE44C, 0x2121250f)
tcp.pokemem(0x235FE450, 0x25132517)
tcp.pokemem(0x235FE454, 0x251b2523)
tcp.pokemem(0x235FE458, 0x252b2533)
tcp.pokemem(0x235FE45C, 0x253b30b7)
tcp.pokemem(0x235FE460, 0x30c43020)
tcp.pokemem(0x235FE464, 0x26422640)
tcp.pokemem(0x235FE468, 0x2122339d)
tcp.pokemem(0x235FE46C, 0x339e33c4)
tcp.pokemem(0x235FE470, 0x33cd338e)
tcp.pokemem(0x235FE474, 0x338f339c)
tcp.s.close()
print("Hacked Keyboard 3 applied for Friend List!")
