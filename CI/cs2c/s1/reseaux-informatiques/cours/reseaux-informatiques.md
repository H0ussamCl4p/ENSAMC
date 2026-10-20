# Réseaux informatiques

## Équipements

| Équipement | Couche OSI | Fonctionnement |
|---|---|---|
| Hub (concentrateur) | 1, physique | Renvoie tout ce qu'il reçoit à tous les ports : collisions et aucune confidentialité |
| Bridge (pont) | 2, liaison | Relie deux segments et filtre le trafic grâce aux adresses MAC |
| Switch (commutateur) | 2, liaison | Pont à plusieurs ports : envoie chaque trame seulement au port du destinataire |
| Router (routeur) | 3, réseau | Relie des réseaux différents et choisit la route selon l'adresse IP |

**Topologie** : la structure d'un réseau (bus, étoile, anneau, maillée...).

**Types de réseaux** selon la zone couverte :

- LAN (Local Area Network) : une maison, une salle, une école ;
- MAN (Metropolitan Area Network) : une ville ;
- WAN (Wide Area Network) : des pays, Internet.

**VPN** (Virtual Private Network) : un tunnel chiffré qui relie un appareil ou un site distant à un réseau privé à travers Internet.

**Brouillage** (signal jamming) : émettre volontairement un signal radio qui couvre les signaux légitimes (Wi-Fi, GPS, téléphone) pour bloquer les communications sans fil.

## Le modèle OSI

| Couche | Nom | Rôle | Exemples |
|---|---|---|---|
| 7 | Application | Services réseau pour les logiciels | HTTP (navigateur), SMTP pour l'envoi de mails, POP3/IMAP pour la réception |
| 6 | Présentation | Encodage, compression, chiffrement | ASCII/UTF-8, JPEG, TLS |
| 5 | Session | Ouvrir, gérer et fermer les sessions | RPC, NetBIOS |
| 4 | Transport | Segmentation, transport de bout en bout | TCP, UDP |
| 3 | Réseau | Adressage logique et routage | IPv4, IPv6, ICMP |
| 2 | Liaison de données | Trames, adressage physique (MAC) | Ethernet, Wi-Fi (802.11) |
| 1 | Physique | Signaux, câbles, connecteurs | RJ45, fibre, ondes radio |

### Couche 4 : transport

Rôles : segmenter et réassembler les données, numéroter les segments (séquençage), accuser réception (acknowledgment), retransmettre les pertes et contrôler le flux.

Deux modes :

- **TCP**, fiable : connexion établie par le *3-way handshake* (SYN, SYN-ACK, ACK), accusés de réception, retransmission. Utilisé par HTTP/1.1 et HTTP/2, SMTP, SSH.
- **UDP**, non fiable : pas de connexion ni d'accusé de réception, donc plus rapide. Utilisé par DNS, la voix sur IP, le streaming, les jeux, et QUIC (la base de HTTP/3).

Attaques liées à cette couche :

- **SYN flood** : l'attaquant envoie beaucoup de SYN sans jamais finir le handshake. Le serveur garde des connexions à moitié ouvertes jusqu'à saturer : c'est un déni de service (DoS), souvent combiné avec de fausses adresses IP sources (IP spoofing).
- **Détournement de session** (session hijacking) : l'attaquant se place entre les deux machines (man in the middle) et prend le contrôle d'une session déjà ouverte.

### Couche 3 : réseau

Adressage et routage avec IP.

| | IPv4 | IPv6 |
|---|---|---|
| Taille d'adresse | 32 bits | 128 bits |
| Nombre d'adresses | environ 4,3 milliards | environ 3,4 × 10³⁸ |
| Notation | décimale pointée : `192.168.5.18` | hexadécimale : `2001:db8::1` |
| Configuration | manuelle ou DHCP | manuelle, DHCPv6 ou autoconfiguration |

Qui distribue les adresses IP :

1. **IANA** (Internet Assigned Numbers Authority) : coordonne au niveau mondial les adresses IP, les numéros de systèmes autonomes (AS) et la racine DNS.
2. **RIR** (Regional Internet Registry), un par région : AFRINIC (Afrique), RIPE NCC (Europe), APNIC (Asie-Pacifique), ARIN, LACNIC.
3. **LIR** (Local Internet Registry) : reçoit des blocs d'un RIR et les attribue à ses clients. Au Maroc ce sont surtout les opérateurs (Maroc Telecom, inwi, Orange).
4. **FAI** (fournisseur d'accès) : donne une adresse publique à chaque box.

**NAT** (Network Address Translation) : la box traduit les adresses privées de la maison vers son adresse IP publique, ce qui permet à tous les appareils d'accéder à Internet avec une seule adresse.
**PAT** (Port Address Translation) : forme de NAT où les connexions sont distinguées par le numéro de port. C'est le cas des box internet.
**NAT64, NAT46, NAT66** : traduction entre IPv4 et IPv6.

### Couche 2 : liaison de données

L'unité de données est la **trame** (frame). Chaque carte réseau a une **adresse MAC** (adresse physique) de 48 bits, par exemple `00-1A-2B-3C-4D-5E`. Les 3 premiers octets forment l'**OUI** et identifient le fabricant : on peut le retrouver sur un site de recherche OUI / MAC lookup (par exemple [dnschecker.org/mac-lookup.php](https://dnschecker.org/mac-lookup.php)).

Voir l'adresse MAC de sa machine :

```bash
ipconfig /all     # Windows
ip link           # Linux
```

**Usurpation d'adresse MAC** (MAC spoofing) : une adresse MAC se change facilement par logiciel. Il faut désactiver la carte réseau avant de la modifier :

```bash
sudo ip link set ens33 down
sudo ip link set ens33 address 02:11:22:33:44:55
sudo ip link set ens33 up
```

Conséquence : le **filtrage par adresse MAC** est une mauvaise protection, car n'importe qui peut prendre l'adresse d'une machine autorisée. La norme **IEEE 802.1X** est la bonne solution : chaque appareil doit s'authentifier avant d'avoir accès au réseau.

Environnement de TP : une machine attaquante (Parrot OS ou Kali Linux, avec Metasploit) et une machine victime volontairement vulnérable (Metasploitable), dans un réseau virtuel isolé.

## Découpage en sous-réseaux

### FLSM (Fixed Length Subnet Mask)

Tous les sous-réseaux utilisent le même masque, donc ils ont tous la même taille. C'est simple, mais on gaspille des adresses quand les besoins sont différents.

Exemple : découper `192.168.1.0/24` en 4 sous-réseaux. On emprunte 2 bits (2² = 4), le masque devient `/26` et chaque sous-réseau a 2⁶ − 2 = 62 hôtes.

| Sous-réseau | Adresse réseau | Hôtes | Broadcast |
|---|---|---|---|
| 1 | 192.168.1.0/26 | .1 à .62 | .63 |
| 2 | 192.168.1.64/26 | .65 à .126 | .127 |
| 3 | 192.168.1.128/26 | .129 à .190 | .191 |
| 4 | 192.168.1.192/26 | .193 à .254 | .255 |

Vidéo : [FLSM expliqué](https://youtu.be/tJ9yAkEKR1Y).

### VLSM (Variable Length Subnet Mask)

Chaque sous-réseau reçoit un masque adapté à son nombre d'hôtes, ce qui évite le gaspillage. Méthode : trier les besoins du plus grand au plus petit, puis attribuer les blocs dans cet ordre.

## Commandes utiles

```bash
nslookup ensam-casa.ma   # adresse IP d'un nom de domaine (DNS)
ping ensam-casa.ma       # tester si une machine répond (ICMP)
netstat -a               # toutes les connexions et ports en écoute
netstat -ab              # idem avec le programme de chaque connexion (Windows, en administrateur)
```
