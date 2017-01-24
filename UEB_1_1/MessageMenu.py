"""
Author: JSeyler 3603466
Date: 2017-01-23 10:43:34
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-23 10:43:34
"""

#from message import Message
from GobalFunctions import get_current_time

"""
Nimmt die versendeten Nachrichten auf,
testet ihren typ
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

def get_message_text(message):
    """ return Text einer uebergebenen Nachricht """
    message_text = find_between(message, 'Text:', ',')
    return message_text

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
