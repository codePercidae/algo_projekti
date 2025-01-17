#Vaatimusmäärittely
opinto-ohjelma: tietojenkäsittelytieteen kandi+maisteri -ohjelma
Käytetty kieli: python
Muut osatut kielet:
  - Haskell (sujuva)
  - Java (jossain määrin)

##Sovelluksen tarkoitus
Sovellusta voi kouluttaa abc-notaatiota sisältävillä tekstitiedostoilla. Kätetyn data pohjalta sovellus pystyy
käyttäjän pyynnöstä generoimaan itse uutta musiikkia, joka palautetaan abc-notaationa.

##Toiminnallisuus
- Käyttäjä pystyy antamaan sovellukselle .txt -mutoisia tiedostoja
- Sovellus oppii saatujen tiedostojen pohjalta
- Sovellus pystyy luomaan uutta musiikkia
- Sovellus palauttaa luomansa musiikin abc-notaationa .txt -tiedostona
- Sovellus luo vain tasaista kahdeksasosa-kulkua, rytmi on siis muuttumaton.

##Mahdollisia lisäominaisuuksia
- Käyttäjä voi kouluttaa usean eri mallin ja valita mitä niistä käyttää musiikin luomiseen
- Käyttäjä voi valita miten entropista ulostulo on (Markovin ketjun asteen valinta)
- Sovellus pystyy varioimaan myös aika-arvoja
