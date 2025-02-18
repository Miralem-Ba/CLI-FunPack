import random

def nearest_multiple_of_4(num):
    """Berechnet das nächste Vielfache von 4"""
    return num + (4 - num % 4) if num >= 4 else 4

def lose(player):
    """Gibt aus, wer verloren hat, und beendet das Spiel"""
    print(f"{player} HAT VERLOREN! 😢")
    print("Besseres Glück beim nächsten Mal!")
    exit(0)

def get_player_input(player, last):
    """Fragt den Spieler, wie viele Zahlen er eingeben möchte"""
    while True:
        try:
            count = int(input(f"{player}, wie viele Zahlen möchtest du eingeben? (1-3) > "))
            if 1 <= count <= 3:
                break
            print("Bitte gib eine Zahl zwischen 1 und 3 ein.")
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl zwischen 1 und 3 eingeben.")

    numbers = list(range(last + 1, last + 1 + count))
    print(f"{player} hat eingegeben:", numbers)
    return numbers

