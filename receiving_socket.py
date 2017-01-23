"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import socket
import argparse
import select

from MessageMenu import check_message_type
#import queue


def create_receiving_socket(host, port, s_host, s_port):
    """ Docstring """
    msg = None
    udp_ip = str(host)
    upd_port = int(port)
    p_ip = str(s_host)
    p_port = int(s_port)

    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP
    sock.bind((udp_ip, upd_port))
    print(str(sock))

    sock.setblocking(0)
    timeout_in_seconds = 10
    ready = select.select([sock], [], [], timeout_in_seconds)
    if ready[0]:

        #while True:
        data, addr = sock.recvfrom(1024)

        upd_msg = data.decode()
        msg = ("received message:" + upd_msg)
        print(msg)
        print("addr" + str(addr))
        message_type = check_message_type(msg)
        if message_type == "spreadRumor":
            print("test test ")
            sock_p = socket.socket(
                socket.AF_INET,  # Internet
                socket.SOCK_DGRAM)  # UDP

            sock_p.sendto(msg.encode(), (p_ip, p_port))

    #set back to P
    if msg == "" or msg == None:
        msg = "Error"

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
__parser__.add_argument(
    "-senderhost",
    "--senderhost",
    type=str,
    required=True,
    help="sender: Ip des Senders")
__parser__.add_argument(
    "-senderport",
    "--senderport",
    type=str,
    required=True,
    help="sender: Port des Sender")

# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    print("!!! ___ create_receiving_socket ___ !!!")
    __args__ = __parser__.parse_args()

    __host__ = __args__.host
    __port__ = __args__.port
    __senderhost__ = __args__.senderhost
    __senderport__ = __args__.senderport

    #print(__host__)
    #print(__port__)
    #print(__senderhost__)
    #print(__senderport__)

    create_receiving_socket(__host__, __port__, __senderhost__, __senderport__)
    #input("prompt: ")
