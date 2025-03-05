# Tekoälyprojekti

Sovellus, jota voidaan opettaa tuottamaan yksinkertaisia melodioita.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/codePercidae/algo_projekti/blob/main/documentation/requirement_spesification.md)

- [Toteutusdokumentti](https://github.com/codePercidae/algo_projekti/blob/main/documentation/completition_documentation.md)

- [Testausdokumentti](https://github.com/codePercidae/algo_projekti/blob/main/documentation/test_documentation.md)

## Viikkoraportit

- [Viikkoraportti 1](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkoraportti_1.md)

- [Viikkoraportti 2](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkoraportti_2.md)

- [Viikkoraportti 3](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkoraportti_3.md)

- [Viikkoraportti 4](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkoraportti_4.md)

- [Viikkoraportti 5](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkoraportti_5.md)

- [Viikkoraportti 6](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkoraportti_6.md)

## Asennus

Asennus vaatii [Poetryn](https://python-poetry.org/)

1. Asenna riippuvuudet komennolla
```
poetry install
```

2. Käynnistä sovellus komennolla
```
poetry run invoke start
```

## Muut komennot

Aja testit komennolla
```
poetry run invoke test
```

Testikattavuus komennolla
```
poetry run invoke coverage
```

Raportti testikattavuudesta
```
poetry run invoke raport
```

HTML muotoinen raportti testikattavuudesta
```
poetry run invoke visualRaport
```

Linttaus komennolla
```
poetry run invoke lint
```

## Ohjelman toiminta
Sovellus kykenee luomaan tasaisesta kahdeksaosa-kulusta muodostuvia
melodioita. Kaikki melodiat ovat 2/4 tahtilajissa. Käyttäjä saa
päättää kuinka monen tahdin mittainen melodia on, minkä
asteen generaatioita käytetään (rajattu kuitenkin maksimissaan kuudenteen
asteeseen) ja montako melodiaa generoidaan.

Käyttäjä saa kouluttaa mallia omalla opetusdatallaan, kuitenkin seuraavat asiat kannattaa
huomioida:
- Ohjelma lukee vain .txt muotoisia tiedostoja
- Nuottien on oltava abc-formaatissa
- Opetuskappaleiden kannattaa olla samassa sävellajissa, mikäli halutaan koherentteja tuloksia
- Sovellus ei ymmärrä kirkkosävellajeja, pitäydy siis doorisessa, tai aiolisessa asteikossa
- Mikäli datassa on virheitä, sovellus saattaa kaatua
- Datan tulee olla koottuna yhteen tiedostoon
- Dataa kannattaa olla paljon, muutoin generointi saattaa päätyä tilanteeseen, jossa uusia arvoja ei enää löydy
- Sovellus osaa hakea tiedoston nimellä suoraan, jos se on sijoitettu data-hakemistoon

Sovellus tuottaa tiedoston joka sisältää generoidut melodiat. Mikäli käyttäjä ei toisin määrittele,
tiedosto on aina music.txt niminen, ja ilmestyy data kansion sisälle.

Lisää abc-notaatiosta löytyy sivulta https://abcnotation.com/

Ja abc-notaatiolla tehtyjä kappaleita oman mallisi kouluttamista varten löytyy sivulta https://abcnotation.com/tunes

## Mahdollisia ongelmia

Mikäli kohtaat seuraavanlaisen virheilmoituksen:
```
File "/usr/lib/python3.10/random.py", line 533, in choices
    total = cum_weights[-1] + 0.0   # convert to float
IndexError: list index out of range
```
On generoinnin aikana tapahtunut kohtuullisen harvinainen tilanne, jossa sovellus ei löydä enää uusia mahdollisia arvoja generoitavaksi. Virhe on fataali, eikä sovellus toivu siitä. Kuitenkin käynnistämällä sovelluksen ja kokeilemalla samoja parametrejä uudestaan, pitäisi ongelman ratketa. 
