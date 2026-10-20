---
title: "SQL en 60 minutes"
date: 2025-10-10
author: CHOUBIK Houssam
tags: [sql, cs2c]
---

# SQL en 60 minutes

Mes notes de la vidéo [Learn SQL in 60 Minutes](https://youtu.be/p3qvj9hO_Bo) (Web Dev Simplified). Le script complet est dans [sql-en-60-minutes.sql](sql-en-60-minutes.sql).

## 1. Introduction au SQL et aux Bases de Données

### 1.1. Qu'est-ce que le SQL ?

SQL, ou **Structured Query Language**, est un langage de programmation conçu spécifiquement pour la gestion des données dans les systèmes de gestion de bases de données relationnelles (SGBDR). Ses fonctions principales sont encapsulées par l'acronyme **CRUD** :

* **Create** (Créer)
* **Read** (Lire)
* **Update** (Mettre à jour)
* **Delete** (Supprimer)

La connaissance du SQL est universelle et s'applique à la quasi-totalité des SGBDR, bien que des fonctionnalités spécifiques puissent varier entre les systèmes (par exemple **MySQL**, **PostgreSQL**, etc.).

### 1.2. Structure d'une Base de Données Relationnelle

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
