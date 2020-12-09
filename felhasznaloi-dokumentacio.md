# Parancssoros Tetris játék

# - Felhasználói dokumentáció

> Készítette: Schelb Arnold - S761AX
> 
> Laborvezető: Sinkovics Bálint

A program egy parancssorban futtatható Tetris játékot valósít meg, mely a `main.py` file-lal futtatható.

## A játékról

A Tetris nevű játékot a '90-es években alkotta meg egy orosz mérnök, Alexey Pajitnov.

Működése kirakósra hasonlít, egy kis csavarral. Itt ugyanis nem áll rendelkezésre minden elem egyszerre, hanem egymás után "esnek" a négyzetekre szabdalt pályára, felülről lefelé.

A játék célja az, hogy az elemek megfelelő helyre rakásával és forgatásával a játékos minél több pontot szerezzen. A játékosnak addig van ideje eldönteni, hogy az adott elem hova és milyen forgatással kerüljön, amíg az le nem esik a pálya legaljára, vagy egy, már elhelyezett elemhez nem ér.

A játékosnak arra kell törekednie, hogy a pálya adott sora tele legyen. Ilyenkor a sor letörlődik, és a sor felett lévő elemek kitöltik a felszabadult helyet (leesnek). Így a játékosnak több tere lesz, ami a játék folytatását könnyíti, és plusz pont is így szerezhető.

A pontok növekedésével viszont fokozatosan egyre gyorsabb lesz az új darabok esési sebessége, így a játékosnak kevesebb ideje lesz gondolkodni/reagálni, ezzel nehezítve a játékot.

A játékban lerakható darabok ún. tetromínók, tehát 4 db négyzetből, éleik összekapcsolásával felépíthető alakzatok. Ez alapján 7 féle elemet különböztetünk meg, ezekből 2-2 tükörképe egymásnak, viszont kizárólag forgatással nem mozgathatók egymásba. Ezeket a darabokat négyzetegységenként lehet mozgatni jobbra-balra (vagy lefelé, az esés gyorsításához), hogy aztán a felhasználó által választott helyre kerüljenek.

A játék végét az jelenti, amikor a fentről beérkező következő darab nem tud teljesen megjelenni a játéktéren, mivel egy korábban lerakott darab ezt megakadályozza. A pálya ilyenkor "telt meg", és a játék befejeződik.

## A program főbb funkciói:

- [x] Új játék indítása, megadható mérettel és kezdő szinttel.
- [x] Mentett játék betöltése file-ból.
- [x] Játékállás mentése file-ba.
- [x] Ha a pontszám a mentett legjobb 5 közé esik, pontszám mentése.
- [x] Dicsőséglista áttekintése.

## Irányítás

- A menüben való navigálásnál az irányítás módja a képernyőn olvasható.
- Játék közben pedig:
  - Jobbra-balra nyilakkal az adott tetromínó a megfelelő irányba mozgatható.
  - Felfelé nyíllal óramutató járása szerint forgatható.
  - Lefelé nyíllal 1 egységgel lejjebb mozgatható.
  - Escape billentyűvel játék közben a játék megállítható, menüben pedig visszalépést, illetve kilépést eredményez.

## Pontozás

- A játékbeli pontszám kétféleképpen növelhető:
  - A tetromínó lefelé mozgatásával, ez egységenként `1 * szint` pontot jelent.
  - Egy sor teljes "kirakásával", ez soronként `100 * szint` pontot jelent, a következő kivételekkel:
    - Egyszerre 2 sor kirakásánál: `(200+100) * szint` pont.
    - 3 sor kirakásánál: `(300 + 200) * szint` pont.
    - 4 sor kirakásánál (Tetris): `400 * 2 * szint` pedig pont.
