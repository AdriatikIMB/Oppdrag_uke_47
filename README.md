# Enkelt Søkeprogram i Python

Dette programmet gir en enkel søkemotor for å søke i tekstfiler. Brukeren kan utføre flere operasjoner på en tekstfil, som å søke etter et spesifikt ord, finne linjer som inneholder et ord, telle ordets forekomster, og søke etter flere ord samtidig.

## Funksjoner i programmet:

### 1. **lesInnTekst(filnavn)**
   - Leser inn tekstinnholdet fra en spesifisert fil.
   - Hvis filen ikke finnes, vises en feilmelding.

### 2. **printTekst(tekst)**
   - Skriver ut hele innholdet i teksten linje for linje.

### 3. **søkOrd(tekst, ord)**
   - Søker etter et spesifikt ord i teksten og viser alle linjer der ordet forekommer.
   - Søket er ikke skille mellom store og små bokstaver.

### 4. **finnLinje(tekst, ord)**
   - Søker etter et spesifikt ord i teksten og viser linjenummeret og innholdet i linjen hvor ordet finnes.

### 5. **tellOrd(tekst, ord)**
   - Teller hvor mange ganger et spesifikt ord forekommer i teksten.

### 6. **søkFlereOrd(tekst, ordliste)**
   - Søker etter flere ord samtidig i teksten og viser alle linjer hvor ett eller flere av ordene forekommer.

### 7. **finnHyppigsteOrd(tekst, antall=10)**
   - Finner og viser de mest brukte ordene i teksten, basert på en teller. Standardvis viser det de 10 mest brukte ordene.

### 8. **visMeny(tekst)**
   - Vist en meny som gir brukeren ulike valg for hvilke operasjoner som skal utføres på teksten. Den gir også valget om å avslutte programmet.

### 9. **hovedprogram()**
   - Hovedprogrammet som åpner tekstfilen og lar brukeren velge hvilke operasjoner som skal utføres.

## Hvordan programmet fungerer:

1. **Åpne fil:** Programmet starter ved å be om at brukeren skriver inn navnet på tekstfilen som skal brukes. Hvis filen eksisterer, leses innholdet inn, og programmet går videre til hovedmenyen.
2. **Valgmeny:** Når filen er åpnet, får brukeren en meny med ulike alternativer, som for eksempel:
   - Se innholdet i filen
   - Søk etter et ord
   - Finn linje med et ord
   - Tell hvor mange ganger et ord opptrer
   - Søk etter flere ord samtidig
3. **Interaktiv bruk:** Brukeren velger ett av alternativene og får spesifikke instrukser for hvordan de kan bruke programmet til å søke etter ord, finne linjer, eller telle ord.
4. **Avslutning:** Når brukeren er ferdig med å bruke programmet, kan de velge å avslutte.

