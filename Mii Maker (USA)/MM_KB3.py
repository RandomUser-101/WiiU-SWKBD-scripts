# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x26F82138, 0xe080e081)
tcp.pokemem(0x26F8213C, 0xe082e083)
tcp.pokemem(0x26F82140, 0xe084e085)
tcp.pokemem(0x26F82144, 0xe086e087)
tcp.pokemem(0x26F82148, 0xe088e089)
tcp.pokemem(0x26F8214C, 0xe08ae08b)
tcp.pokemem(0x26F82150, 0xe08ce08d)
tcp.pokemem(0x26F82154, 0xe08ee08f)
tcp.pokemem(0x26F82158, 0xe090e091)
tcp.pokemem(0x26F8215C, 0xe092e093)
tcp.pokemem(0x26F82160, 0xe094e095)
tcp.pokemem(0x26F82164, 0xe096e097)
tcp.pokemem(0x26F82168, 0xe098e099)
tcp.pokemem(0x26F8216C, 0x00000000)
tcp.pokemem(0x26F82170, 0x00000000)
tcp.pokemem(0x26F82174, 0x00000009)
tcp.pokemem(0x26F82178, 0x25812582)
tcp.pokemem(0x26F8217C, 0x25832584)
tcp.pokemem(0x26F82180, 0x25852586)
tcp.pokemem(0x26F82184, 0x25872588)
tcp.pokemem(0x26F82188, 0x2589534d)
tcp.pokemem(0x26F8218C, 0x2121250f)
tcp.pokemem(0x26F82190, 0x25132517)
tcp.pokemem(0x26F82194, 0x251b2523)
tcp.pokemem(0x26F82198, 0x252b2533)
tcp.pokemem(0x26F8219C, 0x253b30b7)
tcp.pokemem(0x26F821A0, 0x30c43020)
tcp.pokemem(0x26F821A4, 0x26422640)
tcp.pokemem(0x26F821A8, 0x2122339d)
tcp.pokemem(0x26F821AC, 0x339e33c4)
tcp.pokemem(0x26F821B0, 0x33cd338e)
tcp.pokemem(0x26F821B4, 0x338f339c)
tcp.s.close()
print("Hacked Keyboard 3 applied for Mii Maker!")
