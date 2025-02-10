import random                                                               # Zufallszahlen-Modul
import string                                                               # Modul für Buchstaben und Sonderzeichen

# Zeichen, die im Passwort vorkommen können
buchstaben_klein = string.ascii_lowercase                                   # a-z
buchstaben_groß = string.ascii_uppercase                                    # A-Z
zahlen = string.digits                                                      # 0-9
sonderzeichen = string.punctuation                                          # !@#$%&* etc.


# Alle Zeichen zusammenfügen
alle_zeichen = buchstaben_klein + buchstaben_groß + zahlen + sonderzeichen
