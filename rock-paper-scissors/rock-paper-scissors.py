import random                                                   # Importiert das Zufallsmodul, um zufällige Werte zu generieren

# Definiert die Optionen des Spiels
optionen = ["Stein", "Papier", "Schere"]

# Benutzerwahl
benutzer_wahl = input("Wähle Stein, Papier oder Schere: ").capitalize()

# Computerauswahl
computer_wahl = random.choice(optionen)
