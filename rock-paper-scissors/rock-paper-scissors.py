import random                                                   # Importiert das Zufallsmodul, um zufällige Werte zu generieren

# Definiert die Optionen des Spiels
optionen = ["Stein", "Papier", "Schere"]

# Benutzerwahl
benutzer_wahl = input("Wähle Stein, Papier oder Schere: ").capitalize()

# Computerauswahl
computer_wahl = random.choice(optionen)

# Funktion, um den Gewinner zu bestimmen
def gewinner(best, computer):
    if best == computer:
        return "Unentschieden!"                                                     # Wenn beide dasselbe wählen
    elif (best == "Stein" and computer == "Schere") or \
         (best == "Schere" and computer == "Papier") or \
         (best == "Papier" and computer == "Stein"):
        return "Du hast gewonnen! 🎉"                                               # Benutzer gewinnt
    else:
        return "Der Computer hat gewonnen! 😞"                                      # Computer gewinnt
