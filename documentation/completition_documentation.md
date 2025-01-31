# Toteutusdokumentti

Sovellus on jaettu viiteen osaan:
    1. tietorakenteet
    2. markovin ketju
    3. tiedostokonvertteri
    4. käyttöliittymä
    5. sekalaiset OS:n kanssa kommunikoivat elementit

## 1. tietorakenteet

### Node

Node on hyvin pitkälti klassista solmua vastaava luokka. Nodella on seuraavat ominaisuudet:
    - *frequency*: montako kertaa solmussa on vierailtu
    - *children*: sanakirja, johon talletetaan solmun lapset. Avain on lapsisolmun arvo ja varsinainen arvo itse lapsi

Kaikki Noden luokan funktiot ovat aikavaatimukseltaan luokkaa *O(1)*.

### Trie

Trie hyödyntää luokkaa Node solmujen muodostuksessa. Triellä on vain yksi ominaisuus:
    - *root*: juurisolmu, jonka kautta solmujen lisäys ja arvojen haku tapahtuu

Lyhyt selostus Trien funktioista:

**add_notes** lisää annetun joukon solmuja Trieen. Lisäys alkaa aina juurisolmusta. 
Funktio käy läpi listan values rekursiivisesti. Jokaisella rekursion asteella katsotaan, 
onko nykyisen solmun lapsisolmuissa seuraava listan arvo. Jos ei, lisätään arvo solmun lapsiin.
Tämän jälkeen funktio kutsuu itseään uudelleen ja käsittelee lapsisolmun, kunnes koko annettu lista
on käyty läpi. Funktion aikavaativuus on *O(n)*, missä n on listan values, pituus.
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
kyseisen listan pisin sisäkkäinen lista.

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

## 2. markovin ketju

Moduulilla markov, on seuraavat funktiot:
    - choose
    - generate

**choose**
*choose* saa argumentikseen listan tupleja ja palauttaa yhden tuplen ensimmäisen arvon. Valinta perustuu
jokaisen tuplen toisena arvona toimivaan painoon. AIKAVAATIVUUS EHKÄ O(N)?????


**generate**
*generate* saa argumentikseen generoinnin asteen kokonaislukuna, generoitavien listojen pituuden, 
trie-rakenteen, josta potentiaalisia arvoja haetaan ja palauttaa listan, jossa on 10 generoitua listaa. 

```
    generate(degree, length, trie):
        returnList = []
        FOR (i IN RANGE 10):
            generatedList = []
            FOR (j IN RANGE(4*length)):
                IF j < degree:
                    newValue = choose(trie.search(generatedList[0:j], degree))
                ELSE:
                    newValue = choose(trie.search(generatedList[j:j+degree], degree))
                generatedList.append(newValue)
            returnList.append(returnList)
        RETURN returnList
```
