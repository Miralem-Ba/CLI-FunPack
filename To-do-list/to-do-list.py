# Eine leere Liste für die Aufgaben
todo_liste = []

# Eine Schleife, die das Programm am Laufen hält
while True:
    
    # Menü anzeigen
    print("To-Do-Liste:")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe entfernen")
    print("4. Beenden")

    wahl = input("Wähle eine Option (1-4): ")

    # Optionen verarbeiten
    if wahl == "1":
        aufgabe = input("Gib die neue Aufgabe ein: ")
        todo_liste.append(aufgabe)
        print(f"✅ '{aufgabe}' wurde hinzugefügt.")

    # Aufgaben anzeigen
    elif wahl == "2":
        print("Deine To-Do-List:")
        if not todo_liste:
            print("(Keine Aufgaben)")
        else:
            for index, aufgabe in enumerate(todo_liste, start=1):
                print(f"{index}. {aufgabe}")

    # Aufgabe entfernen   
    elif wahl == "3":
        print("Deine To-Do-List:")
        for index, aufgabe in enumerate(todo_liste, start=1):
            print(f"{index}. {aufgabe}")

            nummer = int(input("Welche Aufgabe möchtest du entfernen? (Nummer eingeben): ")) -1
            if 0 <= nummer < len(todo_liste):
                entferne_aufgabe = todo_liste.pop(nummer)
                print(f"❌ '{entferne_aufgabe}' wurde entfernt.")
            else:
                print("Ungültige Nummer.")
    
    # Programm beenden
    elif wahl == "4":
        print("👋 Programm beendet. Bis bald!")
        break

    # Ungültige Eingabe
    else:
        print("❌ Ungültige Eingabe. Bitte wähle 1-4.")
