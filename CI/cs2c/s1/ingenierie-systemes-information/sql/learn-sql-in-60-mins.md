# Apprendre SQL en 60 Minutes : Synthèse du Tutoriel

By [Learn SQL in 60 Minutes - Web Dev Simplified](https://youtu.be/p3qvj9hO_Bo?si=02t-R6j5h9cLVvSB)

## Résumé Exécutif

Ce document synthétise les concepts clés du tutoriel vidéo **"Learn SQL In 60 Minutes"** de la chaîne YouTube **Web Dev Simplified**. Le tutoriel vise à couvrir environ **95 % des utilisations courantes de SQL**, le présentant comme un langage simple à apprendre mais complexe à maîtriser. L'objectif principal est de fournir une base solide sur le **SQL (Structured Query Language)**, le langage universel pour interagir avec les bases de données relationnelles.

La synthèse aborde les concepts fondamentaux, en commençant par la définition d'une base de données comme une collection de tables liées entre elles. Elle détaille ensuite la syntaxe SQL, y compris les mots-clés, la casse et l'utilisation de points-virgules. Le document explore en profondeur les commandes de création et de gestion (**Data Definition Language - DDL**) telles que `CREATE`, `DROP` et `ALTER` pour les bases de données et les tables. L'accent est mis sur la définition des colonnes, des types de données (`INT`, `VARCHAR`) et des contraintes essentielles comme `NOT NULL`, `AUTO_INCREMENT`, `PRIMARY KEY` et `FOREIGN KEY`.

La partie centrale du document est consacrée à la manipulation des données (**Data Manipulation Language - DML**) via les commandes `INSERT`, `SELECT`, `UPDATE` et `DELETE`. La commande `SELECT` est examinée en détail, avec ses multiples options de filtrage (`WHERE`), de tri (`ORDER BY`), de limitation (`LIMIT`) et de sélection de données uniques (`DISTINCT`).

Enfin, le document aborde des sujets plus avancés qui constituent la véritable puissance de SQL : les **jointures** (`JOIN`, `LEFT JOIN`) pour combiner les données de plusieurs tables, et les **fonctions d'agrégation** (`COUNT`, `AVG`, `SUM`) associées au regroupement (`GROUP BY`) et au filtrage post-agrégation (`HAVING`). Le tutoriel utilise un exemple pratique de base de données pour une maison de disques, avec des tables `bands` et `albums`, pour illustrer concrètement chaque commande.

---

## 1. Introduction au SQL et aux Bases de Données

### 1.1. Qu'est-ce que le SQL ?

SQL, ou **Structured Query Language**, est un langage de programmation conçu spécifiquement pour la gestion des données dans les systèmes de gestion de bases de données relationnelles (SGBDR). Ses fonctions principales sont encapsulées par l'acronyme **CRUD** :

* **Create** (Créer)
* **Read** (Lire)
* **Update** (Mettre à jour)
* **Delete** (Supprimer)

La connaissance du SQL est universelle et s'applique à la quasi-totalité des SGBDR, bien que des fonctionnalités spécifiques puissent varier entre les systèmes (par exemple **MySQL**, **PostgreSQL**, etc.).

### 1.2. L'importance d'apprendre le SQL

La maîtrise du SQL est cruciale pour les développeurs, car presque toutes les applications - mobiles, web ou de bureau - interagissent avec des données. Les bases de données sont l'un des moyens les plus efficaces et répandus pour stocker des données à petite et grande échelle. Un développeur rencontrera donc inévitablement le besoin de travailler avec des bases de données au cours de sa carrière.

### 1.3. Structure d'une Base de Données Relationnelle

Une base de données est une collection organisée de données, structurée en tables.

* **Table** : représente un modèle de données unique (ex. `users`, `products`).
* **Ligne (row / record)** : correspond à un enregistrement individuel.
* **Colonne (column)** : représente une propriété ou un attribut du modèle (ex. `id`, `name`, `email`).

Le terme *relationnelle* provient de la capacité à créer des liens entre les tables afin de construire des systèmes de données complexes.

---

## 2. Syntaxe et Configuration de l'Environnement

### 2.1. Syntaxe de Base du SQL

* **Mots-clés** : `SELECT`, `CREATE`, `FROM`, `WHERE`, etc.
* **Sensibilité à la casse** : SQL n'est pas sensible à la casse, mais la convention veut que les mots-clés soient en majuscules.
* **Point-virgule (`;`)** : termine une commande SQL et est indispensable pour séparer plusieurs requêtes.
* **Chaînes de caractères** : délimitées par des apostrophes (`' '`).
* **Sauts de ligne** : ignorés par SQL, ce qui permet de formater les requêtes pour plus de lisibilité.

### 2.2. Environnement de Travail

Le tutoriel utilise **MySQL Workbench** connecté à un serveur MySQL local. Les requêtes sont exécutées dans un nouvel onglet de requête.

---

## 3. Gestion de la Base de Données et des Tables (DDL)

### 3.1. Création et Suppression de Bases de Données

| Commande          | Description                            | Exemple                           |
| ----------------- | -------------------------------------- | --------------------------------- |
| `CREATE DATABASE` | Crée une nouvelle base de données      | `CREATE DATABASE record_company;` |
| `DROP DATABASE`   | Supprime une base de données existante | `DROP DATABASE test;`             |
| `USE`             | Sélectionne la base de données active  | `USE record_company;`             |

> Après `CREATE DATABASE`, il peut être nécessaire de rafraîchir la vue des schémas.

### 3.2. Création de Tables

```sql
CREATE TABLE bands (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);
```

**Éléments clés :**

* **Types de données** :

  * `INT`
  * `VARCHAR(n)`
* **Contraintes** :

  * `NOT NULL`
  * `AUTO_INCREMENT`
* **PRIMARY KEY** :

  * Identifie chaque enregistrement de manière unique
  * Crée automatiquement un index

### 3.3. Modification et Suppression de Tables

| Commande      | Description                       | Exemple                                             |
| ------------- | --------------------------------- | --------------------------------------------------- |
| `ALTER TABLE` | Modifie la structure d'une table  | `ALTER TABLE test ADD another_column VARCHAR(255);` |
| `DROP TABLE`  | Supprime une table et ses données | `DROP TABLE test;`                                  |

### 3.4. Clés Étrangères (FOREIGN KEY)

```sql
CREATE TABLE albums (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  release_year INT,
  band_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (band_id) REFERENCES bands(id)
);
```

La contrainte `FOREIGN KEY` assure l'intégrité référentielle entre les tables.

---

## 4. Manipulation des Données (DML)

### 4.1. Insertion de Données

```sql
INSERT INTO bands (name)
VALUES ('Iron Maiden');
```

```sql
INSERT INTO bands (name)
VALUES ('Deuce'), ('Avenged Sevenfold'), ('Anchor');
```

### 4.2. Lecture de Données (SELECT)

| Syntaxe             | Description          | Exemple                                  |
| ------------------- | -------------------- | ---------------------------------------- |
| `SELECT *`          | Toutes les colonnes  | `SELECT * FROM bands;`                   |
| `SELECT col1, col2` | Colonnes spécifiques | `SELECT name FROM bands;`                |
| `LIMIT n`           | Limite les résultats | `SELECT * FROM bands LIMIT 2;`           |
| `AS`                | Alias de colonne     | `SELECT id AS 'ID' FROM bands;`          |
| `ORDER BY`          | Trie les résultats   | `SELECT * FROM bands ORDER BY name ASC;` |
| `DISTINCT`          | Valeurs uniques      | `SELECT DISTINCT name FROM albums;`      |

### 4.3. Mise à Jour de Données

```sql
UPDATE albums
SET release_year = 1982
WHERE id = 1;
```

### 4.4. Suppression de Données

```sql
DELETE FROM albums
WHERE id = 5;
```

---

## 5. Requêtes Avancées

### 5.1. Filtrage avec WHERE

| Opérateur  | Description               | Exemple                                                           |
| ---------- | ------------------------- | ----------------------------------------------------------------- |
| `=, <, >`  | Comparaisons              | `SELECT * FROM albums WHERE release_year < 2000;`                 |
| `LIKE`     | Recherche de motif        | `SELECT * FROM albums WHERE name LIKE '%er%';`                    |
| `AND / OR` | Combinaison de conditions | `SELECT * FROM albums WHERE release_year = 1984 AND band_id = 1;` |
| `BETWEEN`  | Plage de valeurs          | `SELECT * FROM albums WHERE release_year BETWEEN 2000 AND 2018;`  |
| `IS NULL`  | Valeurs nulles            | `SELECT * FROM albums WHERE release_year IS NULL;`                |

### 5.2. Jointures (JOIN)

* **INNER JOIN** : uniquement les correspondances
* **LEFT JOIN** : toutes les lignes de la table de gauche
* **RIGHT JOIN** : toutes les lignes de la table de droite

### 5.3. Fonctions d'Agrégation

| Fonction  | Description | Exemple                                 |
| --------- | ----------- | --------------------------------------- |
| `AVG()`   | Moyenne     | `SELECT AVG(release_year) FROM albums;` |
| `SUM()`   | Somme       | `SELECT SUM(release_year) FROM albums;` |
| `COUNT()` | Comptage    | `SELECT COUNT(band_id) FROM albums;`    |

#### GROUP BY

```sql
SELECT band_id, COUNT(band_id)
FROM albums
GROUP BY band_id;
```

#### HAVING

```sql
SELECT b.name AS band_name, COUNT(a.id) AS num_albums
FROM bands AS b
LEFT JOIN albums AS a ON b.id = a.band_id
GROUP BY b.id
HAVING num_albums = 1;
```
