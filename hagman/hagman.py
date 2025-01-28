# Bibliothek für zufällige Wörter auswählen
import random

# Wähle ein zufälliges Wort aus der Liste
def get_random_word():
    words = ["python", "java", "meer", "fussball", "kotlin", "javascript", "haus", "arbeit"]
    return random.choice(words)

# Zeige den aktuellen Hangman-Status basierend auf verbleibenden Leben
def display_hangman(lives):
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """,
        """
           -----
               |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[lives]

# Das Hauptspiel
def play_hangman():
    word = get_random_word()                                                                                                            # Zufälliges Wort
    word_letters = set(word)                                                                                                            # Buchstaben des Wortes
    alphabet = set('abcdefghijklmnopqrstuvwxyz')                                                                                        # Alle möglichen Buchstaben
    used_letters = set()                                                                                                                # Bereits geratene Buchstaben
    lives = 7                                                                                                                           # Startanzahl der Leben

    while len(word_letters) > 0 and lives > 0:
        print(display_hangman(lives))                                                                                                   # Zeige aktuellen Hangman-Status
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        
        # Erzeuge die Liste mit dem aktuellen Fortschritt
        word_list = []
        for letter in word:
            if letter in used_letters:
                word_list.append(letter)
            else:
                word_list.append('-')

        print('Current word: ', ' '.join(word_list))

        # Benutzer gibt einen Buchstaben ein
        user_letter = input('Guess a letter: ').lower()

        if user_letter in alphabet - used_letters:                                                                                      # Der Buchstabe wurde noch nicht geraten
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)                                                                                        # Entferne den Buchstaben aus den noch zu ratenden Buchstaben
                
                # Prüfe auf mehrfach vorkommende Buchstaben (z. B. `ss`)
                if word.count(user_letter) > 1:
                    print(f"The letter '{user_letter}' appears multiple times. Guess it again for every occurrence.")
            else:
                lives -= 1                                                                                                              # Falscher Buchstabe, ein Leben weniger
                print('Letter is not in word.')
        elif user_letter in used_letters:
            print('You have already used that letter. Guess another letter.')
        else:
            print('Invalid character. Please enter a letter.')

    # Endzustand des Spiels
    if lives == 0:
        print(display_hangman(lives))
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')

# Hauptfunktion, die das Spiel wiederholt startet
def main():
    keep_playing = True                                                                                                                 # Kontrollvariable für die Schleife
    
    while keep_playing:                                                                                                                 # Solange der Spieler weiterspielen möchte
        play_hangman()                                                                                                                  # Das Spiel wird gestartet
        
        # Sicherstellen, dass nur 'y' oder 'n' akzeptiert werden
        valid_input = False                                                                                                             # Kontrollvariable für die Eingabe
        while not valid_input:                                                                                                          # Solange die Eingabe ungültig ist
            play_again = input('Do you want to play again? (y/n): ').lower()
            if play_again == 'y':                                                                                                       # Spieler will weiterspielen           
                valid_input = True                                                                                                      # Eingabe ist gültig
            elif play_again == 'n':                                                                                                     # Spieler will aufhören                      
                valid_input = True                                                                                                      # Eingabe ist gültig
                keep_playing = False                                                                                                    # Schleife beenden
                print("Thanks for playing! Goodbye!")
            else:
                print("Invalid input. Please enter 'y' to play again or 'n' to quit.")

# Starte das Spiel
if __name__ == '__main__':
    main() 
