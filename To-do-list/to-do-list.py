# Eine leere Liste für die Aufgaben
todo_liste = []

while True:
    
    print("To-Do-Liste:")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgaben anzeigen")
    print("3. Aufgabe entfernen")
    print("4. Beenden")

    wahl = input("Wähle eine Option (1-4): ")

    if wahl == "1":
        aufgabe = input("Gib die neue Aufgabe ein: ")
        todo_liste.append(aufgabe)
        print(f"✅ '{aufgabe}' wurde hinzugefügt.")

    elif wahl == "2":
        print("Deine To-Do-List:")
        if not todo_liste:
            print("(Keine Aufgaben)")
        else:
            for index, aufgabe in enumerate(todo_liste, start=1):
                print(f"{index}. {aufgabe}")
                