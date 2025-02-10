import random

# Funktion zum Anzeigen des Spielfelds
def drucke_brett(brett):
    for zeile in brett:
        print(" | ".join(zeile))
        print("-" *10)

# Funktion zur Eingabe des Spielers
def frage_nach_zug(brett, symbol):
    while True:
        try:
            zug = int(input(f"Spieler {symbol}, wähle ein Feld (1-9): "))
            if zug < 1 or zug > 9:
                print("❌ Ungültige Eingabe. Wähle eine Zahl zwischen 1 und 9.")
                continue

            zeile = (zug - 1) // 3
            spalte = (zug - 1) % 3

            if brett[zeile][spalte] != " ":
                print("❌ Das Feld ist belegt. Wähle ein anderes Feld.")
            else:
                brett[zeile][spalte] = symbol
                break
        except ValueError:
            print("❌ Ungültige Eingabe. Bitte gib eine Zahl ein.")

# Funktion zur Überprüfung des Gewinners
def pruefe_gewinner(brett, symbol):
    for i in range(3):
        if all([feld == symbol for feld in brett[i]]):  # Horizontale Überprüfung
            return True
        if all([brett[j][i] == symbol for j in range(3)]):  # Vertikale Überprüfung
            return True

    if all([brett[i][i] == symbol for i in range(3)]):  # Linke Diagonale
        return True
    if all([brett[i][2 - i] == symbol for i in range(3)]):  # Rechte Diagonale
        return True

    return False

# Funktion für den Computer-Zug (zufälliger freier Platz)
def computer_zug(brett):
    freie_felder = [(i, j) for i in range(3) for j in range(3) if brett[i][j] == " "]
    if freie_felder:
        zeile, spalte = random.choice(freie_felder)
        brett[zeile][spalte] = "O"  # Der Computer spielt immer "O"

# Hauptfunktion für das Spiel
def tictactoe(spielmodus):
    brett = [[" " for _ in range(3)] for _ in range(3)]
    spieler = "X"  # Spieler X beginnt

    drucke_brett(brett)

    for zug in range(9):
        if spielmodus == "1" and spieler == "O":  # Einzelspieler-Modus -> Computer ist dran
            print("💻 Der Computer macht seinen Zug...")
            computer_zug(brett)
        else:  # Menschlicher Spieler ist dran
            frage_nach_zug(brett, spieler)

        drucke_brett(brett)

        if pruefe_gewinner(brett, spieler):
            print(f"🏆 Spieler {spieler} hat gewonnen! 🎉")
            break

        spieler = "O" if spieler == "X" else "X"  # Spieler wechseln

    else:
        print("🤝 Das Spiel endet unentschieden!")

# Menü zum Auswählen des Spielmodus
def menue():
    while True:
        print("\n🎮 Willkommen bei Tic Tac Toe!")
        print("1️⃣ Einzelspieler (gegen Computer)")
        print("2️⃣ Mehrspieler (2 Spieler)")
        auswahl = input("Wähle den Modus (1 oder 2): ")

        if auswahl in ["1", "2"]:
            tictactoe(auswahl)
            break
        else:
            print("❌ Ungültige Eingabe. Bitte wähle 1 oder 2.")

# Spiel starten
menue()
