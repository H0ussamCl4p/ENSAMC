# Adressage IP

## IPv4 et IPv6

| | IPv4 | IPv6 |
|---|---|---|
| Normalisé en | 1981 | 1998 |
| Taille | 32 bits (4 octets) | 128 bits (16 octets) |
| Nombre d'adresses | 2³² ≈ 4,3 milliards | 2¹²⁸ ≈ 3,4 × 10³⁸ |
| Notation | décimale pointée : `192.168.5.18` | hexadécimale : `2001:db8::1` |
| Configuration | manuelle ou DHCP | manuelle, DHCPv6 ou autoconfiguration |

- Les adresses IPv4 libres sont épuisées : l'IANA a distribué ses derniers blocs en 2011, puis les registres régionaux sont tombés à court les uns après les autres.
- IPv6 règle le problème du nombre d'adresses. Il progresse, mais IPv4 reste majoritaire dans beaucoup de réseaux.
- IPv6 n'est pas « sécurisé » par nature : IPsec y a été pensé dès le départ, mais la sécurité dépend de la configuration, comme en IPv4.

## Qui distribue les adresses

1. **IANA** (Internet Assigned Numbers Authority) : coordination mondiale des adresses IP, des numéros de systèmes autonomes (AS) et de la racine DNS. Elle définit aussi les plages privées.
2. **RIR** (Regional Internet Registry), un par région : AFRINIC (Afrique), RIPE NCC (Europe), APNIC (Asie-Pacifique), ARIN, LACNIC.
3. **LIR** (Local Internet Registry) : reçoit des blocs d'un RIR et les attribue à ses clients. Au Maroc, ce sont surtout les opérateurs (Maroc Telecom, inwi, Orange).
4. Les FAI donnent une adresse publique à chaque box.

```
IANA -> RIR -> LIR / FAI -> client
```

**Adresses privées** : réservées par l'IANA pour les réseaux internes, jamais routées sur Internet. Chaque réseau peut réutiliser les mêmes plages sans conflit.

| Plage | Masque |
|---|---|
| `10.0.0.0` à `10.255.255.255` | `/8` |
| `172.16.0.0` à `172.31.255.255` | `/12` |
| `192.168.0.0` à `192.168.255.255` | `/16` |

## NAT

**NAT** (Network Address Translation) : le routeur modifie les adresses IP dans l'en-tête des paquets qui le traversent. Il permet à toutes les machines d'un réseau privé de sortir sur Internet avec **une seule adresse publique**.

- **PAT** (Port Address Translation) : forme de NAT où les connexions sont distinguées par leur numéro de port. C'est ce que fait une box internet.
- **NAT64, NAT46, NAT66** : traduction entre IPv4 et IPv6.

## Adresses particulières

| Adresse | Rôle |
|---|---|
| `255.255.255.255` | Diffusion à tout le réseau local (l'équivalent de `FF:FF:FF:FF:FF:FF` en couche 2) |
| `127.0.0.1` | Boucle locale (*localhost*) : la machine elle-même |
| `169.254.x.x` | APIPA : adresse que la machine se donne quand aucun serveur DHCP ne répond |
| `0.0.0.0` | Adresse non spécifiée ; `0.0.0.0/0` désigne la route par défaut |

## Partie réseau et partie hôte

Une adresse IPv4 a deux parties : le **réseau** et l'**hôte** (la machine). Le **masque** indique où se fait la séparation.

```
IP     : 192.168.1.100
Masque : 255.255.255.0  (/24)
```

Les 24 premiers bits désignent le réseau `192.168.1.0`, les 8 derniers la machine.

- **Adresse réseau** : tous les bits hôte à 0. Elle ne s'attribue pas à une machine.
- **Adresse de diffusion** (broadcast) : tous les bits hôte à 1. Elle ne s'attribue pas non plus.
- **Nombre de machines possibles** : 2^(32 − masque) − 2. Pour un `/24` : 2⁸ − 2 = 254.

### Trouver l'adresse réseau (ET logique)

On fait un ET bit à bit entre l'adresse et le masque.

```
IP     192.168.1.130   11000000.10101000.00000001.10000010
Masque 255.255.255.192 11111111.11111111.11111111.11000000
ET     192.168.1.128   11000000.10101000.00000001.10000000
```

Le réseau est `192.168.1.128/26`. En mettant les 6 bits hôte à 1, on obtient la diffusion `192.168.1.191`. Les machines vont de `.129` à `.190`.

## Découpage en sous-réseaux

### FLSM (Fixed Length Subnet Mask)

Tous les sous-réseaux ont le **même masque**, donc la même taille. Pour n sous-réseaux, on emprunte k bits à la partie hôte, avec 2^k ≥ n. C'est simple, mais on gaspille des adresses si les besoins sont différents.

Exemple : découper `192.168.1.0/24` en 4. On emprunte 2 bits (2² = 4), le masque devient `/26` (`255.255.255.192`) et chaque sous-réseau a 2⁶ − 2 = 62 machines.

| Sous-réseau | Adresse réseau | Machines | Diffusion |
|---|---|---|---|
| 1 | 192.168.1.0/26 | .1 à .62 | .63 |
| 2 | 192.168.1.64/26 | .65 à .126 | .127 |
| 3 | 192.168.1.128/26 | .129 à .190 | .191 |
| 4 | 192.168.1.192/26 | .193 à .254 | .255 |

Vidéo : [FLSM expliqué](https://youtu.be/tJ9yAkEKR1Y).

### VLSM (Variable Length Subnet Mask)

Chaque sous-réseau reçoit **son propre masque**, adapté à son nombre de machines. Méthode : trier les besoins du plus grand au plus petit, puis attribuer les blocs dans cet ordre. Bien choisir ses plages d'adresses au départ évite de tout refaire plus tard.

## DHCP

**DHCP** (Dynamic Host Configuration Protocol) donne automatiquement à chaque machine son adresse IP, son masque, sa passerelle et ses serveurs DNS. Échange en 4 étapes, **DORA** :

1. **Discover** : le client cherche un serveur (en diffusion) ;
2. **Offer** : le serveur propose une adresse ;
3. **Request** : le client demande cette adresse ;
4. **Acknowledge** : le serveur confirme.

Attaques :

- **Faux serveur DHCP** (*rogue DHCP*) : un serveur non autorisé donne une fausse passerelle pour intercepter le trafic. Protection : le **DHCP snooping** sur les switches, qui n'autorise que les serveurs de confiance.
- **Épuisement DHCP** (*DHCP starvation*) : l'attaquant demande toutes les adresses avec de fausses adresses MAC, et les vraies machines n'en obtiennent plus.

## MTU

**MTU** (Maximum Transmission Unit) : taille maximale d'une trame transmise sans découpage, 1500 octets par défaut en Ethernet. Une **jumbo frame** dépasse cette taille (jusqu'à environ 9000 octets) ; tous les équipements du chemin doivent l'accepter.
