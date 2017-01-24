"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import socket
import argparse
import select


def overseer_rec_socket(recevier):
    """ Docstring """
    nid, rec_ip, rec_port = recevier.split(":")
    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind((rec_ip, int(rec_port)))
    #print(str(sock))

    sock.setblocking(0)
    timeout_in_seconds = 10
    ready = select.select([sock], [], [], timeout_in_seconds)
    if ready[0]:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()
        upd_msg = ("received message:" + msg)
        print("addr" + str(addr))
        print(upd_msg)


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

__parser__ = argparse.ArgumentParser(description="EchoSocket erstellen")

__parser__.add_argument(
    "-recevier",
    "--recevier",
    type=str,
    required=True,
    help="Host: zu verbindende IP Addresse")

# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    #print("!!! ___ create_overseer_rec_socket ___ !!!")
    __args__ = __parser__.parse_args()

    #__host__ = __args__.host
    #__port__ = __args__.port
    __rec__ = __args__.recevier
    #print(__host__)
    #print(__port__)

    overseer_rec_socket(__rec__)
