# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x235FDEF8, 0x30423044)
tcp.pokemem(0x235FDEFC, 0x30463048)
tcp.pokemem(0x235FDF00, 0x304A304B)
tcp.pokemem(0x235FDF04, 0x304C304D)
tcp.pokemem(0x235FDF08, 0x304e304f)
tcp.pokemem(0x235FDF0C, 0x30513053)
tcp.pokemem(0x235FDF10, 0x30553057)
tcp.pokemem(0x235FDF14, 0x3059305B)
tcp.pokemem(0x235FDF18, 0x305D305F)
tcp.pokemem(0x235FDF1C, 0x30613063)
tcp.pokemem(0x235FDF20, 0x30663068)
tcp.pokemem(0x235FDF24, 0x306a306b)
tcp.pokemem(0x235FDF28, 0x306c306d)
tcp.pokemem(0x235FDF2C, 0x306e306f)
tcp.pokemem(0x235FDF30, 0x30723075)
tcp.pokemem(0x235FDF34, 0x3078307B)
tcp.pokemem(0x235FDF38, 0x307F3080)
tcp.pokemem(0x235FDF3C, 0x30813082)
tcp.pokemem(0x235FDF40, 0x30833085)
tcp.pokemem(0x235FDF44, 0x30873089)
tcp.pokemem(0x235FDF48, 0x308a308b)
tcp.pokemem(0x235FDF4C, 0x308c308e)
tcp.pokemem(0x235FDF50, 0x30903091)
tcp.pokemem(0x235FDF54, 0x30923093)
tcp.pokemem(0x235FDF58, 0x30943099)
tcp.pokemem(0x235FDF5C, 0x309a309b)
tcp.pokemem(0x235FDF60, 0x309c309d)
tcp.pokemem(0x235FDF64, 0x309e0000)
tcp.pokemem(0x235FDF68, 0x00000000)
tcp.pokemem(0x235FDF6C, 0x00000000)
tcp.pokemem(0x235FDF70, 0x00000000)
tcp.pokemem(0x235FDF74, 0x00000000)
tcp.s.close()
print("Hacked Keyboard 4 applied for Friend List!")
