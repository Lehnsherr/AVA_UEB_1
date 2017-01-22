"""
Author: JSeyler 3603466
Date: 2017-01-21 18:48:44
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:48:44
"""

import argparse
import re
import random
import time

#import os
#import multiprocessing as mltpro

from subprocess import Popen, PIPE, CREATE_NEW_CONSOLE
from threading import Thread
from queue import Queue, Empty
from node import Node

#from connection import *
#from GobalFunctions import get_current_time


def get_node_list_from_file(nodefile):
    """
    Liest eine Liste mit Knoten ein,
    legt sie in einem Array ab und
    gibt sie zurück
    """

    nodelist = list()

    file = open(nodefile)

    with file as nodef:
        node_strings = nodef.read().splitlines()

    # Erstellt mit KnotenObjekt, Kontenlsite auss übergebene Array
    for node_line in node_strings:
        tmp_node_string = re.split('(\r| |:)', node_line)
        #print(tmp_node_string)
        tmp_node = Node(tmp_node_string[0], tmp_node_string[2],
                        tmp_node_string[4])

        #print(tmp_node_string[0])  #--> ID
        #print(tmp_node_string[1]) #--> Blank
        #print(tmp_node_string[2])  #--> Host
        #print(tmp_node_string[3]) #--> :
        #print(tmp_node_string[4] + "\n")  #--> Port
        #print(
        # "Knoten-ID: " + str(tmp_node.id)
        # + " - Host: " + str(tmp_node.host)
        # + " - Port: " + str(tmp_node.port)
        # )

        nodelist.append(tmp_node)

    #print (nodelist)
    return nodelist


def get_node_by_id(nlist, nid):
    """ Testest auf doppelte ID's in liste (Fehlermeldeung + Abbruch) """
    #print (nlist)
    node = [i for i in nlist if str(i.nid) == nid]

    #print (len(node))

    if len(node) > 1:
        print("Der Knoten mit der ID: " + nid +
              " ist doppelt in der Liste enthalten!")
        exit()

    if len(node) == 0:
        print("Der Knoten mit der ID: " + nid +
              " konnte in der Liste nicht gefunden werden!")
        exit()

    print("Der Knoten mit der ID: " + nid + " wurde gefunden.")

    return node[0]


def get_node_neighbor(count, nodelist, search_node):
    """ Eine uebergebene Anzahl von Nachbarn aus der Knotenliste auswaehlen """
    node_neighbor_list = list()

    i = 0
    #Zuletzt gesuchten Knoten aus der generierten Liste entfernen
    if search_node in nodelist:
        nodelist.remove(search_node)

    while i < count:
        #Error wenn uebergebene Liste leer ist oder Kein Noten mehr vorhanden ist
        if len(nodelist) == 0:
            print("Liste enthaelt keine Knoten.")
            exit()
        #Auswahl eines zufälligen Nachbarn innerhalb der uebergebenen Liste
        neighbor_node = random.choice(nodelist)
        node_neighbor_list.append(neighbor_node)

        #neu gewählten Knoten aus der Liste löschen
        if neighbor_node in nodelist:
            nodelist.remove(neighbor_node)

        i += 1

    return node_neighbor_list


def print_node(node):
    """ Print Funktionen """
    print("Knoten-ID: " + str(node.nid) + " - Host: " + str(node.host) +
          " - Port: " + str(node.port))


def print_node_neighbors(neighbor_list):
    """ Print Funktionen """
    i = 0
    print("\n Die Nachbarn des gesuchten Knoten:")

    for neighbor_node in neighbor_list:
        i = i + 1
        print(
            str(i) + ": " + "Knoten-ID: " + str(neighbor_node.nid) +
            " - Host: " + str(neighbor_node.host) + " - Port: " + str(
                neighbor_node.port))


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Watching both stdout and stderr
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
def stream_watcher(identifier, stream):
    """ doc string stream_watcher """
    print("stream_watcher started")
    for line in stream:
        __que__.put((identifier, line))

    if not stream.closed:
        print("Stream closed")
        stream.close()


def printer():
    """ doc string printer """
    print("printer started")
    while True:
        try:
            # Block for 1 second.
            item = __que__.get(True, 1)
        except Empty:
            # No output in either streams for a second. Are we done?
            print("printer Empty")
            if __proc_overseersock_sock__.poll() is not None:
                break
        else:
            identifier, line = item
            print("Printer " + str(identifier) + ':' + str(line))


##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

__parser__ = argparse.ArgumentParser(
    description="Basisimplementierung eines lokalen Konten")

__parser__.add_argument(
    "-l",
    "--list",
    type=str,
    required=True,
    help="Datei mit Liste der verfuegbaren Knoten")
__parser__.add_argument(
    "-id",
    "--id",
    type=str,
    required=True,
    help="ID des Knoten, Wert zwischen 1-20 ")
__parser__.add_argument(
    "-n",
    "--neighborCount",
    type=int,
    required=False,
    default=3,
    help="Anzahl der zufaellig gewaehlten Nachbarknoten")
__parser__.add_argument(
    "-c",
    "--rumorCount",
    type=int,
    required=False,
    default=1,
    help="Größe der maximalenm Gruechte-Grenzte")

if __name__ == '__main__':
    # Parsen der Kommandozeilen-Args
    __args__ = __parser__.parse_args()

    print("\n ##--##--##--##--##--##--##--##--##--##--##--##--##--##--##")

    #Knotenliste aus Datei auslesen und in Array lagern
    __nodes__ = get_node_list_from_file(__args__.list)

    #print("\n ##--##--##--##--##--##--##--##--##--##--##--##--##--##--##")

    #Uebergebene ID, Host und Port aus der Liste suchen
    __searchnode__ = get_node_by_id(__nodes__, __args__.id)

    #Attribute des gesuchten Knoten ausgeben
    print_node(__searchnode__)

    print("\n ##--##--##--##--##--##--##--##--##--##--##--##--##--##--##")

    __searchNeighbors__ = get_node_neighbor(__args__.neighborCount, __nodes__,
                                            __searchnode__)

    print_node_neighbors(__searchNeighbors__)

    print("\n ##--##--##--##--##--##--##--##--##--##--##--##--##--##--##")
    # Erstellen einer neuen FIFO Queue
    __que__ = Queue()

    __command__ = [
        "python", "overseer_rec_socket.py", "-host", __searchnode__.host,
        "-port", str(__searchnode__.port)
    ]

    #__subprocess__ = subprocess.Popen(__command__, shell=True).wait()
    __proc_overseersock_sock__ = Popen(
        __command__, stdout=PIPE, stderr=PIPE, creationflags=CREATE_NEW_CONSOLE)
    __proc_overseersock_sock__.wait()
    print("proc_overseersock_sock Returncode: " + str(
        __proc_overseersock_sock__.returncode))

    Thread(
        target=stream_watcher,
        name='stdout-watcher',
        args=('STDOUT', __proc_overseersock_sock__.stdout)).start()
    Thread(
        target=stream_watcher,
        name='stderr-watcher',
        args=('STDERR', __proc_overseersock_sock__.stderr)).start()

    for neighbor in __searchNeighbors__:

        rec_command = [
            "python", "receiving_socket.py", "-host", neighbor.host, "-port",
            str(neighbor.port), "-senderhost", (__searchnode__.host),
            "-senderport", str(__searchnode__.port)
        ]
        proc_rec_neigbor_sock = Popen(
            rec_command, creationflags=CREATE_NEW_CONSOLE)
        proc_rec_neigbor_sock.wait()
        print("proc_rec_neigbor_sock Returncode: " + str(
            proc_rec_neigbor_sock.returncode))

        time.sleep(4)

        send_command = [
            "python", "sending_socket.py", "-host", neighbor.host, "-port",
            str(neighbor.port), "-message",
            str("Mode: - NodeTyp: - Text: - Sender: -")
        ]
        Popen(send_command, creationflags=CREATE_NEW_CONSOLE).wait()

    Thread(target=printer, name='printer').start()
"""
        mltpro.set_start_method('spawn')
        queue = mltpro.Queue()
        print("Ich bin in dir ... MAIN")

        #queue = Queue()
        p = mltpro.Process(
            target=create_sending_socket(neighbor.host, neighbor.port),
            args=(queue, 1))
        p.start()
        #p.join()  # this blocks until the process terminates
        result = queue.get()
        print("Result: " + result)
"""