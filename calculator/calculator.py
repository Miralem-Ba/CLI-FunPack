# Define arithmetic functions
def add(a, b):
    return a + b

# Define a function to subtract two numbers
def subtract(a, b):
    return a - b

# Define a function to multiply two numbers
def multiply(a, b):
    return a * b

# Variant 1: Simple division
def divide_v1(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Variant 2: Division with remainder
def divide_v2(a, b):
    if b == 0:
        return "Error! Division by zero."
    return f"Quotient: {a // b}, Remainder: {a % b}"

# Variant 3: Return a tuple with quotient and remainder
def divide_v3(a, b):
    if b == 0:
        return "Error! Division by zero."
    return (a / b, a % b)

# Calculator function
def calculator():
    while True:                                                                             #Kann immer zwischen Optionen Wählen, Menü wird endlos angezeigt.
        print("Select operation:")
        print("1 add")
        print("2 subtract")
        print("3 multiply")
        print("4 divide")
        print("5 exit")

        choice = input("Enter choice (1/2/3/4/e): ").strip()                                #.strip = entfernt Leerzeichen um fehler zu miniminieren.

        if choice == 'e':                                                                   #Programm beendet.
            print(" Goodbye see u next time!")
            break                                                                           #Beendet die While True Schleife.

        elif choice in ['1', '2', '3', '4']:
            try:                                                                            #Fehlerbehandlung und Fehlermeldung bei falscher Eingabe.
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")

                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")

                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")

                elif choice == '4':
                    print("Choose a division variant:")
                    print("1 Simple Division")
                    print("2 Division with Quotient and Remainder")
                    print("3 Return Quotient and Remainder as Tuple")
                    variant_choice = input("Enter variant choice (1/2/3): ").strip()

                    if variant_choice == '1':
                        print(f"{num1} / {num2} = {divide_v1(num1, num2)}")

                    elif variant_choice == '2':
                        print(f"{num1} divided by {num2} gives {divide_v2(num1, num2)}")

                    elif variant_choice == '3':
                        quotient, remainder = divide_v3(num1, num2)
                        print(f"Quotient: {quotient}, Remainder: {remainder}")

                    else:
                        print("Invalid variant choice.")

            except ValueError:
                print("Invalid input! Please enter numeric values.")                        #Fehlermeldung bei falscher Eingabe, wenn der Benutzer keine Zahl eingibt.

        else:
            print("Invalid choice! Please select a valid option.")

# Run the calculator
if __name__ == "__main__":
    calculator()
