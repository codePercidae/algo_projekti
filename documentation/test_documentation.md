# Testausdokumentaatio

Ohjelman toiminnallisuuden oikeellisuus on varmistettu yksikkötesteillä ja integraatiotestauksella. 

## Yksikkötestit

Jokainen sovelluksen moduuli on saanut oman testitiedostonsa. Tähän poikkeuksena 
*interface.py* ja hakemiston *utils* sisältö, jotka ovat sovelluslogiikan ulkopuolisia toimintoja.

**Node**
Node-luokkaa testataan hyvin kevyesti, sillä toiminnallisuuttakaan ei juuri ole.

**Trie**
Trien testauksessa on keskiössä varmistaa, että Trieen lisätään oletetut asiat ja että sinne ei päädy odotamattomia arvoja. Tämä toteutetaan *__str__* funktion avulla: oletettu ulostulo on laskettu käsin, ja tätä verrataan funktion palauttamaan merkkijonoon, joka on käytännössä lista syvyyshaulla etsityistä solmuista. Toinen oleellinen ominaisuus on funktion *search* toiminta, tavoitteena on varmistaa, että funktio palauttaa oletetut arvot. Trie on siinä määrin yksinkertainen rakenteeltaan ja toiminnaltaan, että vaikeita syötteitä ei oikeastaan ole.

**Markovin ketju**
Markovin ketjun toimintaa testatessa pyritään varmistamaan, että generoitu materiaali on poikkeuksetta mukana annetussa opetusdatassa. Tämä toteutetaan vertaamalla jokaista ulostuloa alkuperäiseen dataan.

**Konvertteri**
Konvertterin testauksessa pääasiallinen kiinnostuksen kohde on, että konvertteri kääntää vain oleelliset asiat, ja että käännös itsessään on oletetun kaltainen. Rajallisen ajan ja harjoitustyön varsinaisen kohteen vuoksi luokan testaus ei ole ehkä aivan sitä mitä se voisi olla. Esimerkiksi kaikkien sävellajien oikeellinen toiminta tulisi testata ja konvertteria tulisi rasittaa mahdollisimman monimutkaisilla abc-tiedostoilla.