
import random

# Funktion zum Mischen der Buchstaben eines Wortes
def mische_wort(wort):
    """Mischt die Buchstaben eines Wortes zufällig"""
    buchstaben = list(wort)                                                                         # Wort in Buchstaben zerlegen
    random.shuffle(buchstaben)                                                                      # Buchstaben mischen
    return ''.join(buchstaben)                                                                      # Gemischte Buchstaben wieder zu einem Wort zusammenfügen

# Hauptfunktion für das Word Scramble Game
def word_scramble():
    """Hauptfunktion für das Word Scramble Game"""
    woerter = ["python", "spiel", "computer", "programm", "entwickler", "lernen", "spass", "code"]  # Liste mit Wörtern
    punkte = 0                                                                                      # Punktestand                                                                 
    
    # Spielablauf
    while True:
        # Zufälliges Wort auswählen
        wort = random.choice(woerter)                                                               # Zufälliges Wort auswählen
        gemischtes_wort = mische_wort(wort)                                                         # Wort mischen
        
        # Spieler-Eingabe
        print(f"🔀 Errate das Wort: {gemischtes_wort}")                                             # Gemischtes Wort Erraten
        eingabe = input("Dein Tipp: ").strip().lower()                                              # Spieler-Eingabe
        
        # Richtige Antwort
        if eingabe == wort:
            print("✅ Richtig! Du bekommst einen Punkt.")
            punkte += 1

        # Falsche Antwort
        else:
            print(f"❌ Falsch! Das richtige Wort war: {wort}")
        
        # Nochmal spielen?
        nochmal = input("🔄 Nochmal spielen? (ja/nein): ").strip().lower()
        if nochmal != "ja":
            print(f"🏆 Du hast {punkte} Punkte erzielt. Danke fürs Spielen!")
            break

# Spiel starten
word_scramble()
