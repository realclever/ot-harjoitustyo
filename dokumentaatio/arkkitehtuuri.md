# Arkkitehtuurikuvaus

## Rakenne

Sovelluksen rakenne noudattelee kaksitasoista arkkitehtuuria seuraavassa muodossa:

![alt text](https://i.imgur.com/zp4wxDF.png)

Pakkaus UI huolehtii osittain käyttöliittymän komponenteista (näppäimet) ja niiden muodostamisesta sekä services pakkaus sisältää sovelluksen logiikan.

## Käyttöliittymä

Käyttöliittymä on laskimen tapaan yksinkertainen, ja sisältää ainoastaan yhden näkymän - itse laskimen. Käyttöliittymä on eristetty osittain sovelluslogiikasta. 
Käyttöliittymä pakkaus sisältää näppäimien luonti ja käyttöliittymän renderöinti metodit. 

![laskinkuva](https://i.imgur.com/08hSj2J.png)
Käyttöliittymä ja käynnistysnäkymä. 

## Tietojen pysyväistallennus

Sovellus ei tallenna laskutoimituksia tai niiden tuloksia. Tämä voisi tosin toimia jatkokehitys ideana yleisellä tasolla. 


## Sovelluslogiikka

## Päätoiminnallisuudet
Kuvataan sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Yksinkertainen laskutoimitus

Kun laskin käynnistetään ja halutaan suorittaa esimerkiksi yksinkertainen 2 + 2 = 4 laskutoimitus, etenee sovellus seuraavasti:

### Virheellinen laskutoimitus

Jos käyttäjä yrittää suorittaa laskimella esimerkiksi klassisen nollalla jako laskutoimituksen, etenee sovellus seuraavasti:


### Muut toiminnallisuudet

## Ohjelman rakenteeseen jääneet heikkoudet

Käyttöliittymän ja sovellusloogikan eristäminen toisistaan jäi vain puolittaiselle tasolle. Myös laajentamisen näkökulmasta näppäimet ja niiden logiikan olisi voinut eristää omaksi tiedostoksi. Koodi sisältää toisteisuutta varsinkin näppäimien luonnin osalta. 