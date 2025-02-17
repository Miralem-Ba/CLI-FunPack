import random

def generate_story():
    story_templates = [
        "Es war einmal ein mutiger {character}, der in einem {place} lebte. Eines Tages fand er/sie eine mysteriöse {object} und begann ein episches Abenteuer.",
        "In einem weit entfernten {place} entdeckte ein neugieriger {character} eine geheime {object}, die die Welt für immer verändern sollte.",
        "Der {character} wollte immer schon die Welt erkunden. Doch als er/sie eines Tages eine {object} fand, begann das größte Abenteuer seines/ihres Lebens!"
    ]
    
    characters = ["Ritter", "Magier", "Drachenreiter", "Erfinder", "Forscher"]
    places = ["verzauberten Wald", "versteckten Höhle", "futuristischen Stadt", "alten Schloss", "geheimen Labor"]
    objects = ["Schriftrolle", "Zauberstab", "Portal", "Schlüssel", "magische Karte"]
    
    story = random.choice(story_templates).format(
        character=random.choice(characters),
        place=random.choice(places),
        object=random.choice(objects)
    )
    
    return story

if __name__ == "__main__":
    print("Willkommen zum Story Generator! Hier ist deine Geschichte:")
    print(generate_story())
