# Algoritmi/tekoäly projekti

Sovellus, jota voidaan opettaa tuottamaan yksinkertaista musiikkia.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/codePercidae/algo_projekti/blob/main/documentation/requirement_spesification.md)

## Viikkoraportit

- [Viikkoraportti 1](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkorapotti_1.md)

- [Viikkoraportti 2](https://github.com/codePercidae/algo_projekti/blob/main/documentation/Viikkorapotti_2.md)

## Asennus

1. Asenna riippuvuudet komennolla
```
poetry install
```

3. Käynnistä sovellus komennolla
```
poetry run invoke start
```

## Ohjelman toiminta
Sovellus kykenee luomaan tasaisesta kahdeksaosa-kulusta muodostuvia
melodioita. Kaikki melodiat ovat 2/4 tahtilajissa. Käyttäjä saa
päättää kuinka monen tahdin mittainen melodia on ja lisäksi minkä
asteen generaatioita käytetään (rajattu kuitenkin maksimissaan kuudenteen
asteeseen).

Käyttäjä saa kouluttaa mallia omalla opetusdatallaan, kuitenkin seuraavat asiat kannattaa
huomioida:
- Ohjelma lukee vain .txt muotoisia tiedostoja
- Nuottien on oltava abc-formaatissa
- Opetuskappaleiden kannattaa olla samassa sävellajissa, mikäli halutaan koherentteja tuloksia
- Mikäli datassa on virheitä, sovellus saattaa kaatua
- Datan tulee olla koottuna yhteen tiedostoon
