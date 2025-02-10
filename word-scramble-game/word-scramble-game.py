
import random

# Funktion zum Mischen der Buchstaben eines Wortes
def mische_wort(wort):
    """Mischt die Buchstaben eines Wortes zufällig"""
    buchstaben = list(wort)                                                                         # Wort in Buchstaben zerlegen
    random.shuffle(buchstaben)                                                                      # Buchstaben mischen
    return ''.join(buchstaben)                                                                      # Gemischte Buchstaben wieder zu einem Wort zusammenfügen

