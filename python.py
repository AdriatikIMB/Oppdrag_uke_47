import os

# Funksjon for å lese inn tekst fra en fil
def lesInnTekst(filnavn):
    try:
        with open(filnavn, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Feil: Fila '{filnavn}' ble ikke funnet.")
        return []
    except Exception as e:
        print(f"Uventet feil ved lesing av fila: {e}")
        return []

# Funksjon for å vise innholdet i filen
def printTekst(tekst):
    for linje in tekst:
        print(linje.strip())  # Skriv ut innholdet uten ekstra linjeskift

# Funksjon for å søke etter et ord i teksten
def søkOrd(tekst, ord):
    funnet = False
    for linje in tekst:
        if ord.lower() in linje.lower():
            print(linje.strip())
            funnet = True
    if not funnet:
        print(f"Ordet '{ord}' ble ikke funnet.")

# Hovedprogram med meny
def hovedprogram():
    print("Velkommen til den enkle søkemotoren!")
    filnavn = input("Skriv inn navnet på tekstfila du vil åpne: ")
    tekst = lesInnTekst(filnavn)



# Kjøre hovedprogrammet
if __name__ == "__main__":
    hovedprogram()
