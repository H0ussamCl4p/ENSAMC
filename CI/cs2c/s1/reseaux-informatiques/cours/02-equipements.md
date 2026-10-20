# Équipements réseau

| Équipement | Couche | Utilise | Rôle | Relie |
|---|---|---|---|---|
| Hub (concentrateur) | 1 | rien | Renvoie tout à tous les ports | Des machines d'un LAN |
| Bridge (pont) | 2 | MAC | Filtre le trafic entre segments | Des segments d'un LAN |
| Switch (commutateur) | 2 (parfois 3) | MAC (et IP en couche 3) | Envoie chaque trame au bon port | Les machines d'un même réseau |
| Router (routeur) | 3 | IP | Choisit le chemin entre réseaux | Des réseaux différents (LAN et Internet) |

## Hub

Le hub copie chaque signal reçu vers **tous** ses ports. Toutes les machines reçoivent tout, et seule la destinataire traite le message.

- Un seul **domaine de collision** et un seul **domaine de diffusion** pour toutes les machines.
- Types : passif (relie seulement), actif (régénère le signal, comme un répéteur), « intelligent » (quelques fonctions de gestion).

**Gestion des collisions : CSMA/CD** (Carrier Sense Multiple Access with Collision Detection) :

1. chaque machine écoute si le support est libre ;
2. si oui, elle émet ;
3. si deux machines émettent en même temps, elles détectent la collision ;
4. elles envoient un signal de brouillage (*jam*) ;
5. elles attendent un temps aléatoire, puis réessaient.

Plus il y a de machines, plus il y a de collisions et plus le réseau ralentit. En plus, tout le monde voit le trafic des autres. C'est pour cela que les switches ont remplacé les hubs.

Usage restant : brancher un analyseur (Wireshark) sur un hub permet de voir tout le trafic. Aujourd'hui on préfère un **TAP** ou le *port mirroring* d'un switch (voir plus bas).

## Bridge

L'ancêtre du switch. Il relie deux segments d'un LAN et apprend quelles adresses MAC se trouvent de chaque côté :

- destination du même côté : la trame n'est pas transmise ;
- destination de l'autre côté : la trame est transmise.

```
[ Segment A ] <---> [ Bridge ] <---> [ Segment B ]
 PC1    PC2                           PC3    PC4
```

PC1 vers PC2 : la trame reste dans le segment A. PC1 vers PC4 : elle passe le pont. Les machines ne voient pas le pont (*transparent bridging*). Un pont sépare les domaines de collision et peut utiliser STP contre les boucles.

On ne trouve plus de ponts aujourd'hui, mais un switch fonctionne exactement comme un pont à plusieurs ports.

## Switch

Le switch relie les machines d'un LAN et envoie chaque trame **seulement** au port du destinataire :

1. il lit l'adresse MAC de destination de la trame ;
2. il cherche cette adresse dans sa **table MAC** (quelle adresse sur quel port) ;
3. s'il la connaît, il envoie la trame sur ce seul port ;
4. sinon, il l'envoie sur tous les ports (*flooding*) et apprend la réponse pour la prochaine fois.

Chaque port est un domaine de collision séparé. Les **switches de couche 3** savent aussi router avec les adresses IP.

Types : non administrable (*plug and play*, maison), administrable (VLAN, sécurité des ports, supervision, QoS), PoE (alimente caméras et téléphones IP par le câble).

Fonctions importantes :

- **VLAN** : plusieurs réseaux logiques séparés sur le même switch ;
- **port mirroring** : copier le trafic d'un port vers un autre pour l'analyser ;
- **STP** (Spanning Tree Protocol) : empêche les boucles entre switches ;
- **agrégation de liens** : combiner plusieurs ports pour plus de débit.

## Routeur

Le routeur relie des **réseaux différents**, par exemple le réseau de la maison et Internet. Il travaille en couche 3 avec les adresses IP. En résumé : le switch relie des machines, le routeur relie des réseaux.

Pour chaque paquet, il :

1. lit l'adresse IP de destination ;
2. consulte sa **table de routage** (les réseaux connus et le chemin pour les atteindre) ;
3. envoie le paquet au saut suivant (*next hop*).

Exemple :

```
Téléphone -> Wi-Fi -> Box (routeur) -> FAI -> Internet -> Serveur web
```

Types : routeurs de cœur (chez les FAI), routeurs de bordure (entre un réseau interne et l'extérieur), routeurs Wi-Fi (maison), routeurs virtuels (cloud).

Fonctions : routage (RIP, OSPF, BGP...), NAT, DHCP, filtrage (pare-feu), QoS (priorité à certains trafics).

Une box internet réunit en un seul boîtier : routeur, switch, point d'accès Wi-Fi, pare-feu et serveur DHCP.

## TAP (Test Access Point)

Boîtier placé entre deux équipements qui **copie** tout le trafic vers un outil d'analyse, sans le modifier ni le ralentir :

```
Machine A <---> [ TAP ] <---> Switch
                   |
                   +---> Outil d'analyse (Wireshark, IDS)
```

Usages : supervision du trafic, détection d'intrusion (IDS), forensic, recherche de pannes, audit.

Types : passif (cuivre, sans alimentation), actif (fibre, haut débit, alimenté), d'agrégation (plusieurs liens vers une sortie), de régénération (copie vers plusieurs outils).
