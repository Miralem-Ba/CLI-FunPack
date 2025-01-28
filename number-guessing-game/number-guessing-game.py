import random

def number_guessing_game():
    # Zufallszahl erzeugen
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Rate eine Zahl zwischen 1 und 100: "))
        attempts += 1
        
        if guess < secret_number:
            print("Zu niedrig!")
        elif guess > secret_number:
            print("Zu hoch!")
        else:
            print(f"Richtig geraten! Du hast {attempts} Versuche gebraucht.")
            break
    
    # Nach dem Spiel fragen, ob der Benutzer noch einmal spielen möchte
    while True:  # Diese Schleife wird weiter ausgeführt, bis der Benutzer eine gültige Eingabe macht
        play_again = input("Möchtest du noch einmal spielen? (y = Ja, n = Nein): ").lower()
        
        if play_again == 'y':
            number_guessing_game()  # Rekursiver Aufruf für ein neues Spiel
            break
        elif play_again == 'n':
            print("Danke fürs Spielen! Bis zum nächsten Mal.")
            break
        else:
            print("Ungültige Eingabe. Bitte gib 'y' für Ja oder 'n' für Nein ein.")

# Spiel starten
number_guessing_game()
