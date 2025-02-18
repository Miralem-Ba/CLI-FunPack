import random

def nearest_multiple_of_4(num):
    """Berechnet das nächste Vielfache von 4"""
    return num + (4 - num % 4) if num >= 4 else 4

def lose(player):
    """Gibt aus, wer verloren hat"""
    print(f"{player} HAT VERLOREN! 😢")
    print("Besseres Glück beim nächsten Mal!")

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

def computer_turn(last):
    """Berechnet die optimale Eingabe des Computers"""
    near = nearest_multiple_of_4(last)
    count = near - last if 1 <= near - last <= 3 else random.randint(1, 3)
    numbers = list(range(last + 1, last + 1 + count))
    print("Der Computer hat eingegeben:", numbers)
    return numbers

def play_21_game():
    """Das Hauptspiel - Einzelspieler gegen den Computer oder Multiplayer"""
    print("Willkommen zum 21er-Spiel! 🎮")
    print("1️⃣ Singleplayer (Gegen Computer)")
    print("2️⃣ Multiplayer (Gegen einen Freund)")

    while True:
        mode = input("Wähle den Modus (1 oder 2) > ").strip()
        if mode in ['1', '2']:
            break
        print("Ungültige Auswahl! Bitte 1 oder 2 eingeben.")

    player1 = "Spieler 1"
    player2 = "Computer" if mode == '1' else "Spieler 2"

    # Entscheide, wer beginnt
    first_turn = input("Möchtest du zuerst spielen? (J/N) > ").strip().upper()
    player_turn = first_turn == 'J'

    last = 0
    numbers_list = []

    while last < 21:
        if player_turn:
            numbers = get_player_input(player1, last)
        else:
            numbers = computer_turn(last) if mode == '1' else get_player_input(player2, last)

        numbers_list.extend(numbers)
        last = numbers_list[-1]

        if last >= 21:
            lose(player1 if player_turn else player2)
            return  # Beendet das Spiel und fragt danach, ob der Spieler erneut spielen möchte

        player_turn = not player_turn  # Wechsel zwischen den Spielern

    print("🎉 GLÜCKWUNSCH! DU HAST GEWONNEN! 🎉")

# Spiel starten
while True:
    start_game = input("Möchtest du das 21er-Spiel spielen? (Ja/Nein) > ").strip().lower()
    if start_game == "ja":
        play_21_game()
    elif start_game == "nein":
        print("Spiel beendet. 👋")
        break
    else:
        print("Ungültige Eingabe, bitte 'Ja' oder 'Nein' eingeben.")
