import random  # Importiert das Modul für zufällige Zahlen (für den Computer-Gegner)

# Funktion zur Darstellung des Spielfelds
def drucke_brett(brett):
    """ Gibt das aktuelle Spielfeld aus. """
    for zeile in brett:
        print(" | ".join(zeile))
        print("-" *10)

# Funktion zur Spieler-Eingabe und Validierung
def frage_nach_zug(brett, symbol):
    """ Fragt den Spieler nach seinem Zug und überprüft die Eingabe. """
    while True:
        try:
            zug = int(input(f"Spieler {symbol}, wähle ein Feld (1-9): "))                                            # Eingabe als Zahl
            if zug < 1 or zug > 9:
                print("❌ Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 9.")
                continue

            # Berechnung der Zeile und Spalte aus der Eingabe
            zeile = (zug - 1) // 3                                                                                  # Zeile berechnen (0-2)
            spalte = (zug - 1) % 3                                                                                  # Spalte berechnen (0-2)

            if brett[zeile][spalte] != " ":
                print("❌ Das Feld ist belegt. Wähle ein anderes Feld.")
            else:
                brett[zeile][spalte] = symbol                                                                       # Setzt das Symbol ins Spielfeld
                break
        except ValueError:
            print("❌ Ungültige Eingabe. Bitte gib eine Zahl ein.")

# Funktion zur Überprüfung, ob ein Spieler gewonnen hat
def pruefe_gewinner(brett, symbol):
    """ Prüft, ob ein Spieler gewonnen hat. """
    for i in range(3):
        if all([feld == symbol for feld in brett[i]]):                                                              # Horizontale Überprüfung
            return True
        if all([brett[j][i] == symbol for j in range(3)]):                                                          # Vertikale Überprüfung
            return True

    # Diagonalen überprüfen
    if all([brett[i][i] == symbol for i in range(3)]):                                                              # Linke Diagonale (0,0 -> 1,1 -> 2,2)
        return True
    if all([brett[i][2 - i] == symbol for i in range(3)]):                                                          # Rechte Diagonale (0,2 -> 1,1 -> 2,0)
        return True

    return False                                                                                                    # Kein Gewinner

# Funktion für den Computerzug im Einzelspielermodus
def computer_zug(brett):
    """ Der Computer wählt ein zufälliges freies Feld. """
    freie_felder = [(i, j) for i in range(3) for j in range(3) if brett[i][j] == " "]                               # Alle freien Felder
    if freie_felder:
        zeile, spalte = random.choice(freie_felder)                                                                 # Zufälliges Feld auswählen
        brett[zeile][spalte] = "O"                                                                                  # Computer setzt "O"

# Funktion zur Wiederholung des Spiels
def erneut_spielen():
    """ Fragt den Spieler, ob er nochmal spielen will (nur 'ja' oder 'nein' erlaubt). """
    while True:
        nochmal = input("🔄 Nochmal spielen? (ja/nein): ").strip().lower()
        if nochmal in ["ja", "nein"]:
            return nochmal == "ja"
        print("❌ Ungültige Eingabe. Bitte gib 'ja' oder 'nein' ein.")

# Hauptspiellogik für Tic-Tac-Toe
def tictactoe(spielmodus):
    """ Hauptspiel mit Wiederholung, falls der Spieler nochmals spielen will. """
    while True:
        # Erstelle ein leeres Spielfeld
        brett = [[" " for _ in range(3)] for _ in range(3)]
        spieler = "X"                                                                                               # Spieler X beginnt

        drucke_brett(brett)

        # Es gibt maximal 9 Züge (da das Spielfeld 3x3 ist)
        for zug in range(9):                                                                                        # Maximal 9 Züge möglich
            if spielmodus == "1" and spieler == "O":                                                                # Einzelspieler-Modus -> Computer ist dran
                print("💻 Der Computer macht seinen Zug...")
                computer_zug(brett)
            else:                                                                                                   # Menschlicher Spieler ist dran
                frage_nach_zug(brett, spieler)

            drucke_brett(brett)                                                                                     # Spielfeld nach jedem Zug neu ausgeben

            # Prüfen, ob der aktuelle Spieler gewonnen hat
            if pruefe_gewinner(brett, spieler):
                print(f"🏆 Spieler {spieler} hat gewonnen! 🎉")
                break                                                                                                   # Beendet die Schleife und damit das Spiel

            # Wechsel des Spielers
            spieler = "O" if spieler == "X" else "X"

        else:
            print("🤝 Das Spiel endet unentschieden!")

        # Frage, ob der Spieler nochmal spielen will
        if not erneut_spielen():
            print("👋 Danke fürs Spielen! Bis zum nächsten Mal! 😊")
            break  

# Hauptmenü zur Auswahl des Spielmodus
def menue():
    """ Hauptmenü für die Auswahl des Spielmodus. """
    while True:
        print("\n🎮 Willkommen bei Tic Tac Toe!")
        print("1️⃣ Einzelspieler (gegen Computer)")
        print("2️⃣ Mehrspieler (2 Spieler)")
        auswahl = input("Wähle den Modus (1 oder 2): ")

        if auswahl in ["1", "2"]:
            tictactoe(auswahl)                                                                                      # Starte das Spiel mit gewähltem Modus
            break
        else:
            print("❌ Ungültige Eingabe. Bitte wähle 1 oder 2.")

# Spiel starten
menue()
