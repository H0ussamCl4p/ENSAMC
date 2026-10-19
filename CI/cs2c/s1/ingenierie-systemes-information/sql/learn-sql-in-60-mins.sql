

CREATE DATABASE test;

 DROP DATABASE test;
 
 CREATE DATABASE record_company;
 
 use record_company;
 
 CREATE TABLE test(
	test_column INT 
 );
 
 ALTER TABLE test
 ADD another_column VARCHAR(255);
 
 DROP TABLE test;
 
 CREATE TABLE bands(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
 );
 
 CREATE TABLE albums(
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    realease_year INT,
    band_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (band_id) REFERENCES bands(id)
 );
 
 INSERT INTO bands (name)
 VALUES ('Iron Maiden');
 
 INSERT INTO bands (name)
 VALUES ('Deuce'),('Avenged Sevenfold'), ('Ankor');
 
 SELECT * FROM  bands;
 
 SELECT * FROM bands LIMIT 2;
 
 SELECT name FROM bands;
 
 SELECT id AS 'ID' , name AS 'Band Name'
 FROM bands;
 
 SELECT * FROM bands ORDER BY name;
 
 INSERT INTO albums(name, realease_year, band_id)
 VALUES ('The Number of the Beasts', 1985, 1),
		('Power Slave', 1984, 1),
        ('Nightmare', 2018, 2),
        ('Nightmare', 2010, 3),
        ('Test Album', NULL, 3);
 
 SELECT * FROM albums;
 
 SELECT DISTINCT name FROM albums;
 
 UPDATE albums
 SET realease_year = 1982 
 WHERE id=1;
 
 SELECT * FROM albums 
 WHERE realease_year < 2000;
 
 SELECT * FROM albums
 WHERE name LIKE '%er%' OR band_id=2;
 
 SELECT * FROM albums
 WHERE realease_year=1984 AND band_id=1;
 
 SELECT * FROM albums
 WHERE realease_year BETWEEN 2000 AND 2018;
 
 SELECT * FROM albums
 WHERE realease_year IS NULL;
 
 DELETE FROM albums WHERE id=5;
 
 SELECT * FROM bands
 JOIN albums ON bands.id=albums.id;

 SELECT * FROM bands
 LEFT JOIN albums ON bands.id=albums.id;
 
SELECT * FROM albums
 RIGHT JOIN bands ON bands.id=albums.id;
 
 SELECT AVG(realease_year) FROM albums;
 
SELECT band_id, COUNT(band_id) FROM albums
GROUP BY band_id; 



