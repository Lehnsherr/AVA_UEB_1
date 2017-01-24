"""
Author: JSeyler 3603466
Date: 2017-01-23 20:52:06
Last Modified by:   JSeyler 3603466
Last Modified time: 2017-01-23 20:52:06
"""


class Subgraph:
    """
    Klasse Subgraph
    """

    def __init__(self, node_1, node_2):
        self.node_1 = node_1
        self.node_2 = node_2
        self.sep = " -- "
        self.end = ";"

    def __eq__(self, other):
        if (self.node_1 == other.node_1 and self.node_2 == other.node_2) or (
                self.node_1 == other.node_2 and self.node_2 == other.node_1):
            return True
        return False

    #Wird nicht benutzt. Vollständigkeitshalber vorhanden
    def __ne__(self, other):
        print("__ne__ called")
        if not (self.node_1 == other.node_1 and
                self.node_2 == other.node_2) or (
                    self.node_1 == other.node_2 and
                    self.node_2 == other.node_1):
            return False
        return True

    def generate_line(self):
        """
        Print-funktion
        Gibt eine Zeile fuer eine Graphviz-Datei aus
        """
        return str(self.node_1) + self.sep + str(self.node_2) + self.end
