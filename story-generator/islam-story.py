import random

def generate_story():
    story_templates = [
        "Es war einmal ein frommer {character}, der in {place} lebte. Eines Tages fand er eine alte {object}, die eine geheime Botschaft enthielt und ihn auf eine Reise des Glaubens führte.",
        "In {place} lebte ein/e {character}, der/die nach Wissen suchte. Eines Tages entdeckte er eine {object}, die ihn auf eine spirituelle Reise der Erkenntnis führte.",
        "Der {character} hatte stets den Wunsch, Gutes in der Welt zu verbreiten. Als er eine geheimnisvolle {object} fand, begann eine Reise voller Herausforderungen und Segnungen von Allah."
    ]
    
    characters = ["Gelehrter", "Reisender", "Kalif", "Waisenjunge", "Händler", "Imam"]
    places = ["der heiligen Stadt Mekka", "einer friedlichen Oase", "einer alten Moschee", "dem Marktplatz von Bagdad", "einem Dorf in Andalusien"]
    objects = ["verlorene Schriftrolle", "alte Koran-Seite", "verzauberter Kompass", "goldene Laterne", "mysteriöses Manuskript"]
    
    story = random.choice(story_templates).format(
        character=random.choice(characters),
        place=random.choice(places),
        object=random.choice(objects)
    )
    
    return story

if __name__ == "__main__":
    print("Willkommen zum Islamischen Story Generator! Hier ist deine Geschichte:")
    print(generate_story())
