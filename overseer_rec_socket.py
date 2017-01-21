"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import socket
import argparse


def create_receiving_socket(host, port):
    """ Docstring """
    print("!!! ___ create_overseer_rec_socket ___ !!!")
    udp_ip = str(host)
    upd_port = int(port)

    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP
    sock.bind((udp_ip, upd_port))
    print(str(sock))
    while True:
        try:
            # buffer size is 1024 bytes
            data, addr = sock.recvfrom(1024).decode()
            upd_msg = ("received message:" + data)
            print("addr" + str(addr))
            print(upd_msg)

        except socket.timeout:
            pass


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

__parser__ = argparse.ArgumentParser(description="EchoSocket erstellen")

__parser__.add_argument(
    "-host",
    "--host",
    type=str,
    required=True,
    help="Host: zu verbindende IP Addresse")
__parser__.add_argument(
    "-port",
    "--port",
    type=str,
    required=True,
    help="Port: zu verbindender Port der IP")

# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    __args__ = __parser__.parse_args()

    __host__ = __args__.host
    __port__ = __args__.port

    print(__host__)
    print(__port__)

    create_receiving_socket(__host__, __port__)
