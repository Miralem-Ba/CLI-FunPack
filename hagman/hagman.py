#Bibiothen für zufällige wörter auszuwählen
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
    word = get_random_word()                                                                                # Zufälliges Wort
    word_letters = set(word)                                                                                # Buchstaben des Wortes
    alphabet = set('abcdefghijklmnopqrstuvwxyz')                                                            # Alle möglichen Buchstaben
    used_letters = set()                                                                                    # Bereits geratene Buchstaben
    lives = 6                                                                                               # Startanzahl der Leben

    while len(word_letters) > 0 and lives > 0:
        print(display_hangman(lives))                                                                       # Zeige aktuellen Hangman-Status
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]                          
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()                                                     # Benutzer gibt einen Buchstaben ein ( .lower() ignoriert Groß- und Kleinschreibung)
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
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
    while True:
        play_hangman()
        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':                                                                           # hinzufügen von N als Abbruch / Gleicher Buchstabe mehrmals eingeben. /Aktueller Fortschritt  # for lop aufschreiben.
            print("Thanks for playing! Goodbye!")
            break

# Starte das Spiel
if __name__ == '__main__':
    main()
