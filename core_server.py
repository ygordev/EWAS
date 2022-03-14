# EWAS v0.1
# Módulo Principal

import os
from datetime import datetime

# import communications_server
import control
import ew
import navigation
import safety

# class Controle(self):
#     self.latAtual = 24.0
#     self.longAtual = 43.0
#     self.waypoints = []

# Arquivos que conterão os logs:
# log_comm_server.txt, log_control.txt, log_ew.py, log_nav.txt, log_safety.txt
# type 0: core_server,
# type 1: control,
# type 2: ew,
# type 3: nav,
# type 4: safety
# type 5: comm_server

def logWrite(type, info):
    if type == 0:
        file = 'core_server.txt'
    elif type == 1:
        file = 'control.txt'
    elif type == 2:
        file = 'ew.txt'
    elif type == 3:
        file = 'nav.txt'
    elif type == 4:
        file = 'safety.txt'
    elif type == 5:
        file = 'comm_server.txt'

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, 'a') as fileHandler:
        fileHandler.write("{} - {}\n".format(date, info))

logWrite(2, "Testando 4!")
logWrite(3, "Testando nav!")
