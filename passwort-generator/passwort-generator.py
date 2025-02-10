import random                                                                                   # Zufallszahlen generieren          
import string                                                                                   # Zeichen definieren

# Zeichen definieren
buchstaben_klein = string.ascii_lowercase                                                       # a-z
buchstaben_groß = string.ascii_uppercase                                                        # A-Z
zahlen = string.digits                                                                          # 0-9    
sonderzeichen = string.punctuation                                                              # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~   

# Alle Zeichen zusammenfügen
alle_zeichen = buchstaben_klein + buchstaben_groß + zahlen + sonderzeichen

# Funktion zum Erstellen eines Passworts
def passwort_erstellen(laenge):
    return ''.join(random.choice(alle_zeichen) for _ in range(laenge))

# Interaktiver Modus
while True:
    try:
        # Passwortlänge abfragen
        laenge = int(input("Wie lang soll das Passwort sein? (Min. 6 Zeichen): "))
        if laenge < 6:
            print("Das Passwort sollte mindestens 6 Zeichen lang sein!")
            continue

        # Passwort generieren
        passwort = passwort_erstellen(laenge)
        print(f"🔐 Dein Passwort: {passwort}")

        # weiteres Passwort generieren
        nochmal = input("Möchtest du ein weiteres Passwort generieren? (ja/nein): ").lower()
        if nochmal != "ja":
            print("👋 Viel Spaß mit deinem neuen Passwort!")
            break
        
    # Fehlermeldung bei falscher Eingabe
    except ValueError:
        print("Bitte gib eine Zahl ein!")
