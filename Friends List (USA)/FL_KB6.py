# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x235FDEF8, 0x30A230A4)
tcp.pokemem(0x235FDEFC, 0x30A630A8)
tcp.pokemem(0x235FDF00, 0x30AA30AB)
tcp.pokemem(0x235FDF04, 0x30AC30AD)
tcp.pokemem(0x235FDF08, 0x30Ae30Af)
tcp.pokemem(0x235FDF0C, 0x30B130B3)
tcp.pokemem(0x235FDF10, 0x30B530B7)
tcp.pokemem(0x235FDF14, 0x30B930BB)
tcp.pokemem(0x235FDF18, 0x30BD30BF)
tcp.pokemem(0x235FDF1C, 0x30C130C3)
tcp.pokemem(0x235FDF20, 0x30C630C8)
tcp.pokemem(0x235FDF24, 0x30Ca30Cb)
tcp.pokemem(0x235FDF28, 0x30Cc30Cd)
tcp.pokemem(0x235FDF2C, 0x30Ce30Cf)
tcp.pokemem(0x235FDF30, 0x30D230D5)
tcp.pokemem(0x235FDF34, 0x30D830DB)
tcp.pokemem(0x235FDF38, 0x30DF30D0)
tcp.pokemem(0x235FD3FC, 0x30E130E2)
tcp.pokemem(0x235FDF40, 0x30E330E5)
tcp.pokemem(0x235FDF44, 0x30E730E9)
tcp.pokemem(0x235FDF48, 0x30Ea30Eb)
tcp.pokemem(0x235FDF4C, 0x30Ec30Ee)
tcp.pokemem(0x235FDF50, 0x30F030F1)
tcp.pokemem(0x235FDF54, 0x30F230F3)
tcp.pokemem(0x235FDF58, 0x30F430F9)
tcp.pokemem(0x235FDF5C, 0x30Fa30Fb)
tcp.pokemem(0x235FDF60, 0x30Fc30Fd)
tcp.pokemem(0x235FDF64, 0x30Fe0000)
tcp.pokemem(0x235FDF68, 0x00000000)
tcp.pokemem(0x235FDF6C, 0x00000000)
tcp.pokemem(0x235FDF70, 0x00000000)
tcp.pokemem(0x235FDF74, 0x00000000)
tcp.s.close()
print("Hacked Keyboard 4 applied for Friend List!")
