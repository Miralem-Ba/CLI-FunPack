import random

def chatbot():
    responses = {
        "hallo": "Hallo! Wie kann ich dir helfen?",
        "wie geht es dir": "Mir geht es gut, danke! Und dir?",
        "was ist dein name": "Ich bin ein einfacher Chatbot!",
        "tschüss": "Auf Wiedersehen! Bis zum nächsten Mal!",
        "default": "Das verstehe ich leider nicht. Kannst du es anders formulieren?"
    }
    
    print("Willkommen beim Chatbot! (Tippe 'tschüss' zum Beenden)")
    
    while True:
        user_input = input("Du: ").lower()
        
        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot:", responses["default"])
        
        if user_input == "tschüss":
            break

if __name__ == "__main__":
    chatbot()
