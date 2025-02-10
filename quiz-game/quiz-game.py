fragen = [
    {
        "frage": "Was ist die Hauptstadt von Deutschland?",
        "antworten": ["Berlin", "München", "Hamburg", "Köln"],
        "korrekte_antwort": "Berlin"
    },
    {
        "frage": "Wie viele Kontinente gibt es auf der Erde?",
        "antworten": ["6", "7", "8", "9"],
        "korrekte_antwort": "7"
    },
    {
        "frage": "Welches ist das größte Land der Welt?",
        "antworten": ["USA", "China", "Russland", "Kanada"],
        "korrekte_antwort": "Russland"
    },
    {
        "frage": "In welchem Jahr landeten die ersten Menschen auf dem Mond?",
        "antworten": ["1967", "1969", "1971", "1973"],
        "korrekte_antwort": "1969"
    },
    {
        "frage": "Wie viele Planeten gibt es in unserem Sonnensystem?",
        "antworten": ["7", "8", "9", "10"],
        "korrekte_antwort": "8"
    },
    {
        "frage": "Welcher Planet ist der größte in unserem Sonnensystem?",
        "antworten": ["Merkur", "Venus", "Erde", "Jupiter"],
        "korrekte_antwort": "Jupiter"
    },
    {
        "frage": "Wie viele Knochen hat ein erwachsener Mensch?",
        "antworten": ["206", "207", "208", "209"],
        "korrekte_antwort": "206"
    },
    {
        "frage": "Wie viele Sekunden hat ein Tag?",
        "antworten": ["86400", "86500", "86600", "86700"],
        "korrekte_antwort": "86400"
    }
]

# Punktzahl
punktzahl = 0

# Fragen durchgehen
for frage in fragen:
    print(frage["frage"])
    for idx, antwort in enumerate(frage["antworten"], 1):
        print(f"{idx}. {antwort}")

    # Benutzerantwort eingeben
    benutzer_antwort = input("Wähle die Nummer der richtigen Antwort: ")

    # Überprüfen, ob die Antwort korrekt ist
    if frage["antworten"][int(benutzer_antwort) - 1] == frage["korrekte_antwort"]:
        print("✔️ Richtig!")
        punktzahl += 1
    else:
        print(f"❌ Falsch! Die richtige Antwort ist: {frage['korrekte_antwort']}")

# Am Ende die Punktzahl anzeigen
print(f"Deine Punktzahl: {punktzahl}/{len(fragen)}")
