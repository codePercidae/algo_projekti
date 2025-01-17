# Viikkoraportti 1

Aikaa käytetty: 5,5h

**Viikon aikana tehty**:
- taustatutkimusta (Markovin ketjut yms)
- Luotu projektille:
    - Tietorakenteiden rungot
    - Konversioalgoritmi
    - Alustava sovelluksen runko
- Riippuvuuksien hallinta poetryllä

Työ on edistynyt yllättävän nopeasti. Tietorakenteiden luominen oli varsin nopeasti valmista, vaikkakin
hienosäätöä täytyy vielä tehdä, eikä kaiken toimivuutta ole päästy vielä kunnolla testaamaan. Viikon
aikana olen paneutunut Markovin ketjujen toimintaan, trie-tietorakenteeseen ja abc-notaatioon, jolla
on mahdollista ilmaista nuotteja tekstitiedostossa.

Tällä hetkellä pohdituttaa, että miten koulutetun mallin saisi tallennettua. Eli jos käyttäjä on
kouluttanut mallia vaikka viidellä kappaleella, olisi mukavaa jos hänen ei tarvitsisi seuraavalla
käyttökerralla tehdä koko hommaa uudelleen. Trie siis varmaan pitäisi muuttaa johonkin talletettavaan
muotoon, mutten ole varma miten.

Seuraavaksi testailen, että toimiiko konversio-algoritmi halutusti. Sitten selvitetään että Trie-rakenne
toimii myös toivotusti, jonka jälkeen teen varsinaisen musiikkia generoivan osion.