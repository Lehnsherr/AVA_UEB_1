"""
Created on Mon Nov 18 14:51:16 2016

@author: Joris Seyler 3603466
"""

import socket
import argparse
import queue


def create_receiving_socket(host, port, shost, sport):
    """ Docstring """
    print("!!! ___ create_receiving_socket ___ !!!")
    udp_ip = str(host)
    upd_port = int(port)

    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM)  # UDP
    sock.bind((udp_ip, upd_port))
    print(str(sock))
    while True:
        try:
            data, addr = sock.recvfrom(
                1024).decode()  # buffer size is 1024 bytes
            upd_msg = ("received message:" + data)
            print("addr" + str(addr))

            #set back to P
            sock = socket.socket(
                socket.AF_INET,  # Internet
                socket.SOCK_DGRAM)  # UDP

            sock.sendto(upd_msg.encode(), (shost, sport))
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
__parser__.add_argument(
    "-sq",
    "--senderhost",
    type=str,
    required=True,
    help="sender: Ip des Senders")
__parser__.add_argument(
    "-sh",
    "--senderport",
    type=str,
    required=True,
    help="sender: Port des Sender")

# Parsen der Kommandozeilen-Args
if __name__ == '__main__':
    __args__ = __parser__.parse_args()

    __host__ = __args__.host
    __port__ = __args__.port
    __senderhost__ = __args__.sender
    __senderport__ = __args__.sender

    print(__host__)
    print(__port__)
    print(__senderhost__)
    print(__senderport__)


    create_receiving_socket(__host__, __port__, __senderhost__, __senderport__)

    input("prompt: ")
