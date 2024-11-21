import os
from collections import Counter

# Funksjon for å lese inn tekst fra en fil
def lesInnTekst(filnavn):
    try:
        with open(filnavn, 'r', encoding='utf-8') as fil:
            return fil.readlines()
    except FileNotFoundError:
        print(f"Feil: Fila '{filnavn}' ble ikke funnet.")
    except Exception as e:
        print(f"Uventet feil: {e}")
    return []

# Funksjon for å vise innholdet i filen
def printTekst(tekst):
    for linje in tekst:
        print(linje.strip())

# Funksjon for å søke etter et ord i teksten
def søkOrd(tekst, ord):
    funnet = False
    for linje in tekst:
        if ord.lower() in linje.lower():
            print(linje.strip())
            funnet = True
    if not funnet:
        print(f"Ordet '{ord}' ble ikke funnet.")

# Funksjon for å finne linje(r) der ordet finnes
def finnLinje(tekst, ord):
    for linjenummer, linje in enumerate(tekst, start=1):
        if ord.lower() in linje.lower():
            print(f"Ordet '{ord}' ble funnet på linje {linjenummer}: {linje.strip()}")

# Funksjon for å telle hvor mange ganger et ord opptrer i teksten
def tellOrd(tekst, ord):
    antall = sum(linje.lower().count(ord.lower()) for linje in tekst)
    print(f"Ordet '{ord}' forekommer {antall} ganger i teksten.")

# Funksjon for å søke etter flere ord samtidig
def søkFlereOrd(tekst, ordliste):
    for linjenummer, linje in enumerate(tekst, start=1):
        for ord in ordliste:
            if ord.lower() in linje.lower():
                print(f"Ordet '{ord}' funnet på linje {linjenummer}: {linje.strip()}")

# Funksjon for å vise meny og håndtere brukerens valg
def visMeny(tekst):
    while True:
        print("\nHva vil du gjøre?")
        print("1. Se innholdet i filen")
        print("2. Søk etter et ord")
        print("3. Finn linje med et ord")
        print("4. Tell hvor mange ganger et ord forekommer")
        print("5. Søk etter flere ord")
        print("6. Avslutt")

        valg = input("Velg et alternativ (1-6): ").strip()

        if valg == '1':
            printTekst(tekst)
        elif valg == '2':
            ord = input("Skriv inn ordet du vil søke etter: ")
            søkOrd(tekst, ord)
        elif valg == '3':
            ord = input("Skriv inn ordet du vil finne linje for: ")
            finnLinje(tekst, ord)
        elif valg == '4':
            ord = input("Skriv inn ordet du vil telle: ")
            tellOrd(tekst, ord)
        elif valg == '5':
            ordliste = input("Skriv inn ordene du vil søke etter (separert med komma): ").split(',')
            søkFlereOrd(tekst, [ord.strip() for ord in ordliste])
        elif valg == '6':
            print("Takk for at du brukte søkemotoren!")
            break
        else:
            print("Ugyldig valg, prøv igjen.")

# Hovedprogram
def hovedprogram():
    print("Velkommen til den enkle søkemotoren!")
    filnavn = input("Skriv inn navnet på tekstfila du vil åpne: ")
    tekst = lesInnTekst(filnavn)

    if not tekst:
        print("Ingen tekst å vise.")
        return

    # Vis menyen for brukeren og la dem velge handling
    visMeny(tekst)

# Kjøre hovedprogrammet
if __name__ == "__main__":
    hovedprogram()
