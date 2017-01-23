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

def create_receiving_socket(rec, sender):
    """ Docstring """
    msg = None
    udp_id, udp_ip, upd_port = rec.split(":")
    p_id, p_ip, p_port = sender.split(":")
 
    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP
    sock.bind((udp_ip, int(upd_port)))
    #print(str(sock))

    sock.setblocking(0)
    timeout_in_seconds = 10
    ready = select.select([sock], [], [], timeout_in_seconds)
    if ready[0]:
        data, addr = sock.recvfrom(1024)

        upd_msg = data.decode()
        msg = ("received message:" + upd_msg)
        print(msg)
        print("addr" + str(addr))
        message_type = check_message_type(msg)

        if (msg == "") or (msg == None):
            msg = "Error"
        else:
            #set back to P
            sock_p = socket.socket(
                socket.AF_INET,  # Internet
                socket.SOCK_DGRAM)  # UDP

            sock_p.sendto(upd_msg.encode(), (p_ip, int(p_port)))

        if message_type == "spreadRumor":
            #TODO spreadRumor
            print("test test")

##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

__parser__ = argparse.ArgumentParser(description="EchoSocket erstellen")

__parser__.add_argument(
    "-receiver",
    "--receiver",
    type=str,
    required=True,
    help="Knoten zu dem Verbunden werden soll ID:IP:Port")
__parser__.add_argument(
    "-sender",
    "--sender",
    type=str,
    required=True,
    help="Knoten zu dem der gesendet hat ID:IP:Port")


# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    #print("!!! ___ create_receiving_socket ___ !!!")
    __args__ = __parser__.parse_args()

    __rec__ = __args__.receiver
    __sender__ = __args__.sender
    #__senderhost__ = __args__.senderhost
    #__senderport__ = __args__.senderport

    #print(__host__)
    #print(__port__)
    #print(__senderhost__)
    #print(__senderport__)

    #create_receiving_socket(__host__, __port__, __senderhost__, __senderport__)
    create_receiving_socket(__rec__, __sender__)
    #input("prompt: ")
