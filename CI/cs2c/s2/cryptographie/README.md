# Introduction à la cryptographie appliquée (CS2C, S2)

TP en Python (notebooks Jupyter). Chaque dossier contient l'énoncé et la correction.

| TP | Sujet | Contenu |
|---|---|---|
| [TP1](tp/tp1/tp1-crypto-artisanale.ipynb) | Cryptographie artisanale | César (force brute, analyse statistique), substitution mono-alphabétique, homophone, Polybe, Vigenère (Kasiski, indice de coïncidence), Hill |
| [TP2](tp/tp2/tp2-chiffrement-flux.ipynb) | Chiffrement par flux | LFSR, période, attaque à clair connu, générateur de Geffe, comparaison LFSR / Trivium / Salsa20 / ChaCha20 |
| [TP3](tp/tp3/tp3-padding-oracle-cbc.ipynb) | Padding oracle (AES-CBC) | Attaque octet par octet sans la clé, questions de réflexion |
| [TP4](tp/tp4/tp4-asymetrique.ipynb) | Cryptographie asymétrique | Euclide étendu, restes chinois, RSA et RSA-CRT, Pollard rho, baby-step giant-step, ElGamal et réutilisation de l'aléa |

Les énoncés : [TP1](tp/tp1/enonce.pdf), [TP2](tp/tp2/enonce.pdf), [TP3](tp/tp3/enonce.pdf), [TP4](tp/tp4/enonce.pdf).

Bibliothèques : `pip install pycryptodome numpy`

TP3 : le bloc intercepté donné dans l'énoncé ne se déchiffre pas avec un padding valide sous la clé du serveur. Le notebook vérifie donc aussi l'attaque sur un message qu'on chiffre soi-même.
