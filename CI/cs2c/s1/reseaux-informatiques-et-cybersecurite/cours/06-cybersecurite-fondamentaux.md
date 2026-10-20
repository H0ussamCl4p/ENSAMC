# Cybersécurité : les fondamentaux

## La triade CIA

La sécurité repose sur trois objectifs.

### 1. Confidentialité : garder les données secrètes

On utilise le **chiffrement** : il transforme un texte clair en texte chiffré, illisible sans la clé.

**Par flot ou par bloc :**

- **chiffrement par flot** (*stream cipher*) : bit par bit, en temps réel. Exemple : A5, utilisé pour les appels GSM ;
- **chiffrement par bloc** (*block cipher*) : les données sont découpées en blocs de taille fixe (128 bits pour AES), chiffrés un par un. Exemple : **AES**, la référence actuelle du chiffrement symétrique (Wi-Fi, VPN, disques).

Le **mode CTR** (compteur) transforme un chiffrement par bloc en chiffrement par flot.

**Symétrique ou asymétrique :**

| | Symétrique | Asymétrique |
|---|---|---|
| Clés | Une seule clé, partagée | Une paire : clé publique et clé privée |
| Vitesse | Rapide | Lent |
| Problème | Partager la clé en sécurité | Calculs coûteux |
| Exemples | AES, DES, 3DES (DES et 3DES sont dépassés) | RSA, ECC (courbes elliptiques) |

En asymétrique, on **chiffre avec la clé publique** du destinataire, qui **déchiffre avec sa clé privée**. Pour une **signature**, c'est l'inverse : on signe avec sa clé privée, tout le monde vérifie avec la clé publique.

En pratique on combine les deux : l'asymétrique (ou **Diffie-Hellman**) sert à se mettre d'accord sur une clé, puis l'échange se fait en symétrique. C'est ce que fait TLS.

**Certificats :**

- une **autorité de certification (CA)** émet et gère les certificats numériques ; la **CA racine** est le point de confiance de départ ;
- **OCSP** (Online Certificate Status Protocol) et les **CRL** (listes de révocation) indiquent si un certificat a été révoqué ;
- il existe des CA payantes et gratuites (Let's Encrypt est gratuite).

### 2. Intégrité : vérifier que rien n'a changé

**Fonction de hachage** : produit une empreinte de taille fixe ; la moindre modification des données change l'empreinte.

| Algorithme | État |
|---|---|
| MD5 | Cassé (collisions faciles), à ne plus utiliser |
| SHA-1 | Cassé (collision démontrée en 2017) |
| SHA-2 (SHA-256, SHA-512) | Sûr, le plus utilisé |
| SHA-3 | Sûr, conception différente de SHA-2 |

- **HMAC** : empreinte calculée avec une clé secrète. Elle prouve l'**intégrité** et l'**authenticité** (seul le détenteur de la clé a pu la produire).
- **Sel** (*salt*) : valeur aléatoire ajoutée à chaque mot de passe avant hachage. Deux mots de passe identiques n'ont plus la même empreinte, ce qui rend inutiles les **tables arc-en-ciel** (*rainbow tables*, empreintes précalculées).
- **EDR** (Endpoint Detection and Response) détecte les comportements suspects sur un poste, comme la modification de fichiers système. **XDR** (Extended Detection and Response) fait la même chose sur plusieurs sources : postes, serveurs, réseau, cloud.

### 3. Disponibilité : un service accessible quand il le faut

Se protéger des pannes et des dénis de service : redondance, sauvegardes, alimentation de secours, plans de reprise.

## Vulnérabilité, menace, risque

- **Vulnérabilité** : une faiblesse exploitable. Elle peut venir de la configuration (mot de passe par défaut, ports ouverts), du logiciel (système pas à jour, bugs), du matériel (firmware non corrigé, chaîne d'approvisionnement) ou de l'humain (négligence, ingénierie sociale, employé mécontent).
- **Menace** : un événement qui pourrait exploiter une vulnérabilité. Humaine (pirates, employés, concurrents), naturelle (inondation, incendie, séisme) ou technique (malware, DDoS, panne).
- **Risque** : la probabilité qu'une menace exploite une vulnérabilité, multipliée par l'impact sur les biens. Toute la cybersécurité consiste à comprendre, mesurer et réduire le risque.

Pour évaluer le risque : **inventorier ses biens** (matériel, logiciels, données ; un **SBOM**, Software Bill of Materials, liste les composants et dépendances d'un logiciel), puis **estimer l'impact** d'une attaque réussie.

### Les 4 réponses au risque

1. **Accepter** : le risque est faible ou inévitable. On le documente et on le surveille.
2. **Réduire** (*mitigate*) : ajouter des mesures pour baisser la probabilité ou l'impact.
3. **Éviter** : supprimer l'activité qui crée le risque.
4. **Transférer** : le confier à un tiers, par une assurance ou un contrat (sous-traitance avec un **SLA**, Service Level Agreement).

## NIST Cybersecurity Framework

Cadre de référence du **NIST** (National Institute of Standards and Technology), utilisé dans le monde entier :

1. **Identifier** : connaître ses biens, ses risques et ses dépendances (l'étape la plus difficile) ;
2. **Protéger** : correctifs, pare-feu, gestion des identités, sauvegardes ;
3. **Détecter** : supervision, SOC, détection d'anomalies ;
4. **Répondre** : avoir un plan de réponse aux incidents **et le tester** (rôle du CIRT) ;
5. **Rétablir** : restaurer, tirer les leçons, s'améliorer.

La version 2.0 (2024) ajoute une sixième fonction, **Gouverner**, qui encadre les cinq autres.

## Indicateurs de reprise

| Indicateur | Signification |
|---|---|
| **MTTD** | Mean Time To Detect : temps moyen pour détecter un incident |
| **MTD** | Maximum Tolerable Downtime : durée d'arrêt maximale supportable |
| **RPO** | Recovery Point Objective : quantité de données qu'on accepte de perdre (depuis la dernière sauvegarde) |
| **RTO** | Recovery Time Objective : délai visé pour redémarrer |
| **WRT** | Work Recovery Time : temps pour vérifier et relancer les services après la restauration |
| **MTBF** | Mean Time Between Failures : temps moyen entre deux pannes |

Disponibilité en « neuf » : « cinq neuf » = 99,999 % de disponibilité, soit environ 5 minutes d'arrêt par an.

## Noter les vulnérabilités

- **CVE** (Common Vulnerabilities and Exposures) : identifiant unique d'une vulnérabilité publique, par exemple `CVE-2021-44228` (Log4Shell).
- **CVSS** (Common Vulnerability Scoring System) : note de gravité de 0 à 10.
- **NVD** (National Vulnerability Database) : base qui publie les CVE avec leur note CVSS.

## PKI (Public Key Infrastructure)

L'ensemble qui rend le chiffrement d'Internet digne de confiance :

- **CA** : émet les certificats ;
- **RA** (Registration Authority) : vérifie l'identité du demandeur avant l'émission ;
- **certificats numériques** : prouvent l'identité d'un site, d'une personne ou d'un appareil ;
- **paires de clés** publique et privée ;
- **OCSP et CRL** : révocation.

Normes **PKCS** (Public Key Cryptography Standards, de RSA Labs) à connaître :

| Norme | Rôle |
|---|---|
| PKCS #1 | Chiffrement et signature RSA |
| PKCS #7 | Messages signés ou chiffrés (base de S/MIME) |
| PKCS #10 | Demande de certificat (CSR) envoyée à une CA |
| PKCS #12 | Fichier `.pfx` / `.p12` qui contient clé privée et certificat |

### Monter sa propre CA interne

1. Générer une **CA racine** : une clé privée et un certificat autosigné.
2. **Installer le certificat racine** sur toutes les machines, pour qu'elles fassent confiance à cette CA.
3. Pour chaque serveur (par exemple `web.entreprise.local`), générer une **CSR** et la signer avec la CA.
4. Installer les certificats sur les serveurs (HTTPS, VPN...).

Outils : **AD CS** (Active Directory Certificate Services) sous Windows, **OpenSSL** ou **EasyRSA** sous Linux.

## Organisation de la sécurité en entreprise

| Équipe | Rôle |
|---|---|
| **NOC** (Network Operations Center) | Disponibilité et performances du réseau |
| **SOC** (Security Operations Center) | Surveillance des menaces et des incidents |
| **CIRT** (Computer Incident Response Team) | Réponse aux incidents et reprise |

- **RSSI** : Responsable de la Sécurité des Systèmes d'Information (CISO en anglais).
- **AUP** (Acceptable Use Policy) : règles d'utilisation du système d'information.
- **ISO 27001** : norme de management de la sécurité de l'information.
- **Gestion des changements** : processus encadré pour modifier une configuration ou appliquer une mise à jour sans casser la production.
- **M-of-N** : une action sensible demande l'accord de M personnes parmi N (par exemple 2 sur 3 pour restaurer une clé).
- **Surface d'attaque** : tout ce qui peut être attaqué. On cherche toujours à la réduire.

## Notes diverses

- **CPU et sécurité** : le chiffrement consomme du calcul ; les processeurs modernes ont des instructions dédiées (Intel AES-NI). Des failles matérielles comme **Meltdown** et **Spectre** permettent de lire la mémoire d'autres processus.
- **Matériel impossible à corriger** : certaines failles physiques n'ont pas de correctif logiciel ; il faut remplacer le matériel.
- **Hyperviseurs** : type 1 (*bare metal*) : matériel, hyperviseur, machines virtuelles. Type 2 : matériel, système d'exploitation, hyperviseur, machines virtuelles (VirtualBox, VMware Workstation).
- **Wi-Fi** : le **SSID** est le nom du réseau ; le **handover** est le passage d'un point d'accès à un autre sans couper la connexion.
