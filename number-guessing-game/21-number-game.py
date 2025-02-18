import random

def nearest_multiple_of_4(num):
    """Berechnet das nächste Vielfache von 4"""
    return num + (4 - num % 4) if num >= 4 else 4

def lose(player):
    """Gibt aus, wer verloren hat, und beendet das Spiel"""
    print(f"{player} HAT VERLOREN! 😢")
    print("Besseres Glück beim nächsten Mal!")
    exit(0)

