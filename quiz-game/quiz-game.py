# Fragen und Antworten
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
    },
    {
        "frage": "Wer malte die Mona Lisa?",
        "antworten": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "korrekte_antwort": "Leonardo da Vinci"
    },
    {
        "frage": "Welcher Fluss fließt durch London?",
        "antworten": ["Rhein", "Themse", "Donau", "Elbe"],
        "korrekte_antwort": "Themse"
    },
    {
        "frage": "Welche ist die größte Wüste der Welt?",
        "antworten": ["Kalahari", "Sahara", "Gobi", "Antarktische Wüste"],
        "korrekte_antwort": "Antarktische Wüste"
    },
        {
        "frage": "Wie viele Nerven hat das menschliche Gehirn?",
        "antworten": ["10 Milliarden", "100 Milliarden", "1 Billion", "500 Milliarden"],
        "korrekte_antwort": "100 Milliarden"
    },
        {
        "frage": "Welche ist die größte Wüste der Welt?",
        "antworten": ["Kalahari", "Sahara", "Gobi", "Antarktische Wüste"],
        "korrekte_antwort": "Antarktische Wüste"
    },
    {
        "frage": "Wer erfand das Telefon?",
        "antworten": ["Nikola Tesla", "Alexander Graham Bell", "Thomas Edison", "Albert Einstein"],
        "korrekte_antwort": "Alexander Graham Bell"
    },
    {
        "frage": "Wie viele Zähne hat ein erwachsener Mensch normalerweise?",
        "antworten": ["28", "30", "32", "34"],
        "korrekte_antwort": "32"
    },
]


# Punktzahl
punktzahl = 0

# Willkommen
print("🎉 Willkommen zum Quiz-Spiel! Viel Spaß beim Beantworten der Fragen! 🎉\n")

# Fragen durchgehen
for frage in fragen:
    print(frage["frage"])
    for idx, antwort in enumerate(frage["antworten"], 1):
        print(f"{idx}. {antwort}")

    # Frage wiederholen, wenn die Eingabe ungültig ist
    while True:
        benutzer_antwort = input("Wähle die Nummer der richtigen Antwort: ")

        # Überprüfen, ob die Antwort gültig ist
        if benutzer_antwort.isdigit():
            benutzer_antwort_nummer = int(benutzer_antwort)

            # Sicherstellen, dass die Eingabe innerhalb des gültigen Bereichs liegt
            if 1 <= benutzer_antwort_nummer <= len(frage["antworten"]):
                # Überprüfen, ob die Antwort korrekt ist
                if frage["antworten"][benutzer_antwort_nummer - 1] == frage["korrekte_antwort"]:
                    print("✔️ Richtig!")
                    punktzahl += 1
                else:
                    print(f"❌ Falsch! Die richtige Antwort ist: {frage['korrekte_antwort']}")
                break  # Die Frage ist beantwortet, also brechen wir die Schleife ab
            else:
                print(f"❌ Ungültige Antwort! Bitte eine Nummer zwischen 1 und {len(frage['antworten'])} wählen.")
        else:
            print("❌ Ungültige Eingabe! Bitte eine Nummer zwischen 1 und 4 eingeben.")

# Am Ende die Punktzahl anzeigen
print(f"\n🎯 Deine Punktzahl: {punktzahl}/{len(fragen)}")