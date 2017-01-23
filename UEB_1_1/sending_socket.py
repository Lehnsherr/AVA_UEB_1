"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import socket
import argparse

from GobalFunctions import get_current_time


def create_sending_socket(recevier, msg):
    """ Erstellt ein UDP Socket zum versenden von Nachrichten """
    currenttime = get_current_time()

    nid, rec_ip, rec_port = recevier.split(":")

    upd_msg = str(msg + ", Time:" + currenttime)

    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP

    sock.sendto(upd_msg.encode(), (rec_ip, int(rec_port)))
    #print(upd_msg + udp_ip + str(upd_port))

##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##


__parser__ = argparse.ArgumentParser(description="SendSocket erstellen")
__parser__.add_argument(
    "-recevier",
    "--recevier",
    type=str,
    required=True,
    help="Host: zu verbindende IP Addresse")

__parser__.add_argument(
    "-message",
    "--message",
    type=str,
    required=True,
    help="Message: Nachricht die gesendet werden soll")

# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    #print("!!! ___ create_sending_socket ___ !!!")
    __args__ = __parser__.parse_args()
    __recevier__ = __args__.recevier
    __msg__ = __args__.message

    create_sending_socket(__recevier__, __msg__)
