# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne noudattelee kaksitasoista arkkitehtuuria seuraavassa muodossa:

![ark](https://i.imgur.com/c00F3td.png)

Pakkaus UI huolehtii osittain käyttöliittymän komponenteista (näppäimet) ja niiden muodostamisesta sekä services pakkaus sisältää sovelluksen logiikan.

## Käyttöliittymä

Käyttöliittymä on laskimen tapaan yksinkertainen, ja sisältää yhden näkymän. Käyttöliittymä on eristetty osittain sovelluslogiikasta. 
Käyttöliittymä pakkaus sisältää näppäimien luonti ja käyttöliittymän renderöinti metodit. 

![laskinkuva](https://i.imgur.com/7S0fDAK.png)

Käyttöliittymä ja käynnistysnäkymä. 

## Tietojen pysyväistallennus

Sovellus ei tallenna laskutoimituksia tai niiden tuloksia. Tämä voisi tosin toimia jatkokehitys ideana yleisellä tasolla. 

## Sovelluslogiikka

Sovelluslogiikka koostuu luokasta CalService, joka sisältää näppäimien matemaattisen loogikan ja komponenttien toteutuksen. Jokainen matemaattinen toiminto on toteutettu omana metodinaan ja ne toimivat toistensa kanssa vuorovaikutuksessa. Esimerkiksi ulkonäkökomponenttien toteutuksesta vastaavat metodit:

- `buttons_space()`
- `screen_space()`
- `screen_line()`
- `secondary_screen_line()`

Loput metodit koostuvat näppäimien luonnista, logiikasta ja arvojen päivittämisestä. 

![alt text](https://i.imgur.com/rgIGrAA.png)

## Päätoiminnallisuudet

Kuvataan sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Yksinkertainen laskutoimitus

Kun laskin käynnistetään ja halutaan suorittaa esimerkiksi 2 + 2 = 4 laskutoimitus, etenee sovellus seuraavasti:

![laskinkuva](https://i.imgur.com/cuAthTl.png)

![laskinkuva](https://i.imgur.com/yfWdkjA.png)

Käyttäjän painaessa painiketta 2, kutsutaan CalService luokan metodia `setTotal`, tämän jälkeen käyttäjä painaa "+" painiketta, joka kutsuu metodia `press`. Tämän jälkeen ensimmäinen sykli toistuu, jonka jälkeen käyttäjä painaa viimein painiketta "=", joka kutsuu metodia `equals_btn_func`. Tämän jälkeen `update_values` ja `update_second_values` metodit päivittävät lopullisen laskutoimituksen ja tuloksen riveille. Jokaisen metodin kutsumisen yhteydessä myös päivitetään laskimen rivit kyseiseillä metodeilla.  

### Virheellinen laskutoimitus

Jos käyttäjä yrittää suorittaa laskimella esimerkiksi klassisen nollalla jako laskutoimituksen, etenee sovellus seuraavasti:

![laskinkuva](https://i.imgur.com/6YGZkIR.png)

![laskinkuva](https://i.imgur.com/buxFCuo.png)

Kaava on edellisen kohdan tapaan samanlainen, mutta nollalla jako heittää tässä tilanteessa poikkeuksen, joka tyhjentää laskimen apurivin ja asettaa päärivin arvoksi "Syntax error"  

### Muut toiminnallisuudet

Logiikaltaan sovellus on esiteltyjen esimerkki mukainen, käyttäjä syöttää laskutoimituksia jotka päättyvät joko haluttuun tulokseen tai mahdollisesti virheelliseen laskutoimitukseen.

## Ohjelman rakenteeseen jääneet heikkoudet

Käyttöliittymän ja sovellusloogikan eristäminen toisistaan jäi vain puolittaiselle tasolle. Myös laajentamisen näkökulmasta näppäimet ja niiden logiikan olisi voinut eristää omaksi tiedostoksi. Koodi sisältää toisteisuutta varsinkin näppäimien luonnin osalta. 