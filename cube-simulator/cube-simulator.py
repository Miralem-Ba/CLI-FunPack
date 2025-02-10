import random                                   # Bibliothek für Zufallszahlen

# Schleife, die so lange läuft, bis der Benutzer [q] eingibt
while True:
    input("Drücke [Enter] um zu würfeln oder [q] zum Beenden.")

    # Wenn der Benutzer [q] eingibt, wird die Schleife beendet
    if input == "q":
        print("👋 Tschüss! Bis zum nächsten Mal.")
        break

# Eine Zufallszahl zwischen 1 und 6 generieren
zahl = random.randint(1, 6)

print("Du hast gewürfelt:", zahl)
