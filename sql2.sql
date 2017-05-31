CREATE DATABASE salongier;
USE salongier;

CREATE TABLE `Gry` (
  `id_gry` mediumint,
  `nazwa` varchar(30) default NULL,
  `rok_produkcji` mediumint default NULL,
  `gatunek` varchar(30) default NULL,
  PRIMARY KEY (`id_gry`)
);

CREATE TABLE `Wyniki` (
  `id_gracza` mediumint default NULL,
  `id_gry` mediumint default NULL,
  `wynik` mediumint default NULL
);

CREATE TABLE `Gracze` (
  `id_gracza` mediumint,
  `imie` varchar(30) default NULL,
  `nazwisko` varchar(30) default NULL,
  `adres` varchar(50) default NULL,
  `email` varchar(50) default NULL,
  PRIMARY KEY (`id_gracza`)
);

LOAD DATA LOCAL INFILE 'Gry2.csv' INTO TABLE Gry
  FIELDS TERMINATED BY '|' 
  LINES TERMINATED BY '\r\n'
  IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Wyniki2.csv' INTO TABLE Wyniki
  FIELDS TERMINATED BY '|' 
  LINES TERMINATED BY '\r\n'
  IGNORE 1 LINES;

LOAD DATA LOCAL INFILE 'Gracze.csv' INTO TABLE Gracze
  FIELDS TERMINATED BY '|' 
  LINES TERMINATED BY '\r\n'
  IGNORE 1 LINES;


