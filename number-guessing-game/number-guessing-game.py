import random
import os

# Dateien, um Highscore und Statistiken zu speichern
HIGHSCORE_FILE = "highscore.txt"
STATS_FILE = "stats.txt"

# Funktion zum Laden des Highscores aus einer Datei
def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            try:
                return int(file.read())                                                                                                 # Versuche, den Highscore als Zahl zu laden
            except ValueError:
                return None                                                                                                             # Falls die Datei keine gültige Zahl enthält
    return None                                                                                                                         # Wenn die Datei nicht existiert, zurückgeben

# Funktion zum Speichern des Highscores in einer Datei
def save_highscore(highscore):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(highscore))                                                                                                      # Schreibe den Highscore in die Datei

# Funktion zum Laden der Spielstatistiken (Anzahl der Spiele und Versuche)
def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as file:
            try:
                stats = file.read().split(",")                                                                                          # Datei in zwei Teile aufteilen
                total_games = int(stats[0])                                                                                             # Anzahl der Spiele
                total_attempts = int(stats[1])                                                                                          # Gesamtzahl der Versuche
                return total_games, total_attempts
            except ValueError:
                return 0, 0                                                                                                             # Falls die Datei keine gültigen Zahlen enthält
    return 0, 0                                                                                                                         # Wenn keine Statistiken existieren, zurückgeben

# Funktion zum Speichern der Spielstatistiken in einer Datei
def save_stats(total_games, total_attempts):
    with open(STATS_FILE, "w") as file:
        file.write(f"{total_games},{total_attempts}")                                                                                   # Speichere die Gesamtstatistiken

# Funktion zur Auswahl des Schwierigkeitsgrades
def select_difficulty():
    print("Choose a level of difficulty:")
    print("1. Simple (Unlimited attempts)")                                                                                             # Unbegrenzte Versuche
    print("2. Medium (10 Attempts)")                                                                                                    # 10 Versuche
    print("3. Hard (5 Attempts)")                                                                                                       # 5 Versuche
    
    while True:
        difficulty = input("Enter the difficulty level number (1/2/3): ")
        if difficulty == '1':
            return None                                                                                                                 # Unbegrenzte Versuche
        elif difficulty == '2':
            return 10                                                                                                                   # 10 Versuche
        elif difficulty == '3':
            return 5                                                                                                                    # 5 Versuche
        else:
            print("❗ Invalid entry. Please select 1, 2, or 3.")                                                                        # Ungültige Eingabe abfangen

# Funktion zur sicheren Eingabe einer Zahl
def get_valid_number(prompt, min_value, max_value):
    while True:
        try:
            num = int(input(prompt))                                                                                                    # Versuche, die Eingabe als Zahl zu interpretieren
            if min_value <= num <= max_value:
                return num                                                                                                              # Wenn die Zahl im erlaubten Bereich liegt, zurückgeben
            else:
                print(f"❗ Please enter a number between {min_value} and {max_value}.")                                                 # Eingabebereich prüfen
        except ValueError:
            print("❗ Invalid input. Please enter a whole number.")                                                                     # Ungültige Eingabe abfangen

# Hauptspiel des Zahlraten-Spiels
def number_guessing_game():
    """
    Hauptspiel des Zahlraten-Spiels mit Schwierigkeitsgraden und Highscore-Tracking.
    """

    # Highscore und Statistiken laden
    highscore = load_highscore()                                                                                                        # Laden des Highscores
    total_games, total_attempts = load_stats()                                                                                          # Laden der Statistiken

    if highscore is not None:
        print(f"🏆 Current Highscore: {highscore} attempts")                                                                            # Wenn ein Highscore existiert, anzeigen
    else:
        print("No highscore yet. Be the first to set one!")                                                                             # Kein Highscore vorhanden

    print("Welcome to the guessing game!")
    max_attempts = select_difficulty()                                                                                                  # Schwierigkeitsgrad wählen
    secret_number = random.randint(1, 100)                                                                                              # Zufällige Zahl zwischen 1 und 100 generieren
    attempts = 0                                                                                                                        # Initialisierung der Anzahl der Versuche

    while True:

        # Wenn ein Schwierigkeitsgrad mit begrenzten Versuchen gewählt wurde
        if max_attempts is not None and attempts >= max_attempts:
            print(f"❌ You have reached the maximum number of {max_attempts} attempts. The correct number was {secret_number}.")
            break                                                                                                                       # Wenn die maximale Anzahl an Versuchen erreicht ist, das Spiel beenden

        guess = get_valid_number("Guess a number between 1 and 100: ", 1, 100)                                                          # Benutzer nach einer Zahl fragen
        attempts += 1                                                                                                                   # Zähle den Versuch

        if guess < secret_number:
            print("📉 Too low!")                                                                                                        # Hinweis, wenn die Zahl zu niedrig ist
        elif guess > secret_number:
            print("📈 Too high!")                                                                                                       # Hinweis, wenn die Zahl zu hoch ist
        else:
            print(f"🎉 You guessed right! The number was {secret_number}. You used {attempts} attempts.")                               # Erfolgreiche Eingabe

            # Highscore aktualisieren
            if highscore is None or attempts < highscore:
                highscore = attempts                                                                                                    # Setze den neuen Highscore
                save_highscore(highscore)                                                                                               # Speichere den neuen Highscore
                print(f"🏆 New highscore! You set the record with {attempts} attempts.")                                                # Bestätigung der neuen Bestmarke
            else:
                print(f"The current highscore remains {highscore} attempts.")                                                           # Wenn der Highscore nicht gebrochen wurde
            break

    # Statistiken nach dem Spiel aktualisieren
    total_games += 1
    total_attempts += attempts
    save_stats(total_games, total_attempts)

    # Statistiken anzeigen
    average_attempts = total_attempts / total_games if total_games > 0 else 0
    print("📊 Game Statistics:")
    print(f"  Total games played: {total_games}")
    print(f"  Total attempts made: {total_attempts}")
    print(f"  Average attempts per game: {average_attempts:.2f}")

    # Nach dem Spiel fragen, ob der Benutzer noch einmal spielen möchte
    while True:
        play_again = input("Would you like to play again? (y = Yes, n = No): ").lower()
        if play_again == 'y':
            number_guessing_game()                                                                                                      # Starte das Spiel neu, wenn 'y' eingegeben wird
            break
        elif play_again == 'n':
            print("Thanks for playing! See you next time.")                                                                             # Verabschiedung, wenn 'n' eingegeben wird
            break
        else:
            print("❗ Invalid input. Please enter 'y' for yes or 'n' for no.")                                                          # Fehlerhafte Eingabe abfangen

# Multiplayer-Modus für das Zahlraten-Spiel
def multiplayer_mode():
    """
    Multiplayer-Modus für das Zahlraten-Spiel
    """

    print("🎮 Welcome to Multiplayer Mode!")
    num_players = get_valid_number("Enter the number of players (2-10): ", 2, 10)                                                       # Anzahl der Spieler eingeben

    player_names = []
    for i in range(1, num_players + 1):
        name = input(f"Enter the name of Player {i}: ")                                                                                 # Namen der Spieler eingeben
        player_names.append(name)
    
    secret_number = random.randint(1, 100)                                                                                              # Zufallszahl für alle Spieler generieren
    max_attempts = select_difficulty()                                                                                                  # Schwierigkeitsgrad wählen
    scores = {name: 0 for name in player_names}                                                                                         # Spieler-Scores initialisieren

    attempts = 0
    current_player_index = 0                                                                                                            # Index des aktuellen Spielers

    while True:

        # Maximal erlaubte Versuche überprüfen
        if max_attempts is not None and attempts >= max_attempts * len(player_names):
            print(f"❌ No one guessed the number. The correct number was {secret_number}.")
            break                                                                                                                       # Wenn niemand die Zahl erraten hat, das Spiel beenden

        current_player = player_names[current_player_index]                                                                             # Bestimme den aktuellen Spieler
        print(f"It's {current_player}'s turn!")                                                                                         # Zeige an, welcher Spieler gerade an der Reihe ist
        guess = get_valid_number("Guess a number between 1 and 100: ", 1, 100)                                                          # Zahl raten lassen
        attempts += 1
        scores[current_player] += 1                                                                                                     # Zähle die Versuche des aktuellen Spielers

        if guess < secret_number:
            print("📉 Too low!")                                                                                                        # Hinweis für eine zu niedrige Zahl
        elif guess > secret_number:
            print("📈 Too high!")                                                                                                       # Hinweis für eine zu hohe Zahl
        else:
            print(f"🎉 {current_player} guessed right! The number was {secret_number}.")
            print(f"{current_player} won in {scores[current_player]} attempts!")                                                        # Gewinner anzeigen
            break                                                                                                                       # Spiel beenden, sobald jemand richtig geraten hat

        # Zum nächsten Spieler wechseln
        current_player_index = (current_player_index + 1) % len(player_names)

    print("📊 Final Scores:")
    for name, score in scores.items():
        print(f"  {name}: {score} attempts")                                                                                            # Endergebnisse für alle Spieler anzeigen

    # Wieder spielen
    while True:
        play_again = input("Would you like to play again? (y = Yes, n = No): ").lower()
        if play_again == 'y':
            multiplayer_mode()                                                                                                          # Multiplayer-Modus neu starten
            break
        elif play_again == 'n':
            print("Thanks for playing! See you next time.")                                                                             # Verabschiedung bei Spielende
            break
        else:
            print("❗ Invalid input. Please enter 'y' for yes or 'n' for no.")                                                          # Fehlerhafte Eingabe abfangen

# Hauptmenü zur Auswahl des Spielmodus
def main_menu():
    """
    Zeigt das Hauptmenü zur Auswahl des Spielmodus.
    """
    print("Welcome to the Number Guessing Game!")
    print("1. Play alone")                                                                                                              # Einspieler-Modus
    print("2. Play multiplayer")                                                                                                        # Multiplayer-Modus
    while True:
        choice = input("Select an option (1/2): ")                                                                                      # Eingabe des Spielmodus
        if choice == '1':
            number_guessing_game()                                                                                                      # Starte den Einspieler-Modus
            break
        elif choice == '2':
            multiplayer_mode()                                                                                                          # Starte den Multiplayer-Modus
            break
        else:
            print("❗ Invalid option. Please select 1 or 2.")                                                                           # Ungültige Auswahl abfangen

# Hauptmenü starten
main_menu()
