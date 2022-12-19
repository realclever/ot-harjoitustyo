# Arkkitehtuurikuvaus

Arkkitehtuurikuvausta päivitetään vielä ennen lopullista palautusta. 

## Rakenne

Sovelluksen rakenne noudattelee kaksitasoista arkkitehtuuria seuraavassa muodossa:

![alt text](https://i.imgur.com/zp4wxDF.png)

Pakkaus UI huolehtii käyttöliittymän komponenteista ja niiden muodostamisesta sekä services sisältää sovelluksen logiikan.

## Käyttöliittymä

Käyttöliittymä on laskimen tapaan yksinkertainen, ja sisältää ainoastaan yhden näkymän - itse laskimen. 

![laskinkuva](https://i.imgur.com/xGDbk4e.png)

## Sovelluslogiikka

## Päätoiminnallisuudet
Kuvataan sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Yksinkertainen laskutoimitus

Kun laskin käynnistetään ja halutaan suorittaa yksinkertainen 2 + 2 = 4 laskutoimitus, etenee sovellus seuraavasti:

![alt text](https://i.imgur.com/rBIPRFB.png)

![alt text](https://i.imgur.com/h5eX0Fb.png)


### Muut toiminnallisuudet

## Ohjelman rakenteeseen jääneet heikkoudet