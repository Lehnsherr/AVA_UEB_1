"""
Author: JSeyler 3603466
Date: 2017-01-21 18:54:05
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-21 18:54:05
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
