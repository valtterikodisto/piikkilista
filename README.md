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
- Salasanan vaihto [TULOSSA]
- Asiakkaan lisäys / tietojen päivitys / jäädyttäminen / poisto
- Organisaation lisäys / (tietojen päivitys [TULOSSA] / poisto [TULOSSA])
- Juomahinnaston muuttaminen [TULOSSA]
- Asiakkaan piikin tilan ja eston tarkastaminen
- Yhteenveto asiakkaan tilaushistoriasta [TULOSSA]
- Yhteenveto järjestön piikillisistä jäsenistä ja kokonaispiikista

## Demo
Demo löytyy osoitteesta: https://tsoha-piikkilista.herokuapp.com/
Käyttäjänimi: `admin`
Salasana: `admin`

## Toiminnot

### Järjestöjen lisäys
1. Navigoi yläpalkista löytyvälle 'Järjestöt' -sivulle
2. Lisäyssivustolle pääset painamalla 'Lisää järjestöjä' -linkkiä
3. Anna järjestölle nimi ja ja klikkaa 'Lisää järjestö'

### Asiakkaiden lisäys
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Lisäyssivustolle pääset painamalla 'Lisää asiakas' -linkkiä
3. Lisää asiakkaalle etu- ja sukunimi
4. Lisää asiakkaalle syntymäpäivä

   Esimerkki: Jos asikkaan syntymäpäivä on 17. päivä Tammikuuta,
   niin syntymäpäivä kirjoitetaan 1701 (vielä toistaiseksi)
   
5. Lisää asiakkaalle piikki (sentteinä vielä toistaiseksi)

   Esimerkki: Jos asiakkaalla on piikki 7,50€ positiivisella puolella,
   niin piikki annetaan muodossa 750
   
6. Anna asiakkaan järjestö (valitse sallituista järjestöistä)
7. Klikkaa 'Lisää asiakas'

### Asiakkaan tietojen päivitys
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Valitse haluamasi asiakas ja paina etunimen vasemmalla olevaa linkkiä 'Tiedot'
3. Klikkaa 'Muokkaa käyttäjän tietoja' nappia ja täytä jokainen kenttä
4. Klikkaa päivitä tiedot, jolloin tiedot päivittyvät

### Asiakkaan poisto
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Klikkaa haluamasi asiakkaan riviltä löytyvää 'Profiili' -painiketta
3. Klikkaa 'Muokkaa käyttäjän tietoja' nappia
4. Klikkaa 'Poista käyttäjä'

### Asiakkaan esto (pysyvä)
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Klikkaa haluamasi asiakkaan riviltä löytyvää 'Profiili' -painiketta
3. Valitse kalenteristä eston loppumisajankohta
4. Klikkaa 'Estä käyttäjä', jonka vahvista esto painamalla 'OK'

   HUOM! Esto on pysyvä eikä sitä ole mahdollista poistaa. Jos siis
   estät asiakkaan tietyksi ajanjaksoksi, niin ainut keino poistaa
   esto on odottaa eston loppumiseen asti.

## Muuta

[Käyttäjätarinat](https://github.com/valtterikodisto/piikkilista/blob/master/documentation/user_stories.md)
[Tietokantakaavio](https://github.com/valtterikodisto/piikkilista/tree/master/documentation/database.png)
