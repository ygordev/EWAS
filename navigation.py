# EWAS v0.1
# Módulo de Navegação

import pynmea2

'''
class NavegacaoGlobal(self, origemLat, origemLong, destinoLat, destinoLong):
    self.origemLat = origemLat
    self.origemLong = origemLong
    self.destinoLat = destinoLat
    self.destinoLong = destinoLong

'''

msg = pynmea2.parse("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
print(msg.lat)