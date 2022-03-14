#############################
# EWAS v0.1
# Módulo de Navegação
# Escrito por Ygor Moreira Lima
#############################

# Documentação oficial pynmea2
# https://github.com/Knio/pynmea2

import pynmea2

###############################################################
# Estrutura dos waypoints baseada em listas, por conta da sua fácil iteração entre os elementos
# Quantidade total de pontos: len(waypoints)
# Usage:
# waypoints[0][0] - Latitude do primeiro waypoint
# waypoints[0][1] - Longitude do primeiro waypoint
# waypoints[0][2] - Profundidade do primeiro waypoint
# ...
# waypoints[n][0] - Latitude do n-ésimo waypoint.
###############################################################

waypoints = [
    [23.1, 042.0, 15],
    [23.2, 042.0, 18],
    [23.3, 042.0, 15],
]

# class NavegacaoGlobal(self, origemLat, origemLong, destinoLat, destinoLong):
#     self.origemLat = origemLat
#     self.origemLong = origemLong
#     self.destinoLat = destinoLat
#     self.destinoLong = destinoLong
    
# class NavegacaoLocal(self, posAtualLat, posAtualLong):
    
def mostraInformacoesGPGGA(msgNMEA):
    msg = pynmea2.parse(msgNMEA)
    lat = '%02d°%07.4f′' % (msg.latitude, msg.latitude_minutes)
    long = '%02d°%07.4f′' % (msg.longitude, msg.longitude_minutes)
    print("Latitude: {}".format(lat))
    print("Longitude: {}".format(long))

def mostraInformacoesRATTM(msgNMEA):
    msg = pynmea2.parse(msgNMEA)
    target_distance = msg.distance
    target_bearing = msg.bearing
    target_speed = msg.speed
    target_course = msg.cog
    target_PMA = msg.dist_cpa
    target_bearingReference = msg.brg_ref # T / R

    print("Target Distance: {}".format(target_distance))
    print("Target Bearing: {}º {}".format(target_bearing, target_bearingReference))
    print("Target Speed: {}".format(target_speed))
    print("Target Course: {}".format(target_course))
    print("Target PMA: {}".format(target_PMA))

mostraInformacoesGPGGA("$GPGGA,184353.07,1929.045,S,02410.506,E,1,04,2.6,100.00,M,-33.9,M,,0000*6D")
mostraInformacoesRATTM("$RATTM,11,11.4,13.6,T,7.0,20.0,T,0.0,0.0,N,,Q,,154125.82,A,*17")
