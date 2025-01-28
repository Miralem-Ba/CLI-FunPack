import random
import os

# Dateien, um Highscore und Statistiken zu speichern
HIGHSCORE_FILE = "highscore.txt"
STATS_FILE = "stats.txt"

def load_highscore():
    """
    Funktion, um den Highscore aus der Datei zu laden.
    """
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return None
    return None

def save_highscore(highscore):
    """
    Funktion, um den Highscore in eine Datei zu speichern.
    """
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(highscore))

def load_stats():
    """
    Funktion, um die Statistiken aus der Datei zu laden.
    """
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r") as file:
            try:
                stats = file.read().split(",")
                total_games = int(stats[0])
                total_attempts = int(stats[1])
                return total_games, total_attempts
            except ValueError:
                return 0, 0
    return 0, 0

def save_stats(total_games, total_attempts):
    """
    Funktion, um die Statistiken in eine Datei zu speichern.
    """
    with open(STATS_FILE, "w") as file:
        file.write(f"{total_games},{total_attempts}")

def select_difficulty():
    """
    Funktion, um den Schwierigkeitsgrad auszuwählen.
    """
    print("Choose a level of difficulty:")
    print("1. Simple (Unlimited attempts)")
    print("2. Medium (10 Attempts)")
    print("3. Hard (5 Attempts)")
    
    while True:
        difficulty = input("Enter the difficulty level number (1/2/3): ")
        if difficulty == '1':
            return None  # Unbegrenzte Versuche
        elif difficulty == '2':
            return 10  # 10 Versuche
        elif difficulty == '3':
            return 5  # 5 Versuche
        else:
            print("❗ Invalid entry. Please select 1, 2, or 3.")

def get_valid_number(prompt, min_value, max_value):
    """
    Funktion, um eine gültige Zahl vom Benutzer zu erhalten.
    """
    while True:
        try:
            num = int(input(prompt))
            if min_value <= num <= max_value:
                return num
            else:
                print(f"❗ Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("❗ Invalid input. Please enter a whole number.")

def number_guessing_game():
    """
    Hauptspiel des Zahlraten-Spiels mit Schwierigkeitsgraden und Highscore-Tracking.
    """
    # Highscore und Statistiken laden
    highscore = load_highscore()
    total_games, total_attempts = load_stats()

    if highscore is not None:
        print(f"🏆 Current Highscore: {highscore} attempts")
    else:
        print("No highscore yet. Be the first to set one!")

    print("Welcome to the guessing game!")
    max_attempts = select_difficulty()  # Schwierigkeitsgrad wählen
    secret_number = random.randint(1, 100)  # Zufällige Zahl zwischen 1 und 100
    attempts = 0  # Zähle die Versuche des Spielers

    while True:
        # Wenn ein Schwierigkeitsgrad mit begrenzten Versuchen gewählt wurde
        if max_attempts is not None and attempts >= max_attempts:
            print(f"❌ You have reached the maximum number of {max_attempts} attempts. The correct number was {secret_number}.")
            break

        guess = get_valid_number("Guess a number between 1 and 100: ", 1, 100)  # Fehlertolerante Eingabe
        attempts += 1  # Zähle die Versuche

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"🎉 You guessed right! The number was {secret_number}. You used {attempts} attempts.")
            
            # Highscore aktualisieren
            if highscore is None or attempts < highscore:
                highscore = attempts
                save_highscore(highscore)
                print(f"🏆 New highscore! You set the record with {attempts} attempts.")
            else:
                print(f"The current highscore remains {highscore} attempts.")
            break

    # Statistiken aktualisieren
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
            number_guessing_game()  # Starte das Spiel neu
            break
        elif play_again == 'n':
            print("Thanks for playing! See you next time.")
            break
        else:
            print("❗ Invalid input. Please enter 'y' for yes or 'n' for no.")

# Spiel starten
number_guessing_game()
