import random

def select_difficulty():
    """
    function to select the difficulty level.
    """
    print("Choose a level of difficulty:")
    print("1. Simple (Unlimited attempts)")
    print("2. Medium (10 Attempts)")
    print("3. Hard (5 Attempts)")
    
    while True:
        difficulty = input("Enter the difficulty level number (1/2/3): ")
        if difficulty == '1':
            return None                                                                                                                 # Unbegrenzte Versuche
        elif difficulty == '2':
            return 10                                                                                                                   # 10 Versuche
        elif difficulty == '3':
            return 5                                                                                                                    # 5 Versuche
        else:
            print("Invalid entry. Please select 1, 2 or 3.")

def number_guessing_game():
    """
    Main game of the number guessing game with difficulty levels.
    """
    print("Welcome to the guessing game!")
    max_attempts = select_difficulty()                                                                                                  # Schwierigkeitsgrad wählen
    secret_number = random.randint(1, 100)                                                                                              # Zufällige Zahl zwischen 1 und 100
    attempts = 0                                                                                                                        # Versuche des Spielers

    while True:
        # Wenn ein Schwierigkeitsgrad mit begrenzten Versuchen gewählt wurde
        if max_attempts is not None and attempts >= max_attempts:
            print(f"You have reached the maximum number of {max_attempts}. The correct number was {secret_number}.")
            break
        
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1                                                                                                               # Zähle die Versuche
            
            if guess < secret_number:
                print("To low!")
            elif guess > secret_number:
                print("To high!")
            else:
                print(f"You guessed right! You used {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Nach dem Spiel fragen, ob der Benutzer noch einmal spielen möchte
    while True:
        play_again = input("Would you like to play again? (y = Ja, n = Nein): ").lower()
        if play_again == 'y':
            number_guessing_game()                                                                                                      # Starte das Spiel neu
            break
        elif play_again == 'n':
            print("Thanks for playing! See you next time.")
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

# Spiel starten
number_guessing_game()
