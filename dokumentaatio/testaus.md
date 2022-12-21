# Testausdokumentti

Sovellusta on testattu yksikkötesteillä unittestilla ja manuaalisesti tehdyin järjestelmätason testein.

## Yksikkötestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa CalService luokkaa testattiin TestCalculator-testiluokalla, jolla on alustuksen myötä käytössä kaikki CalService luokan metodit. 

### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 94%. 

![testauskuva](https://i.imgur.com/lAyhW6i.png)

Testien ulkopuolelle jäivät sovelluksen käynnistyksestä ja käyttöliittymästä vastaavat tiedostot. 

## Järjestelmätestaus

Sovelluksen järjelmätestaus suoritettiin manuaalisesti. 

### Asennus ja konfigurointi

Sovellus on haettu ja asennettu ohjeiden mukaisesti sekä testattu macOS- ja Linux-ympäristöissä (laitoksen Cubbli Linux virtuaalikone).

### Toiminnallisuudet

Testauksessa pyrittiin testaamaan jokainen metodi vähintään yhdellä tai useamalla eri tavalla. Testauksessa otettiin huomioon mahdolliset käyttäjän virhesyötteet ja pyrittiin varmistamaan, että sovellusta ei saada kaatumaan virhetilanteessa.

## Sovellukseen jääneet laatuongelmat

Sovellus ei tuota "Syntax error" virheilmoitusta muutamissa tilanteissa, kuten esimerkiksi kun yritetään ottaa neliöjuuri negatiivisesta luvusta. Tämä ei kuitenkaan vaikuta laskimen toimintaan. 