# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x235FE3F8, 0x30423044)
tcp.pokemem(0x235FE3FC, 0x30463048)
tcp.pokemem(0x235FE400, 0x304A304B)
tcp.pokemem(0x235FE404, 0x304C304D)
tcp.pokemem(0x235FE408, 0x304e304f)
tcp.pokemem(0x235FE40C, 0x30513053)
tcp.pokemem(0x235FE410, 0x30553057)
tcp.pokemem(0x235FE414, 0x3059305B)
tcp.pokemem(0x235FE418, 0x305D305F)
tcp.pokemem(0x235FE41C, 0x30613063)
tcp.pokemem(0x235FE420, 0x30663068)
tcp.pokemem(0x235FE424, 0x306a306b)
tcp.pokemem(0x235FE428, 0x306c306d)
tcp.pokemem(0x235FE42C, 0x306e306f)
tcp.pokemem(0x235FE430, 0x30723075)
tcp.pokemem(0x235FE434, 0x3078307B)
tcp.pokemem(0x235FE438, 0x307F3080)
tcp.pokemem(0x235FE43C, 0x30813082)
tcp.pokemem(0x235FE440, 0x30833085)
tcp.pokemem(0x235FE444, 0x30873089)
tcp.pokemem(0x235FE448, 0x308a308b)
tcp.pokemem(0x235FE44C, 0x308c308e)
tcp.pokemem(0x235FE450, 0x30903091)
tcp.pokemem(0x235FE454, 0x30923093)
tcp.pokemem(0x235FE458, 0x30943099)
tcp.pokemem(0x235FE45C, 0x309a309b)
tcp.pokemem(0x235FE460, 0x309c309d)
tcp.pokemem(0x235FE464, 0x309e0000)
tcp.pokemem(0x235FE468, 0x00000000)
tcp.pokemem(0x235FE46C, 0x00000000)
tcp.pokemem(0x235FE470, 0x00000000)
tcp.pokemem(0x235FE470, 0x00000000)
tcp.pokemem(0x235FE474, 0x00000000)
tcp.s.close()
print("Hacked Keyboard 4 applied for Friend List!")
