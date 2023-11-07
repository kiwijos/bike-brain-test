# bike-brain-test

Ett repo som jobbar med tre containrar där en är databas, en är server och en tredje som gör automatiska request till servern. Databsen är mariadb, servern är i javascript och automatiken görs me python.

Jämför en elsparkcykel som skickar ut data till en server via ett api.

## Testa det lilla som finns
Just nu gör inte repot så mycket, men man kan starta upp det med:

```
docker-compose up -d --build
```

Det bygger först två containrar, en express-server och en python container. 

Sedan startar mariadb, där en heathcheck görs så att inte express containern startar före databsen är uppe och snurrar vilket gör uppstarten tar lite längre tid. Detta kan man ändra så det blir effektivare/snabbare, men nu är bara tanken att det ska fungera.

Sedan startar express servern. Sidan har url http://localhost:1337, där det bara visar att servern är igång och skickar ut data från tabellen 'bike' i databasen som är tom från start.

Man kan sen starta python containern och se till man hamnar i bash.

```
docker-compose run python bash
```

Nu kan man köra filen som ligger där, vilket i sin tur gör 10 POST-request till servern med data med en sekunds intervall.
```
python app.py
```
I en simulering tänker jag att man ser till detta blir automatiskt, eller att man triggar scriptet på något sätt utifrån med en knapp i webbläsaren "Starta simulering" eller liknande.

Man kan sen se reslutatet i webbläsaren, och gör man det samtidigt som scriptet körs så hämtar ju då den det som finns i databasen vid den requesten.

Stäng ner nätverket.
```
docker-compose down -v
```
