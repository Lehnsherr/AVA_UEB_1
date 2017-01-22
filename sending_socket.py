"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import socket
import argparse

def create_sending_socket(host, port, msg):
    """ DocString """
    udp_ip = str(host)
    upd_port = int(port)
    upd_msg = str(msg)

    #print("UDP target IP:", udp_ip)
    #print("UDP target port:", upd_port)
    #print("message:", upd_msg)

    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP

    sock.sendto(upd_msg.encode(), (udp_ip, upd_port))
    print(upd_msg + udp_ip + str(upd_port))


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

__parser__ = argparse.ArgumentParser(
    description="SendSocket erstellen")

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
__parser__.add_argument(
    "-message",
    "--message",
    type=str,
    required=True,
    help="Message: Nachricht die gesendet werden soll")

# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    print("!!! ___ create_sending_socket ___ !!!")
    __args__ = __parser__.parse_args()

    __host__ = __args__.host
    __port__ = __args__.port
    __msg__ = __args__.message

    #print(__host__)
    #print(__port__)
    #print(__msg__)

    create_sending_socket(__host__, __port__, __msg__)
