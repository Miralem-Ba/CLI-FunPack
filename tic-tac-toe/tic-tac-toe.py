# Das Tic Tac Toe Spielfeld
def drucke_brett(brett):
    for zeile in brett:
        print(" | ".join(zeile))
        print("-" * 5)  # Trennt die Zeilen durch Linien

# Start des Spiels
brett = [[" " for _ in range(3)] for _ in range(3)]

# Das Spiel
def frage_nach_zug(brett, symbol):
    while True:
        try:
            zug = int(input(f"Spieler {symbol}, wähle ein Feld (1-9): "))
            if zug < 1 or zug > 9:
                print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 9.")
                continue
            zeile = (zug - 1) // 3
            spalte = (zug - 1) % 3
            if brett[zeile][spalte] != " ":
                print("Das Feld ist bereits belegt. Wähle ein anderes Feld.")
            else:
                brett[zeile][spalte] = symbol
                break
        except ValueError:
            print("Ungültige Eingabe. Bitte gib eine Zahl ein.")

# Überprüfen, ob ein Spieler gewonnen hat
def tictactoe():
    brett = [[" " for _ in range(3)] for _ in range(3)]  # Das Spielfeld initialisieren
    spieler = "X"  # Spieler X beginnt

    drucke_brett(brett)

    for zug in range(9):
        frage_nach_zug(brett, spieler)
        drucke_brett(brett)

        # Überprüfen, ob der aktuelle Spieler gewonnen hat
        if pruefe_gewinner(brett, spieler):
            print(f"Spieler {spieler} hat gewonnen! 🎉")
            break

        # Wechsel zum anderen Spieler
        spieler = "O" if spieler == "X" else "X"

    else:
        print("Das Spiel endet unentschieden! 👾")

# Das Spiel starten
tictactoe()
