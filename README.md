# Piikkilista
## Aihekuvaus
Tehtävänä on toteuttaa www-sivuila toimiva piikkilista. Piikkilistaan
tulee kirjautua joko admin- tai user-tunnuksella. Listalle
lisätyn asiakkaan piikkiin lisätään, jos asiakas ostaa jotain ja piikistä
voidaan vähentää, jos asiakas maksaa piikkiä pois. Asiakas tunnistetaan
etunimen, sukunimen, (syntymäpäivän) ja järjestön perusteella.

User-käyttäjä voi lisätä asiakkaan piikkiin tilauksia, jotka sisältävät 
yhden tai useamman juoman. Piikkiä voidaan myös maksaa pois. User tason 
käyttäjä voi myös hakea yksittäisen henkilön piikin ja eston 
tämänhetkisen tilan.

Admin-käyttäjä voi lisätä/päivittää/poistaa järjestöjä ja asiakkaita,
jäädyttää asiakkaan piikin, vaihtaa käyttäjän salasanan (user & admin)
ja muuttaa juoman hintaa. Admin-käyttäjä näkee yhteenvedon kaikista
asiakkaista ja heidän ostoshistoriastaan.

Toimintoja:
- Kirjautuminen (admin, user)
- Asiakkaan lisäys / tietojen päivitys / jäädyttäminen / poisto
- Automaattinen piikin jäätyminen, kun piikki liian suuri
- Organisaation lisäys
- Asiakkaan piikin tilan ja eston tarkastaminen
- Yhteenveto asiakkaan tilaushistoriasta
- Yhteenveto järjestön piikillisistä jäsenistä ja kokonaispiikista

## Demo
Demo löytyy osoitteesta: https://tsoha-piikkilista.herokuapp.com/
Käyttäjänimi: `admin`
Salasana: `admin`

## Toiminnot

### Järjestöjen lisäys
1. Navigoi yläpalkista löytyvälle 'Järjestöt' -sivulle
2. Lisäyssivustolle pääset painamalla 'Lisää järjestöjä' -linkkiä
3. Anna järjestölle nimi ja järjestön jäsenen maksimivelka (tämän ylittyessä piikki jäätyy, kunnes se maksetaan kokonaan)
4. Klikkaa 'Lisää järjestö'

### Järjestön tietojen päivitys
1. Navigoi yläpalkista löytyvälle 'Järjestöt' -sivulle
2. Paina haluamasi järjestön rivin oikeasta laidasta löytyvää 'Muokkaa' -nappia
3. Täytä jokainen lomakkeen kenttä
4. Klikkaa 'Päivitä tiedot', jolloin tiedot päivittyvät

### Järjestön poisto
1. Navigoi yläpalkista löytyvälle 'Järjestöt' -sivulle
2. Paina haluamasi järjestön rivin oikeasta laidasta löytyvää 'Muokkaa' -nappia
3. Klikkaa 'Poista järjestö'

   HUOM! Poistamalla järjestön, poistat myös jokaisen järjestöön kuuluvan asiakkaan. 
   Tällöin siis menetät myös jokaiseen asiakkaaseen liittyvät tiedot.

### Asiakkaiden lisäys
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Lisäyssivustolle pääset painamalla 'Lisää asiakas' -linkkiä
3. Lisää asiakkaalle etu- ja sukunimi
4. Lisää asiakkaalle syntymäpäivä

   Esimerkki: Jos asikkaan syntymäpäivä on 17. päivä Tammikuuta,
   niin syntymäpäivä kirjoitetaan 1701
   
5. Lisää asiakkaalle piikki

   Esimerkki: Jos asiakkaalla on piikki 7,50€ positiivisella puolella,
   niin piikki annetaan muodossa 7.5
   
6. Anna asiakkaan järjestö (valitse sallituista järjestöistä)
7. Klikkaa 'Lisää asiakas'

### Asiakkaan tietojen päivitys
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Valitse haluamasi asiakas ja paina etunimen vasemmalla olevaa painiketta 'Profiili'
3. Klikkaa 'Muokkaa käyttäjän tietoja' nappia ja täytä jokainen kenttä
4. Klikkaa 'Päivitä tiedot', jolloin tiedot päivittyvät

### Asiakkaan poisto
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Klikkaa haluamasi asiakkaan riviltä löytyvää 'Profiili' -painiketta
3. Klikkaa 'Muokkaa käyttäjän tietoja' nappia
4. Klikkaa 'Poista käyttäjä'

   HUOM! Poistamalla asiakkaan, menetät kaikki asiakkaaseen liittyvät tiedot.

### Asiakkaan esto (pysyvä)
1. Navigoi yläpalkista löytyvälle 'Asiakkaat' -sivulle
2. Klikkaa haluamasi asiakkaan riviltä löytyvää 'Profiili' -painiketta
3. Valitse kalenteristä eston loppumisajankohta
4. Klikkaa 'Estä käyttäjä', jonka vahvista esto painamalla 'OK'

   HUOM! Esto on pysyvä eikä sitä ole mahdollista poistaa. Jos siis
   estät asiakkaan tietyksi ajanjaksoksi, niin ainut keino poistaa
   esto on odottaa eston loppumiseen asti.
   
### Tilauksen tekeminen
1. Navigoi yläpalkista etusivulle painamalla 'Piikkilistaa'
2. Syötä olemassa olevan asiakkaan tiedot kenttiin
   
   HUOM! Mikäli useammalla asiakkaalla samassa järjestössä on sama etu- ja 
   sukunimi, lomakkeen lähettämisen jälkeen ilmestyy syntymäpäiväkenttä. Täytä 
   kenttä asiakkaan syntymäpäivällä ja paina lähetä lomake uudelleen. 
   
3. Lisää +/- painikkeilla juomia tilaukseen
4. Mikäli asiakas tekee talletuksen, lisää se talletuskenttään (talletus saa olla negatiivinen)
5. Klikkaa 'Lisää ostos'

## Asennusohje

### Lataus ja suoritus
Jotta saat sovelluksen pyörimään lokaalisti, tarvitset ainakin seuraavat: `python3, pip, sqlite3, git`.
```bash
git clone https://github.com/valtterikodisto/piikkilista
cd piikkilista
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Sovelluksen saat tämän jälkeen auki suorittamalla `python3 run.py`, jonka jälkeen sovellus löytyy osoitteesta http://localhost:5000. Tietokannassa ei kuitenkaan ole käyttäjätunnuksia, joten joudumme lisäämään ne seuraavasti:

```bash
cd application/
sqlite3 piikkilista.db
```
```SQL
INSERT INTO account (username, password, admin) VALUES ('admin', 'admin', 1);
```
Normaalien käyttäjien lisäys taas tapahtuu rekisteröintisivulla: http://localhost:5000/register

## Muuta

### Linkkejä

[Käyttäjätarinat](https://github.com/valtterikodisto/piikkilista/blob/master/documentation/user_stories.md) <br />
[Tietokantakaavio](https://github.com/valtterikodisto/piikkilista/tree/master/documentation/database.png) <br />
[CREATE TABLE -lauseet](https://github.com/valtterikodisto/piikkilista/tree/master/documentation/create_table.md)

### Miksi syntymäpäivä on kokonaisluku?
Syntymäpäivän olisi helposti voinut toteuttaa myös tyyppinä DATE. Syntymäpäivän arvolla ei sinänsä ole väliä. Sen tarkoitus 
on ainoastaan toimia helposti muistettavana "tunnisteena", mikäli järjestöön kuuluu useita samannimisiä asiakkaita.

### Puuttuvat ominaisuudet
Projektiin kaavailtiin alussa, että olisi helppoa muuttaa juomahinnastoa ja että käyttäjä pystyisi vaihtamaan salasanan. 
Nämä ominaisuudet eivät kuitenkaan kerenneet tähän projektiin.