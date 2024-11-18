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

# Hovedprogram
def hovedprogram():
    print("Velkommen til den enkle søkemotoren!")
    filnavn = input("Skriv inn navnet på tekstfila du vil åpne: ")
    tekst = lesInnTekst(filnavn)
        
    if tekst:
        print("\nInnholdet i filen er:")
        for linje in tekst:
            print(linje.strip())  # Skriv ut innholdet uten ekstra linjeskift
    else:
        print("Ingen tekst å vise.")

# Kjøre hovedprogrammet
if __name__ == "__main__":
    hovedprogram()


    

