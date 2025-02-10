# Das Tic Tac Toe Spielfeld
def drucke_brett(brett):
    for zeile in brett:
        print(" | ".join(zeile))
        print("-" * 5)  # Trennt die Zeilen durch Linien

# Start des Spiels
brett = [[" " for _ in range(3)] for _ in range(3)]
