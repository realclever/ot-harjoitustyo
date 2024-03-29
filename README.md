# Ohjelmistotekniikka, harjoitustyö
## Laskin

Käyttäjä voi laskea yksinkertaisia laskutoimituksia sovelluksen avulla. Sovelluksesta löytyy kaikki nelilaskimen perustoiminnot. Sovellus on kehitetty ja testattu Python versiolla 3.10.7.

- [Final release](https://github.com/realclever/ot-harjoitustyo/releases/tag/final_release)

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/realclever/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/realclever/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/realclever/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/realclever/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md) 
- [Käyttöohje](https://github.com/realclever/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Testaus](https://github.com/realclever/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)

 

## Asennus

1. Asenna projektin riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

tai 

```bash
poetry run invoke coverage-report-html
```
(generoituu hakemistoon "htmlcov"):

### Pylint

Sovelluksen laatuvaatimukset voidaan tarkastaa komennolla:

```bash
poetry run invoke lint
```


