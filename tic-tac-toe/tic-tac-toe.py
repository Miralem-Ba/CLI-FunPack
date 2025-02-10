# Funktion zum Anzeigen des Spielfelds
def drucke_brett(brett):
    """
    Diese Funktion gibt das Spielfeld aus.
    Es geht durch jede Zeile der Liste und formatiert die Ausgabe.
    """
    for zeile in brett:
        print(" | ".join(zeile))                                                                                     # Trennt die Spalten mit "|"
        print("-" *10)                                                                                               # Erstellt eine Trennlinie zwischen den Zeilen

# Funktion zur Eingabe des Spielers
def frage_nach_zug(brett, symbol):
    """
    Diese Funktion fragt den Spieler, in welches Feld er seinen Zug setzen möchte.
    Es überprüft, ob die Eingabe gültig ist und ob das Feld bereits belegt ist.
    """
    while True:
        try:
            zug = int(input(f"Spieler {symbol}, wähle ein Feld (1-9): "))                                           # Eingabe des Spielers als Zahl
            if zug < 1 or zug > 9:
                print("❌ Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 9.")
                continue

            # Umrechnung der Eingabe (1-9) in eine 2D-Listenposition (0-2 für Zeile, 0-2 für Spalte)
            zeile = (zug - 1) // 3                                                                                  # Berechnet die Zeile
            spalte = (zug - 1) % 3                                                                                  # Berechnet die Spalte

            # Prüfen, ob das Feld bereits belegt ist
            if brett[zeile][spalte] != " ":
                print("❌ Das Feld ist bereits belegt. Wähle ein anderes Feld.")
            else:
                brett[zeile][spalte] = symbol                                                                        # Setzt das Symbol des Spielers ins Spielfeld
                break
        except ValueError:
            print("❌ Ungültige Eingabe. Bitte gib eine Zahl ein.")

# Funktion zur Überprüfung des Gewinners
def pruefe_gewinner(brett, symbol):
    """
    Diese Funktion überprüft, ob ein Spieler gewonnen hat.
    Es werden horizontale, vertikale und diagonale Reihen geprüft.
    """
    # Überprüfung von horizontalen und vertikalen Reihen
    for i in range(3):
        if all([feld == symbol for feld in brett[i]]):                                                              # Horizontale Überprüfung
            return True
        if all([brett[j][i] == symbol for j in range(3)]):                                                          # Vertikale Überprüfung
            return True

    # Überprüfung der beiden Diagonalen
    if all([brett[i][i] == symbol for i in range(3)]):                                                              # Linke Diagonale (0,0 -> 1,1 -> 2,2)
        return True
    if all([brett[i][2 - i] == symbol for i in range(3)]):                                                          # Rechte Diagonale (0,2 -> 1,1 -> 2,0)
        return True

    return False                                                                                                    # Kein Gewinner

# Hauptfunktion des Spiels
def tictactoe():
    """
    Diese Funktion startet das Tic Tac Toe Spiel.
    Die Spieler setzen abwechselnd ihre Zeichen, bis ein Spieler gewinnt oder ein Unentschieden erreicht wird.
    """
    # Initialisiere das Spielfeld mit leeren Feldern
    brett = [[" " for _ in range(3)] for _ in range(3)]
    spieler = "X"                                                                                                   # Spieler X beginnt

    # Ausgabe des leeren Spielfelds
    drucke_brett(brett)

    for zug in range(9):                                                                                            # Maximal 9 Züge möglich
        frage_nach_zug(brett, spieler)                                                                              # Spieler macht seinen Zug
        drucke_brett(brett)                                                                                         # Aktualisiertes Spielfeld ausgeben

        # Prüfen, ob der Spieler gewonnen hat
        if pruefe_gewinner(brett, spieler):
            print(f"🏆 Spieler {spieler} hat gewonnen! 🎉")
            break

        # Wechsel des Spielers nach jedem Zug
        spieler = "O" if spieler == "X" else "X"

    else:
        print("🤝 Das Spiel endet unentschieden!")

# Spiel starten
tictactoe()
