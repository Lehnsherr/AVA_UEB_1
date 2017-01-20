# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 17:51:36 2016

@author: Joris Seyler 3603466
"""

class Node:
    """
    Klasse Knoten
    Parm:
        host: ip Addresse
        post: 4 Stelliger Port
    """
    def __init__(self, nid, host, port):
        self.nid = int(nid)
        self.host = host
        self.port = int(port)
