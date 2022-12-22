# Käyttöohje

## Asennus

I. Lataa uusin [release](https://github.com/realclever/ot-harjoitustyo/releases/) tai kloonaa projekti. 

II. Varmista, että koneellasi on asenettuna Python 3.8^ ja 1.2.2^ 

III. Asenna projektin riippuvuudet komennolla:

       poetry install

IV. Käynnistä sovellus komennolla:

       poetry run invoke start

## Järjestelmävaatimukset, konfigurointi ja käyttöjärjestelmien väliset erot 

Sovelluksella ei käytön näkökulmasta ole järjestelmävaatimuksia, eikä se vaadi erillistä konfigurointia. Käyttöjärjestelmällä on väliä, koska macOS ei tue tkinterin painikkeiden värin vaihtamista. 
Sovellus on testattu macOS versiolla 13.0.1 Python versio (3.10.7), ja virtuaalityöaseman Linuxilla. Visuaalisesti paras käyttäjäkokemus saavutetaan Windows tai Linux käyttöjärjestelmillä. 

## Laskin

Sovellus käynnistyy laskimen näkymään.

![laskinkuva](https://i.imgur.com/7S0fDAK.png)

Laskin toimii samalla periaatteella kuten esimerkiksi Googlen oma websovellus, laskinta tulee käyttää hiirellä ja se ei tue näppäinkomentoja. Laskin sisältää perus nelilaskimen toiminnot sekä muutaman lisätoiminnon. 


