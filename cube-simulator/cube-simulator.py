# Description: A simple dice simulator that simulates a dice roll with a random number between 1 and 6.
import random

# Unicode characters for dice faces
wuerfel = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# Main loop
while True:
    eingabe = input("Drücke [Enter] zum Würfeln oder 'q' zum Beenden: ").lower()
    
    # Exit the program
    if eingabe == "q":
        print("👋 Tschüss! Bis zum nächsten Mal.")
        break

# Roll the dice
    zahl = random.randint(1, 6)
    print(f"🎲 Du hast eine {zahl} gewürfelt! {wuerfel[zahl]}")
