"""
Author: JSeyler 3603466
Date: 2017-01-23 20:48:34
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-23 20:48:34
"""
import argparse

from random import randint
from subgraph import Subgraph

__entries__ = list()
__edges__ = 1

def generate_edge(node_1, random_n_count):
    """
        Generiert eine Kante zwischen
        einem festen Knoten und
        einem zufaellig gewaehlten
    """
    entry = Subgraph(node_1, randint(1, random_n_count))

    #Wenn Kante auf den Knoten selbst zeigt
    #entfernen/nicht verwenden und neue generieren
    if entry.node_1 == entry.node_2:
        return generate_edge(node_1, random_n_count)

    return entry


def generate_random_edge(random_n_count):
    """
        Generiert eine Kante zwischen
        zwei zufaellig gewaehlten Knoten
    """
    edges = randint(1, random_n_count)
    entry = generate_edge(edges, random_n_count)
    return entry


def check_for_duplicates(edges, entries):
    """
        Ueberprueft ob eine Kante
        schon in einer Liste vorhanden ist
    """
    for entry in entries:
        # __eq__ funktion des Subgraph wird aufgerufen
        if entry == edges:
            return True

    return False


def write_to_file(entries, filename):
    """
        Eintrage aus einer Liste von Kanten in eine
        Datei schreiben
    """
    with open(filename, 'w') as target:
        target.write("graph G {\n")
        for edge in entries:
            target.write(edge.generate_line() + "\n")
        target.write("}")

##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##
# Kommandozeilen-Args
##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##--##

__parser__ = argparse.ArgumentParser(description="graphgen")
__parser__.add_argument(
    "-n", "--nodeCount", type=int, required=True, help="Knotenzahl")
__parser__.add_argument(
    "-m", "--edgeCount", type=int, required=True, help="Kantenzahl")
__parser__.add_argument(
    "-f", "--filename", type=str, required=True, help="Ausgabedatei")


"""
Zufaelligen zusammenhaengenden Graphen erzeugen
"""
if __name__ == '__main__':
    # Parsen der Kommandozeilen-Args
    __args__ = __parser__.parse_args()

    #Wenn Kantenzahl kleiner Knotenzahl
    #Fehlermeldung und abbrechen
    if __args__.edgeCount < __args__.nodeCount:
        print("Kantenzahl muss groesser als Knotenzahl sein!")
        exit()

    #Fuer jeden Knoten eine Kante festlegen
    for i in range(1, __args__.nodeCount + 1):
        __entry__ = generate_edge(i, __args__.nodeCount)
        if not check_for_duplicates(__entry__, __entries__):
            __entries__.append(__entry__)
            __edges__ += 1
        else:
            i -= 1

    #Zufaellige Kanten erstellen bis die
    #Kantenzahl der gewuenschten Anzahl entspricht
    while __edges__ <= __args__.edgeCount:
        __entry__ = generate_random_edge(__args__.nodeCount)
        if not check_for_duplicates(__entry__, __entries__):
            __entries__.append(__entry__)
            __edges__ += 1

    write_to_file(__entries__, __args__.filename)
