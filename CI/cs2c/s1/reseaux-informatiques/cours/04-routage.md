# Routage

Le **routage** permet :

- d'apprendre les **destinations** et les **chemins** pour les atteindre ;
- d'envoyer le trafic par le **meilleur chemin**.

Le « coût » d'une route (la **métrique**) dépend du protocole : nombre de sauts, débit, délai, charge...

Deux familles : le routage **statique** et le routage **dynamique**.

## Routage statique

L'administrateur saisit **à la main** chaque route.

| Avantages | Inconvénients |
|---|---|
| Sécurité : aucun échange de routes entre routeurs | Convergence lente : tout changement est à refaire à la main |
| Économie de bande passante : pas de messages de protocole | Difficile à maintenir quand le réseau grandit (le plus gros défaut) |

Pour une destination, on indique soit :

- l'**interface de sortie** (« sortir par... »), peu adapté si plusieurs réseaux passent par la même interface ;
- l'**adresse du routeur suivant** (« sortir vers... »), en général le meilleur choix.

Il faut aussi configurer la **route de retour** sur l'autre routeur.

### Plusieurs chemins : répartition de charge

S'il existe plusieurs routes valides vers la même destination, on les déclare toutes. Avec **ECMP** (Equal-Cost Multi-Path), le routeur partage le trafic entre les routes de **même coût**. La répartition peut se faire selon l'IP source, l'IP destination, un poids, le volume ou le débit (débordement).

### Choisir une route : la distance administrative

Quand plusieurs sources proposent une route vers la même destination, le routeur garde celle qui a la plus petite **distance administrative (AD)** :

| Source de la route | AD |
|---|---|
| Réseau directement connecté (noté `C`) | 0 |
| Route statique | 1 |
| eBGP | 20 |
| EIGRP | 90 |
| OSPF | 110 |
| RIP | 120 |

Pour faire d'une route statique une route **de secours**, on lui donne une AD plus grande (par exemple 5) : elle ne sert que si la route principale disparaît.

### Route par défaut

```
ip route 0.0.0.0 0.0.0.0 <routeur suivant ou interface de sortie>
```

Tout le trafic vers une destination inconnue part vers la **passerelle par défaut** (`0.0.0.0/0`). C'est le cas d'un téléphone : téléphone, puis box, puis passerelle du FAI.

## Routage dynamique

Les routeurs **apprennent et mettent à jour** les routes eux-mêmes grâce à des protocoles de routage. Si les mises à jour s'arrêtent, c'est en général que le lien ou le protocole est tombé.

| Avantages | Inconvénients |
|---|---|
| S'adapte seul aux changements | Peut être attaqué (fausses annonces de routes) |

### Systèmes autonomes

Pour limiter les mises à jour, Internet est découpé en **systèmes autonomes (AS)**, des blocs gérés indépendamment.

- **IGP** (Interior Gateway Protocol) : à l'intérieur d'un AS (RIP, OSPF, EIGRP, IS-IS).
- **EGP** (Exterior Gateway Protocol) : entre AS. Aujourd'hui c'est **BGP**.

### Les protocoles

| Protocole | Type | Métrique | Usage |
|---|---|---|---|
| RIP | Vecteur de distance | Nombre de sauts (15 max) | Petits réseaux, ancien |
| OSPF | État de liens | Coût, calculé à partir du débit | Réseaux d'entreprise |
| EIGRP | Vecteur de distance avancé (Cisco) | Débit, délai, charge, fiabilité | Réseaux Cisco |
| IS-IS | État de liens | Coût | Grands opérateurs |
| BGP | Vecteur de chemin | Attributs de chemin | Entre FAI, routage d'Internet |

## RIP (vecteur de distance)

- Chaque routeur envoie **périodiquement** (toutes les 30 s) toute sa table à ses voisins.
- Chaque routeur traversé ajoute 1 saut ; on garde le chemin avec le moins de sauts. À égalité, on répartit la charge.
- Algorithme de **Bellman-Ford**. AD 120, messages sur **UDP port 520**.

Versions :

- **RIP v1** : *classful*, diffusion (broadcast), pas de masque dans les annonces, pas d'authentification.
- **RIP v2** : *classless* (transporte les masques, donc VLSM et CIDR possibles), multicast, authentification (dont MD5).

Limites :

- 15 sauts maximum (16 = inaccessible) ;
- aucune vue de la topologie, pas de table des voisins, donc risque de **boucles** et de trous noirs ;
- de fausses annonces peuvent détourner le trafic si l'authentification n'est pas activée.

Minuteurs contre les boucles :

- **hold-down** (180 s) : après la perte d'une route, le routeur ignore pendant ce temps les annonces moins bonnes pour cette destination ;
- **flush** (240 s) : la route est finalement supprimée de la table.

Le champ **TTL** du paquet IP limite aussi la durée de vie d'un paquet pris dans une boucle.

## OSPF (état de liens)

- Métrique : le **coût**, calculé à partir du débit des liens.
- Le routeur découvre d'abord ses **voisins** (table des voisins), puis échange l'état des liens et construit une carte complète du réseau. Il calcule les meilleurs chemins avec l'algorithme de **Dijkstra**.
- Pas de boucles, convergence rapide. AD 110.

### Aires

- Le réseau est découpé en **aires**. L'**aire 0** (*backbone*) relie toutes les autres.
- Deux aires standard ne communiquent qu'en passant par l'aire 0. Un **lien virtuel** peut contourner cette règle, mais c'est déconseillé.

### Élection du DR et du BDR

Sur un réseau partagé (Ethernet), les routeurs élisent un **DR** (Designated Router) et un **BDR** (Backup DR). Les autres routeurs échangent leurs informations avec eux plutôt qu'entre tous.

1. La **priorité** la plus haute gagne (1 par défaut ; 0 = ne peut pas être élu).
2. À égalité, le **router ID** le plus haut gagne. C'est un identifiant au format IP (`x.x.x.x`) : choisi à la main, sinon la plus haute adresse de loopback, sinon la plus haute adresse d'interface active.
3. Pour éviter des réélections, on fixe le router ID (de préférence sur une interface **loopback**).
4. Pas d'élection sur les liens point à point.

## Reverse Path Forwarding (RPF)

Le routeur vérifie qu'un paquet arrive par l'interface qu'il utiliserait lui-même pour **répondre à la source**.

- Si oui, le paquet est accepté et transmis.
- Sinon, il est rejeté : boucle possible ou adresse source usurpée.

Usages :

- **multicast** : empêche les paquets de circuler sans fin ;
- **uRPF** (unicast) : protection contre l'usurpation d'adresse IP.
