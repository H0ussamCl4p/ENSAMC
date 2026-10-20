# Attaques, tests d'intrusion et forensic

## Les attaquants

| Type | Description |
|---|---|
| **APT** | Groupe persistant et discret, souvent soutenu par un État, qui reste longtemps dans un réseau |
| **Hackers** | Attaquants compétents, éthiques (*white hat*) ou malveillants (*black hat*) |
| **Script kiddies** | Peu compétents, utilisent des outils tout faits |
| **Hacktivistes** | Motivations politiques ou idéologiques |
| **Menace interne** | Employé ou prestataire qui abuse de ses accès |

## Logiciels malveillants

- **Virus** : a besoin d'être lancé (il s'exécute avec un fichier), se recopie et porte une **charge utile** (*payload*), l'action malveillante.
- **Ver** (*worm*) : se propage seul par le réseau, sans action de l'utilisateur. Il peut installer une bombe logique, une porte dérobée ou un RAT.
- **Bombe logique** : code qui se déclenche à une condition (une date, la suppression d'un compte).
- **Porte dérobée** (*backdoor*) : accès caché qui contourne l'authentification. Elle ouvre en général une connexion **sortante** vers l'attaquant, que beaucoup de pare-feu laissent passer.
- **RAT** (Remote Access Trojan) : cheval de Troie qui donne à l'attaquant le contrôle à distance de la machine.
- **C2** (Command and Control) : le canal par lequel l'attaquant envoie ses ordres aux machines infectées.

### En TP : comprendre une porte dérobée

Avec `msfvenom` (Metasploit), dans le labo isolé :

- `LHOST` : adresse IP de l'attaquant, que la victime va contacter ;
- `LPORT` : port d'écoute de l'attaquant (443 par exemple, pour se fondre dans le trafic HTTPS) ;
- `-p` : la charge utile, adaptée au système de la cible (par exemple `windows/meterpreter/reverse_tcp`) ;
- `-x` : un exécutable légitime qui sert de modèle ;
- `-k` : garde le comportement normal du modèle et lance la charge à part.

Les **encodeurs polymorphes** changent la signature du fichier à chaque génération, ce qui explique pourquoi un antivirus basé seulement sur les signatures ne suffit pas.

## Ingénierie sociale

- **Hameçonnage** (*phishing*) : faux mails ou faux sites pour voler des identifiants.
- **Fouille de poubelles** (*dumpster diving*) : chercher des informations dans les documents jetés.
- **Prétexte, appât, talonnage** (*pretexting, baiting, tailgating*) : inventer une histoire, laisser traîner une clé USB piégée, entrer derrière un employé.

## Attaques réseau et Wi-Fi

| Attaque | Description |
|---|---|
| **Point d'accès pirate** (*rogue AP*) | Borne Wi-Fi non autorisée branchée dans le réseau |
| **Evil twin** | Faux point d'accès qui imite un vrai pour intercepter le trafic |
| **Menace interne** | Personne autorisée qui installe un malware ou vole des données |
| **Bombe logique** | Code malveillant déclenché par une condition |
| **APT** | Campagne longue et discrète (exemples attribués à des États : l'attaque contre Sony Pictures en 2014, WannaCry en 2017) |

## Attaques par force brute

1. **Exhaustive** : essayer toutes les combinaisons. Garanti mais lent, seulement pour de petits espaces (codes PIN, mots de passe courts).
2. **Dictionnaire** : essayer les mots d'une liste plutôt que toutes les combinaisons.
3. **Hybride** : dictionnaire plus variations (chiffres ajoutés, lettres remplacées).
4. **Credential stuffing** : réutiliser des listes de couples identifiant / mot de passe volés sur d'autres sites. Ça marche parce que les gens réutilisent leurs mots de passe.
5. **Pulvérisation** (*password spraying*, force brute inversée) : essayer un mot de passe courant sur beaucoup de comptes, pour éviter le blocage après plusieurs échecs.

En TP, l'outil `crunch` génère une liste de mots de passe à partir d'un jeu de caractères :

```bash
crunch 4 6 abc123 -o liste.txt   # tous les mots de 4 à 6 caractères pris dans "abc123"
```

Protections : mots de passe longs, blocage ou ralentissement après plusieurs échecs, authentification à plusieurs facteurs.

## Tests d'intrusion

**Fenêtre de maintenance** : période convenue pendant laquelle les tests sont autorisés. Les personnes concernées doivent être prévenues : SOC, fournisseur d'accès, fournisseur cloud. Sans accord préalable, un fournisseur cloud peut prendre les tests pour une vraie attaque et suspendre le compte.

Selon les informations données aux testeurs :

- **boîte noire** (*zero knowledge*) : aucune information, aucun identifiant. Le plus réaliste, mais long et cher ;
- **boîte grise** (*partial knowledge*) : quelques informations ou un compte simple ;
- **boîte blanche** (*full knowledge*) : accès complet, identifiants et documentation.

Les **outils d'évaluation des vulnérabilités** listent les failles. Pour vérifier qu'elles sont vraiment exploitables, on passe à la **simulation d'attaques** (**BAS**, Breach and Attack Simulation) ou à l'émulation d'adversaire : MITRE Caldera et Atomic Red Team (open source) ; Armitage et Cobalt Strike servent à piloter des attaques lors d'exercices red team.

## Sauvegardes et alimentation

- **Complète** : copie de tout.
- **Incrémentale** : ce qui a changé depuis la **dernière sauvegarde**, quelle qu'elle soit. Rapide, mais la restauration demande toute la chaîne.
- **Différentielle** : ce qui a changé depuis la **dernière sauvegarde complète**. Restauration avec seulement deux sauvegardes.
- **PDU** (Power Distribution Unit) : répartit l'alimentation entre les équipements d'une baie.
- **Onduleur** (UPS) : garde les serveurs allumés pendant une coupure de courant.

## Forensic

- **IOC** (Indicator of Compromise) : trace qui montre qu'une intrusion **a déjà eu lieu** (adresse IP malveillante, empreinte de fichier, nom de fichier suspect). On les cherche dans les journaux, les outils XDR et les **SIEM**.
- **CTI** (Cyber Threat Intelligence) : collecter et analyser les informations sur les menaces et les attaquants pour anticiper et mieux se défendre.

### 1. Le cadre légal

- Vérifier qu'on a le **droit** de collecter les preuves (mandat, consentement, politique de l'entreprise). Une preuve mal collectée peut être refusée devant un tribunal.
- **Chaîne de possession** (*chain of custody*) : noter qui a collecté quoi, quand, comment, et où la preuve a été stockée ou transmise. Sacs scellés et registres.

### 2. Ne jamais travailler sur l'original

- Faire une **image forensique** (copie bit à bit) et travailler sur la copie.
- Utiliser un **bloqueur d'écriture** pour ne rien modifier sur le support d'origine. Le bloqueur matériel, placé entre le poste d'analyse et le disque, est préférable aux précautions logicielles.

### 3. Outils de copie

- **dcfldd** et **dc3dd** : versions forensiques de `dd`, qui calculent les empreintes pendant la copie et journalisent tout.
- **dd** : l'outil Unix classique ; il faut alors calculer les empreintes à part.
- **FTK Imager** : outil graphique (Windows) pour créer et prévisualiser des images, avec leurs empreintes.

### 4. La mémoire vive

La RAM contient les processus en cours, des clés déchiffrées, des identifiants et les connexions réseau. Elle doit être capturée **avant** d'éteindre ou de redémarrer la machine.

- Capture : **LiME** (Linux), **WinPMEM**, **Magnet RAM Capture**, **Belkasoft RAM Capturer** (Windows).
- Analyse : **Volatility**.

### 5. Machine encore allumée

Relever, avec des outils de confiance, en notant l'heure et chaque commande : processus et services, connexions et ports ouverts, utilisateurs connectés, configuration réseau (routes, table ARP).

```bash
ps aux        # processus
ss -tunap     # connexions (netstat sous Windows)
lsof -i       # fichiers et ports ouverts par les processus
ip a          # configuration réseau
```

### 6. Analyse

| Besoin | Outils |
|---|---|
| Système de fichiers | Autopsy / The Sleuth Kit, EnCase, FTK |
| Mémoire | Volatility |
| Journaux, détection | SIEM : Wazuh (open source), Splunk, ELK (Elasticsearch, Logstash, Kibana) |
| Rétro-ingénierie, malwares | Ghidra, IDA Pro, x64dbg, Radare2 |

### 7. Rapport

Tout noter : ce qui a été collecté et comment, la chaîne de possession, les outils et leurs versions, les commandes, les horaires (en UTC). Le rapport donne les preuves, une chronologie, les IOC et les mesures recommandées.

### Déroulé type

1. Vérifier l'autorisation.
2. Photographier les lieux et les appareils (étiquettes, câbles, écrans).
3. Si la machine est allumée : relever la configuration réseau et les processus, capturer la RAM.
4. Isoler du réseau ou éteindre proprement, brancher un bloqueur d'écriture, faire l'image disque en calculant les empreintes (SHA-256).
5. Mettre les originaux en sécurité, analyser les copies, tout documenter.

## Outils de veille et d'analyse

- **Cartes des cybermenaces** (Cyber Threat Map) : attaques visibles en temps réel, par exemple celle de Radware.
- **OSINT** (Open Source Intelligence) : informations publiques. **Shodan** recense les appareils connectés à Internet ; **Whois** donne le propriétaire d'un nom de domaine.
- **VirusTotal** : analyse un fichier ou une URL avec des dizaines d'antivirus.
- **Wazuh** : SIEM et XDR open source (collecte des journaux, détection, réponse).
- **browser.lol** : navigateur jetable en ligne pour ouvrir une page suspecte sans risque pour sa machine.
