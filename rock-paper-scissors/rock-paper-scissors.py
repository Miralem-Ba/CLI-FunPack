# importiere das random Modul, um zufällige Auswahl zu treffen
import random

# Optionen für das Spiel
optionen = ["Stein", "Papier", "Schere"]

# Funktion, um den Gewinner zu bestimmen
def gewinner(best, computer):
    if best == computer:
        return "Unentschieden!"
    elif (best == "Stein" and computer == "Schere") or \
         (best == "Schere" and computer == "Papier") or \
         (best == "Papier" and computer == "Stein"):
        return "Du hast gewonnen! 🎉"
    else:
        return "Der Computer hat gewonnen! 😞"

# Willkommensnachricht
print("🎉 Willkommen zu Schere, Stein, Papier! 🎉\n")

while True:
    # Benutzerwahl
    benutzer_wahl = input("Wähle Stein, Papier oder Schere (oder 'quit' zum Beenden): ").capitalize()

    # Beenden, wenn der Benutzer "quit" eingibt
    if benutzer_wahl == "Quit":
        print("Danke fürs Spielen! 👋")
        break

    # Überprüfen, ob die Eingabe gültig ist
    if benutzer_wahl not in optionen:
        print("❌ Ungültige Eingabe! Bitte wähle Stein, Papier oder Schere.")
        continue

    # Computerauswahl
    computer_wahl = random.choice(optionen)
    print(f"Der Computer wählt: {computer_wahl}")

    # Bestimme den Gewinner
    ergebnis = gewinner(benutzer_wahl, computer_wahl)
    print(ergebnis)

    # Option, um nochmal zu spielen
    nochmal = input("\nMöchtest du nochmal spielen? (ja/nein): ").lower()
    if nochmal != "ja":
        print("Danke fürs Spielen! 👋")
        break
