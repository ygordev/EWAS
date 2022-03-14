#############################
# EWAS v0.1
# Módulo de Navegação
# Escrito por Ygor Moreira Lima
#############################

# Documentação oficial pynmea2
# https://github.com/Knio/pynmea2

import pynmea2

class NavegacaoGlobal(self, origemLat, origemLong, destinoLat, destinoLong):
    self.origemLat = origemLat
    self.origemLong = origemLong
    self.destinoLat = destinoLat
    self.destinoLong = destinoLong
    return True

class NavegacaoLocal(self, posAtualLat, posAtualLong):
    return True

def mostraInformacoes(msgNMEA):
    msg = pynmea2.parse(msgNMEA)
    lat = '%02d°%07.4f′' % (msg.latitude, msg.latitude_minutes)
    long = '%02d°%07.4f′' % (msg.longitude, msg.longitude_minutes)
    print("Latitude: {}".format(lat))
    print("Longitude: {}".format(long))
    
mostraInformacoes("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
