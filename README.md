# Piikkilista
## Aihekuvaus
Tehtävänä on toteuttaa www-sivuila toimiva piikkilista. Piikkilistaan
tulee kirjautua joko admin- tai user-tunnuksella. Listalle
lisätyn asiakkaan piikkiin lisätään, jos asiakas ostaa jotain ja piikistä
voidaan vähentää, jos asiakas maksaa piikkiä pois. Asiakas tunnistetaan
etunimen, toisen nimen, sukunimen ja järjestön perusteella.

User-käyttäjä voi lisätä asiakkaan piikkiin tilauksia, jotka sisältävät 
yhden tai useamman juoman. Piikkiä voidaan myös maksaa pois. User tason 
käyttäjä voi myös hakea yksittäisen henkilön piikin ja eston 
tämänhetkisen tilan.

Admin-käyttäjä voi lisätä/päivittää/poistaa järjestöjä ja asiakkaita,
jäädyttää asiakkaan piikin, vaihtaa käyttäjän salasanan (user & admin)
ja muuttaa juoman hintaa. Admin-käyttäjä näkee yhteenvedon kaikista
asiakkaista ja heidän ostoshistoriastaan.

Toimintoja:
- Kirjautuminen
- Salasanan vaihto
- Asiakkaan lisäys / tietojen päivitys / jäädyttäminen / poisto
- Organisaation lisäys / tietojen päivitys / poisto
- Juomahinnaston muuttaminen
- Asiakkaan piikin tilan ja eston tarkastaminen
- Yhteenveto asiakkaan tilaushistoriasta

## Demo
Demo löytyy osoitteesta: https://tsoha-piikkilista.herokuapp.com/

### Järjestöjen lisäys
1. Navigoi yläpalkista löytyvälle 'Järjestöt' -sivulle
2. Lisäyssivustolle pääset painamalla 'Lisää järjestöjä' -linkkiä
3. Anna järjestölle nimi ja ja klikkaa 'Lisää järjestö'

### Asiakkaiden lisäys
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Lisäyssivuostlle pääset painamalla 'Lisää asiakas' -linkkiä
3. Lisää asiakkaalle etu- ja sukunimi
4. Lisää asiakkaalle syntymäpäivä

   Esimerkki: Jos asikkaan syntymäpäivä on 17. päivä Tammikuuta,
   niin syntymäpäivä kirjoitetaan 1701 (vielä toistaiseksi)
   
5.Lisää asiakkaalle piikki (sentteinä vielä toistaiseksi)

   Esimerkki: Jos asiakkaalla on piikki 7,50€ positiivisella puolella,
   niin piikki annetaan muodossa 750
   
6. Anna asiakkaan järjestö (valitse sallituista järjestöistä)
7. Klikkaa 'Lisää asiakas'
