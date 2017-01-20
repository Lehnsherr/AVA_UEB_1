""" Funktionen die ueberall zur Verfuegung stehen"""
import time


def get_current_time():
    """ Return Zeit im Format Bsp: Tue 17 Jan 2017 11:53:46"""
    currenttime = time.localtime()
    formatcurrenttime = time.strftime("%a %d %b %Y %H:%M:%S", currenttime)
    return formatcurrenttime
    