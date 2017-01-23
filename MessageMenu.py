"""
Author: JSeyler 3603466
Date: 2017-01-23 10:43:34
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-23 10:43:34
"""

#from message import Message
from GobalFunctions import get_current_time
"""
class MessageMenu:
    
    Nimmt die versendeten Nachrichten auf,
    testet ihren typ,
    und sendet sie entsprechend weiter
    

    def __init__(self, neighbors, sender):
        self.neighbors = neighbors
        self.sender = sender
        self.spreadrumor = False
        self.rumorcounter = 0
"""


def check_message_type(message):
    """ Ueberprueft den Typ der Nachricht """
    currenttime = get_current_time()

    #print(get_message_mode(message))
    #print(get_message_type(message))
    #print(get_message_sender(message))
    #message:Mode:APP, NodeTyp:rumor,  Text:  Sender:8, Time:Mon 23 Jan 2017 10:59:29

    print(get_message_mode(message))
    if get_message_mode(message) == "APP":
        if get_message_type(message) == "id":
            print("-->" + str(currenttime) + ": ID-Nachricht:" +
                  get_message_sender(message))
            return "Exit"
        elif get_message_type(message) == "rumor":
            print("rumor")
            return "spreadRumor"

    elif get_message_mode(message) == "Con":
        if get_message_type(message) == "Exit":
            #print("Exit")
            return "Exit"
        if get_message_type(message) == "rumor":
            #print("spreadRumor")
            return "spreadRumor"
    else:
        print("!!! " + str(currenttime) +
              " Typ der empfangenen Nachricht nicht erkannt")
        return "Exit"


def spread_rumor(self, message):
    """
        Verbreitet ein Geruecht unter den verbleibenden Knoten
        """
    currenttime = get_current_time()

    self.rumorcounter += 1
    #Wer labert den
    print("-->" + str(currenttime) + " Geruecht erhalten von " +
          get_message_sender(message))

    for neighbor in self.neighbors:
        print(neighbor.nid)
        print("Message Sender " + get_message_sender(message))

    #Wenn das Gerucht noch nicht bekannt
    if not self.spreadrumor:
        #Ist Sender Nachbar
        sender = [
            x for x in self.neighbors
            if x.nid == int(get_message_sender(message))
        ]
        print(sender)
        if sender:
            #Sender aus Liste entfernen
            if sender[0] in self.neighbors:
                self.neighbors.remove(sender[0])

            #Wenn noch Nachbarn in Listevorhanden sind
            #Weitere Geruchte versenden
            if len(self.neighbors) >= 1:
                #rumor = Message("app", "rumor", "Geruecht", self.sender[0])
                #rumor.sendtoneighbornods(self.neighbors)

                #Gerucht als bekannt ansehen
                self.spreadrumor = True
        #Wenn das Gerucht schon bekannt
        else:
            print("!!!" + str(currenttime) +
                  " Error: Geruecht wird nicht mehr weiter verbreitet")

        return self.rumorcounter

def get_message_type(message):
    """ return Typ einer uebergebenen Nachricht """
    message_type = find_between(message, 'NodeTyp:', ',')
    return message_type


def get_message_mode(message):
    """ return Mode einer uebergebenen Nachricht """
    message_mode = find_between(message, 'Mode:', ',')
    return message_mode


def get_message_sender(message):
    """ return Sender einer uebergebenen Nachricht """
    message_sender = find_between(message, 'Sender:', ',')
    return message_sender


def find_between(findstr, first, last):
    """
    Stringsplit lieftert string zwischen 'first' und 'last'
    Param:
    findstr: String der geteilt werden soll
    first:  Startpunkt
    last:   Endpunkt
    """
    try:
        start = findstr.index(first) + len(first)
        end = findstr.index(last, start)
        return findstr[start:end]
    except ValueError:
        return ""
