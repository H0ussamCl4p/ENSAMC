# Commandes et outils

## Commandes de diagnostic

```bash
nslookup ensam-casa.ma   # adresse IP d'un nom de domaine (DNS)
ping ensam-casa.ma       # tester si une machine répond (ICMP)
tracert ensam-casa.ma    # routeurs traversés (traceroute sous Linux)
ipconfig /all            # configuration IP et adresse MAC (Windows ; ip a sous Linux)
netstat -a               # connexions et ports en écoute
netstat -ab              # idem avec le programme de chaque connexion (Windows, en administrateur)
```

## Cisco IOS

| Invite | Mode | Pour y entrer |
|---|---|---|
| `Router>` | Utilisateur | Mode de départ |
| `Router#` | Privilégié | `enable` |
| `Router(config)#` | Configuration globale | `configure terminal` |

- Découvrir les équipements voisins : **CDP** (Cisco Discovery Protocol) ou **LLDP** (son équivalent standard).
- Configurer un routeur neuf sans adresse IP : **câble console** (port série DB9 ou adaptateur USB) et un terminal comme **PuTTY**.
- Une interface de routeur correspond à un port physique.
- Dans la table de routage, `C` désigne un réseau directement connecté.

## Câblage

| Liaison | Câble |
|---|---|
| Deux équipements de même type (PC à PC, switch à switch) | Croisé |
| Deux équipements de types différents (PC à switch, switch à routeur) | Droit |

La plupart des équipements récents détectent le type de câble tout seuls (Auto-MDIX).

## Logiciels utilisés en TP

- **Cisco Packet Tracer** : simulateur de réseau.
- **Wireshark** : capture et analyse de trafic.
- **EdrawMax** : schémas de réseau.
- **Parrot OS** ou **Kali Linux** (avec Metasploit) comme machine attaquante, et **Metasploitable**, une machine virtuelle volontairement vulnérable, comme cible. Toujours dans un réseau virtuel isolé.
