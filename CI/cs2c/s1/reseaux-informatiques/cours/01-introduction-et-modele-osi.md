# Introduction et modèle OSI

## La filière en bref

**Cybersécurité (CS)**, les grands domaines :

- **Red team** (sécurité offensive) : attaquer pour trouver les failles.
- **Blue team** (sécurité défensive) : pare-feu, Zero Trust, forensic.
- **Purple team** : red et blue team qui travaillent ensemble.
- **SOC** (Security Operations Center) : surveiller et analyser les événements de sécurité.
- **Cryptographie**, en particulier la PKI (Public Key Infrastructure).
- **Réseaux** (dont le SD-WAN) et **droit** du numérique.
- **APT** (Advanced Persistent Threat) : groupes d'attaquants persistants, souvent financés par un État.

**Cloud computing (CC)** :

- **Pay as you go** : on paie ce que l'on consomme.
- Architecture cloud et fondations cloud.
- **Virtualisation** : Proxmox, VMware vSphere.
- **DevOps** : développement et exploitation réunis.
- **CAPEX / OPEX** : le cloud transforme des investissements (CAPEX : serveurs, salles) en dépenses de fonctionnement (OPEX : abonnement mensuel).

## Un peu d'histoire

- **ARPANET** (années 1960, financé par la DARPA) : le premier réseau, pour échanger des informations entre laboratoires.
- Années 1980 : il devient Internet. Problème : des machines de constructeurs différents doivent se comprendre (**interopérabilité**).
- Solution : la **normalisation**. L'ISO publie le **modèle OSI**, un modèle de référence qui décrit comment l'information passe de la source à la destination.

**Définition.** Un réseau informatique est un ensemble d'équipements finaux et intermédiaires, reliés par des supports physiques ou sans fil, afin de partager des informations.

**Types de réseaux** selon la zone couverte : LAN (local : maison, salle), MAN (une ville), WAN (des pays, Internet).

## Le modèle OSI

| Couche | Nom | Rôle | Unité | Exemples |
|---|---|---|---|---|
| 7 | Application | Services réseau pour les logiciels | Données | HTTP, SMTP, POP3/IMAP, DNS |
| 6 | Présentation | Encodage, compression, chiffrement | Données | UTF-8, JPEG, TLS |
| 5 | Session | Ouvrir, maintenir et fermer les échanges | Données | RPC, NetBIOS |
| 4 | Transport | Segmentation, transport de bout en bout | Segment | TCP, UDP |
| 3 | Réseau | Adressage logique et routage | Paquet | IPv4, IPv6, ICMP |
| 2 | Liaison | Trames, adresses MAC | Trame | Ethernet, Wi-Fi |
| 1 | Physique | Transmission des bits | Bit | Câbles, fibre, radio |

### Couche 7 : application

L'interface entre l'utilisateur et le réseau. Chaque service a son protocole : le navigateur utilise HTTP, la messagerie SMTP pour l'envoi et POP3 ou IMAP pour la réception, la résolution de noms DNS (`nslookup ensam-casa.ma` affiche l'adresse IP d'un nom).

C'est l'application qui choisit le protocole de transport (TCP ou UDP).

### Couche 6 : présentation

Codage et décodage des données (codecs), compression et chiffrement, pour que les deux machines interprètent les données de la même façon.

### Couche 5 : session

Ouvre un canal pour chaque communication, le maintient et le ferme. Exemple : une session RPC, ou un appel vidéo qui garde la même session pendant toute la conversation.

### Couche 4 : transport

Rôles : segmenter les données, les numéroter (séquençage), accuser réception (acknowledgment), retransmettre les pertes, contrôler le flux (fenêtrage, *windowing*).

**TCP, fiable.** La connexion commence par le *3-way handshake* :

1. le client envoie `SYN` (numéro de séquence x) ;
2. le serveur répond `SYN-ACK` (séquence y, acquittement x + 1) ;
3. le client confirme `ACK` (acquittement y + 1).

Ensuite, chaque acquittement vaut **numéro de séquence reçu + nombre d'octets reçus** : il annonce le prochain octet attendu. Si un segment se perd, il est retransmis.

**UDP, non fiable.** Pas de connexion, pas d'accusé de réception : plus rapide. Utilisé quand la vitesse compte plus que la perte d'un paquet : DNS, voix sur IP, streaming, jeux, et QUIC (la base de HTTP/3).

**VoIP** (Voice over IP) : la voix est découpée en paquets envoyés sur Internet (WhatsApp, Teams, Meet, téléphones IP d'entreprise). Elle utilise RTP au-dessus d'UDP. Moins chère que la téléphonie classique, mais elle demande une connexion stable et doit être sécurisée.

### Attaques liées au transport

- **SYN flood** (attaque par connexions à moitié ouvertes) : l'attaquant envoie beaucoup de `SYN`, souvent avec de fausses adresses IP sources (**IP spoofing**), et ne termine jamais le handshake. Le serveur réserve de la mémoire pour chaque connexion en attente jusqu'à saturer : c'est un **déni de service (DoS)**. Protections : SYN cookies, limitation du nombre de connexions, pare-feu ou proxy devant le serveur, flux de renseignement sur les menaces (*threat feeds*).
- **Man in the middle** : l'attaquant se place entre deux machines et se fait passer pour l'autre.
- **Détournement de session** (*session hijacking*) : prendre le contrôle d'une connexion TCP déjà ouverte. C'est difficile, car il faut deviner les numéros de séquence.

### Couche 3 : réseau

Le segment est mis dans une « enveloppe » : le **paquet**, avec un en-tête qui contient les adresses IP source et destination. La couche réseau s'occupe de l'**adressage** et du **routage** (choisir le chemin). Détails dans [Adressage IP](03-adressage-ip.md) et [Routage](04-routage.md).

### Couche 2 : liaison de données

Le paquet est mis dans une **trame** avec les adresses MAC. Deux sous-couches :

- **MAC** (Media Access Control) : accès au support et adressage physique.
- **LLC** (Logical Link Control) : indique à quel protocole appartiennent les données (IP, ARP...).

**Adresse MAC** : identifiant de 48 bits de la carte réseau, par exemple `00-1A-2B-3C-4D-5E`.

- Les 24 premiers bits (3 octets) forment l'**OUI** et identifient le fabricant. On le retrouve sur un site de recherche « MAC lookup » (par exemple [dnschecker.org/mac-lookup.php](https://dnschecker.org/mac-lookup.php)).
- Les 24 bits suivants sont propres à la carte.
- L'adresse MAC ne sert qu'à l'intérieur du réseau local : elle ne traverse pas les routeurs.

Voir son adresse MAC : `ipconfig /all` (Windows) ou `ip link` (Linux).

**Usurpation d'adresse MAC** (*MAC spoofing*) : l'adresse est gravée dans la carte, mais le système peut en annoncer une autre très facilement :

```bash
sudo ip link set ens33 down        # toujours désactiver la carte avant
sudo ip link set ens33 address 02:11:22:33:44:55
sudo ip link set ens33 up
```

Conséquence : le **filtrage par adresse MAC** protège mal. La bonne solution est **IEEE 802.1X** : chaque appareil doit s'authentifier avant d'accéder au réseau.

### Couche 1 : physique

Transmission des bits bruts sur un support :

- **supports** : câbles Ethernet (Cat5e, Cat6), fibre optique, coaxial, ondes radio ;
- **codage du signal** : tension électrique, impulsions lumineuses, ondes ;
- **débit** (1 Gbit/s, 10 Gbit/s...) et **synchronisation** entre émetteur et récepteur ;
- **topologie** : étoile, bus, anneau, maillée ;
- **caractéristiques physiques** : connecteurs (RJ45), brochage, niveaux de tension.

Équipements de couche 1 : hubs, répéteurs, cartes réseau, câbles et connecteurs.

**Brouillage** (*signal jamming*) : émettre volontairement un signal radio qui couvre les signaux légitimes (Wi-Fi, GPS, téléphone) pour bloquer les communications sans fil.
