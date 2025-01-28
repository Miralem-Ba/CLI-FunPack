# Funktion

#Subtrahiere zwei Zahlen
def subtrahiere_zahlen(a, b):
    return a - b


#Berechne das Quadrat einer Zahl
ergebnis = subtrahiere_zahlen(10, 4)
print(ergebnis)  # Ausgabe: 6

def quadrat_zahl(a):
    return a ** 2

ergebnis = quadrat_zahl(7) 
print(ergebnis)  # Ausgabe: 49



# Prüfe, ob eine Zahl gerade ist
def ist_gerade(zahl):
    return zahl % 2 == 0

ergebnis = ist_gerade(8)
print(ergebnis)  # Ausgabe: True


#Berechne die Summe einer Liste
def summe_liste(listee):
    return sum(listee)

ergebnis = summe_liste([1, 2, 3, 4, 5])
print (ergebnis)  # Ausgabe: 15


#Zähle die Vokale in einem String
def zaehle_vokal(text):
    vokale = "aeiou"
    return sum(1 for char in text if char in vokale)

ergebnis = zaehle_vokal("Hallo Welt")
print(ergebnis)  # Ausgabe: 3



#Multipliziere zwei Zahlen
def zahlen_multiplizieren(a, b):
    return a * b

ergebnis = zahlen_multiplizieren(6, 7)
print(ergebnis) 


#Berechne die Länge eines Strings
def laenge_string(text):
    return len(text)

ergebnis = laenge_string("Programmieren")
print(ergebnis)

#Verdopple eine Zahl
def verdopple_zahl(zahl):
    return zahl * 2

ergebnis = verdopple_zahl(15)
print(ergebnis)


#Überprüfe, ob eine Zahl positiv oder negativ ist
def ist_positiv(zahl):
    return zahl >0

ergebnis = ist_positiv(-3)
print(ergebnis)


#Finde das größte Element in einer Liste
def groesstes_element(liste):
    return max(liste)

ergebnis = groesstes_element([3, 9, 2, 15, 7])
print(ergebnis)


#Umkehre einen String
def umkehre_string(text):
    return text [::-1]

ergebnis = umkehre_string("Python")
print(ergebnis)


#Berechne den Durchschnitt einer Liste von Zahlen
def durchschnitt_liste(liste):
    return sum(liste)/len(liste)

ergebnis = durchschnitt_liste([10, 20, 30, 40])
print(ergebnis)


#Überprüfe, ob eine Zahl ein Teiler von 100 ist
def zahl_ueberpruefen(zahl):
    return 100 % zahl == 0

ergebnis = zahl_ueberpruefen(25)
print(ergebnis)

#Zähle die Anzahl der Großbuchstaben in einem String
def zahlen_grossbuchstaben(text):
    return sum(1 for char in text if char.isupper())

ergebnis = zahlen_grossbuchstaben("HaLLo WoRLd")
print (ergebnis)


# Fakultät mit Rekursion berechnen
def berechne_fakultaet_rekursiv(n):
    if n == 0 or n == 1:                                                # Fakultät von 0 oder 1 ist immer 1
        return 1
    else:
        return n * berechne_fakultaet_rekursiv(n - 1)

# Funktion mit der Zahl 5 aufrufen und Ergebnis ausgeben
ergebnis = berechne_fakultaet_rekursiv(5)
print(ergebnis)                                                         # Erwartete Ausgabe: 120

#Erklärung: Fakultät

#    Was ist die Fakultät? 
#    Die Fakultät einer Zahl n ist das Produkt aller positiven ganzen Zahlen von 11 bis n. Zum Beispiel:
#    5!=5×4×3×2×1=120

#    Wie funktioniert der Code?
#        Die Funktion berechne_fakultaet(n) verwendet eine Schleife (for), die von 1 bis n läuft.
#        In jedem Schleifendurchlauf wird die aktuelle Zahl i mit der bisherigen Fakultät multipliziert.

#    Wie kannst du es testen?
#        Speichere den Code in deiner Datei test.py.
#        Führe das Programm aus, und überprüfe, ob die Ausgabe 120 ist.




#Create a list and find the smallest element
def smallest_element(liste):
    return min(liste)

ergebnis = smallest_element([9, 4, 2, 15, 49])
print(ergebnis)


#Create an empty list
def empty_list():
    return[]

ergebnis = empty_list()
print(ergebnis)


#Add an element to the list
def add_element(liste, element):
    liste.append(element)
    return liste

ergebnis = add_element([1, 2, 3], 4)
print(ergebnis)


#Access an element in the list
def access_element(liste):
    return liste

ergebnis = access_element([10, 20, 30 ,40])
print(ergebnis)


#Replace an element in the list
def replace_element(liste):
    liste[2] = 9
    return liste

ergebnis = replace_element([1, 2, 3, 4])
print(ergebnis)

