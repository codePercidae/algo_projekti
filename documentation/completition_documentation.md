# Toteutusdokumentti

Sovellus on jaettu viiteen osaan:

    1. tietorakenteet
    2. markovin ketju
    3. tiedostokonvertteri
    4. käyttöliittymä
    5. sekalaiset OS:n kanssa kommunikoivat elementit

Tässä dokumentissä esitetään ensiksi jokaisen osan toiminnallisuus erikseen ja lopuksi 
käydään läpi end-to-end -tyylinen toimintaselostus ja aikavaativuuksien esitys. 

Kaikki pseudokoodi esitykset eivät välttämättä vastaa ulkoasultaan sitä, mitä koodissa lopulta on.
Tavoite on esittää mahdollisimman selkeästi ohjelman toimintaa ja jättää *siistit temput* varsinaisen koodin puolelle.

Laajoja kielimalleja (ChatGPT, DeepSeek, yms.) ei ole sovelluksen toteutuksessa käytetty millään tavalla.

## 1. tietorakenteet

### Node

Node on hyvin pitkälti klassista solmua vastaava luokka. Nodella on seuraavat ominaisuudet:

    - *frequency*: montako kertaa solmussa on vierailtu
    - *children*: sanakirja, johon talletetaan solmun lapset. Avain on lapsisolmun arvo ja varsinainen arvo itse lapsi

### Trie

Trie hyödyntää luokkaa Node solmujen muodostuksessa. Triellä on vain yksi ominaisuus:

    - *root*: juurisolmu, jonka kautta solmujen lisäys ja arvojen haku tapahtuu

Lyhyt selostus Trien funktioista:

**add_notes** lisää annetun joukon solmuja Trieen. Lisäys alkaa aina juurisolmusta. 
Funktio käy läpi listan values rekursiivisesti. Jokaisella rekursion kerroksella katsotaan, 
onko nykyisen solmun lapsisolmuissa seuraava listan arvo. Jos ei, lisätään arvo solmun lapsiin.
Tämän jälkeen funktio kutsuu itseään uudelleen ja käsittelee lapsisolmun, kunnes koko annettu lista
on käyty läpi. Funktion aikavaativuus on *O(n)*, missä *n* on listan `values`, pituus.
```
    add_notes(current, values, depth)
        current.visit()
        IF depth >= values.length
             return
        IF values[depth] NOT IN current.children
            current.add_child(values[depth])
        RETURN add_notes(current.children[values[depth]], values, depth+1)
```

**train** kutsuu *add_notes* funktiota kaikille saamilleen listoille. Näin ollen
sen aikavaativuus on *O(mn)* missä *m* on *train* funktion saaman listan pituus ja *n* 
kyseisen listan pisimmän sisäkkäisen listan pituus.

**search** etsii mahdollisia seuraavia arvoja annetulle joukolle. Funktio tutkii onko nykyisellä solmulla 
sopivaa seuraajaa lastensa joukossa, jos on, kutsutaan funktiota uudelleen lapselle. Mikäli on päästy 
argumentin *degree* osoittamaan syvyyteen, palautetaan nykyisen solmun lapset listassa, joka sisältää
jokaisen lapsisolmun arvon ja frekvenssin talletettuna tuplena. *search* -funktion aikavaativuus on 
*O(n+m)*, jossa *n* on listan values pituus ja *m* viimeisen solmun lapsien lukumäärä.
```
    search(current, values, degree, depth)
        possibleValues = []

        IF depth == degree OR depth >= values.length
            FOR (node, child IN current.children):
                tupleToReturn = (node, child.frequency)
                possibleValues.append(tupleToReturn)

        ELSE IF values[depth] IN current.children:
            valuesToAdd = search(current.children[values[depth]], degree, depth+1)
            possibleValues.concat(valuesToAdd)

        RETURN possibleValues
```

## 2. Markovin ketju

Moduuli markov on tarkoitettu Markovin ketjuun pohjautuvaan tilageneraatioon. Moduuli sisältää seuraavat 
funktiot:

    - choose
    - generate

**choose** saa argumentikseen listan tupleja ja palauttaa yhden tuplen ensimmäisen arvon. Valinta perustuu
jokaisen tuplen toisena arvona toimivaan painoon.


**generate** saa argumentikseen generoinnin asteen kokonaislukuna, generoitavien listojen pituuden, 
trie-rakenteen, josta potentiaalisia arvoja haetaan ja palauttaa listan, jossa on 10 generoitua listaa.
Funktio hyödyntää yllä mainittua *choose* -funktiota uusien arvojen valinnassa. Huomion arvoista on, että 
generoitavan listan ensimmäiset *k* elementtiä, jossa *k < degree*, generoidaan *k* -asteen mukaisesti. 
Funktion aikavaativuus on *O(n²O(nm))*, jossa *n=length* ja *O(nm)* vastaa *trien* funktion *search* 
aikavaatimusta. Tämä voidaan kirjoittaa sievemmin muotoon *O(mn²)* 
```
    generate(degree, length, trie):
        returnList = []

        FOR (i=0 TO 10):
            generatedList = []
            FOR (j=0 TO (4*length)):
            sublist = []

                IF j < degree:
                    FOR (k=0 to j):
                        sublist.append(generatedList[k])
                    newValue = choose(trie.search(sublist, k))
                ELSE:
                    FOR (k=j to j+degree):
                        sublist.append(generatedList[k])
                    newValue = choose(trie.search(sublist, degree))

                generatedList.append(newValue)
            returnList.append(returnList)
        RETURN returnList
```

## Tiedostokonvertteri

Tiedostokonvertteri pitää sisällään funktiot abc-muotoisen tekstitiedoston kääntämisen 
kokonaislukulistoiksi ja toisinpäin. Luokalla on seuraavat ominaisuudet:

    - *notes_to_numbers*: sanakirja, jossa avaimina nuotin nimet kirjaimina, ja arvoina niiden kokonaisluku esitys
    - *numbers_to_notes*: sama kuin yllä, mutta käänteisenä
    - *keys*: sanakirja, jossa avaimina sävellajien lyhenteet ja arvoina niiden kokonaisluku esitys
    - *key*: nykyisen sävellajin kokonaislukuesitys

Kuvaus luokan funktioiden toiminnasta.

**reset** palauttaa ominaisuuden *notes_to_numbers* arvot takaisin alkuperäiseksi. Aikavaatimus on valkioaikainen.

**apply_key** saa argumentikseen sävellajin lyhenteen ja muuttaa ominaisuuden *notes_to_numbers* arvon vastaamaan sävellajia. Aikavaatimus vakioaikainen.

**parse_row** saa argumentikseen yhden tiedoston rivin, ja muuntaa sen listaksi kokonaislukuja. Aikavaatimus on *O(n)*, jossa *n* on rivin pituus.

**convert** saa argumentikseen listan, joka sisältää tiedoston jokaisen rivin omana merkkijononaan. Funktio etsii sitten riviä, joka halutaan kääntää ja löytäessään sellaisen, välittää rivin funktiolle 
*parse_row*. Aikavaatimus on *(Omn)*, jossa *m* on tiedoston rivien määrä ja *n* pisimmän käännettävän rivin pituus.

**reverse_convert** saa argumentikseen listan kokonaislukuja, ja kääntää sen abc-notaatioksi. Aikavaatimus on *O(n)*, jossa *n* on annetun listan pituus.

**chunk** saa argumentikseen listan kokonaislukuja, jotka se pilkkoo annetun kokoisiksi osalistoiksi. Funktion aikavaatimus on teoriassa *O(n²)*, mutta käytännössa osalistojen koko on rajattu maksimissaan kuuteen, joten aikavaatimus yksinkertaistuu lineaariseksi *O(n)*, jossa *n* on annetun listan pituus.
<<<<<<< HEAD

## Käyttöliittymä

Käyttöliittymä sitoo ohjelman eri osat toisiinsa ja välittää tietoa niiden välillä. 
=======
>>>>>>> ed62b0c5a6a7623ea1839f4751169b30fa5e6cee
