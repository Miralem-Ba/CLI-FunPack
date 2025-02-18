import random

def nearest_multiple_of_4(num):
    """Berechnet das nächste Vielfache von 4"""
    return num + (4 - num % 4) if num >= 4 else 4

