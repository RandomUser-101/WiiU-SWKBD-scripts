# -*- coding: cp1252 -*-
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.178")
tcp.pokemem(0x15A650F8, 0xe000e001)
tcp.pokemem(0x15A650FC, 0xe002e003)
tcp.pokemem(0x15A65100, 0xe004e005)
tcp.pokemem(0x15A65104, 0xe006e007)
tcp.pokemem(0x15A65108, 0xe008e009)
tcp.pokemem(0x15A6510C, 0xe00ae00b)
tcp.pokemem(0x15A65110, 0xe00ce00d)
tcp.pokemem(0x15A65114, 0xe00ee00f)
tcp.pokemem(0x15A65118, 0xe010e011)
tcp.pokemem(0x15A6511C, 0xe012e013)
tcp.pokemem(0x15A65120, 0xe014e015)
tcp.pokemem(0x15A65124, 0xe015e016)
tcp.pokemem(0x15A65128, 0xe017e018)
tcp.pokemem(0x15A6512C, 0xe019e01a)
tcp.pokemem(0x15A65130, 0xe01be01c)
tcp.pokemem(0x15A65134, 0xe01de01e)
tcp.pokemem(0x15A65138, 0xe01fe020)
tcp.pokemem(0x15A6513C, 0xe021e022)
tcp.pokemem(0x15A65140, 0xe023e024)
tcp.pokemem(0x15A65144, 0xe025e026)
tcp.pokemem(0x15A65148, 0xe027e028)
tcp.pokemem(0x15A6514C, 0xe029e02a)
tcp.pokemem(0x15A65150, 0xe02be02c)
tcp.pokemem(0x15A65154, 0xe02de02e)
tcp.pokemem(0x15A65158, 0xe02fe030)
tcp.pokemem(0x15A6515C, 0xe031e032)
tcp.pokemem(0x15A65160, 0xe033e034)
tcp.pokemem(0x15A65164, 0xe035e036)
tcp.pokemem(0x15A65168, 0xe037e038)
tcp.pokemem(0x15A6516C, 0xe039e03a)
tcp.pokemem(0x15A65170, 0xe03be03c)
tcp.pokemem(0x15A65174, 0xe03de03e)
tcp.s.close()
print("Hacked Keyboard 1 applied for Minecraft!")
