"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import socket
import argparse
import select


def overseer_rec_socket(host, port):
    """ Docstring """
    udp_ip = str(host)
    upd_port = int(port)

    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #print(udp_ip)
    #print(upd_port)
    sock.bind((udp_ip, upd_port))
    #print(str(sock))
    #while True:
    #    try:
            # buffer size is 1024 bytes
    sock.setblocking(0)
    timeout_in_seconds = 10
    ready = select.select([sock], [], [], timeout_in_seconds)
    if ready[0]:
        data, addr = sock.recvfrom(1024)
        msg = data.decode()
        upd_msg = ("received message:" + msg)
        print("addr" + str(addr))
        print(upd_msg)

  #      except socket.timeout:
  #          pass


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
    print("!!! ___ create_overseer_rec_socket ___ !!!")
    __args__ = __parser__.parse_args()

    __host__ = __args__.host
    __port__ = __args__.port

    #print(__host__)
    #print(__port__)

    overseer_rec_socket(__host__, __port__)
