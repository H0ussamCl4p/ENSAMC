# Résumé Linux

## Système de fichiers

### Types de chemins

| Type | Exemple | Explication |
|---|---|---|
| Absolu | `/home/user/docs` | Commence par `/`, part de la racine |
| Relatif | `../images`, `etc/config` | Part du répertoire courant |
| Répertoire personnel | `~`, `/home/user` | Dossier de l'utilisateur |

### Commandes de base

| Action | Commande |
|---|---|
| Lister les fichiers | `ls`, `ls -l`, `ls -a` |
| Changer de dossier | `cd /chemin`, `cd ~`, `cd ..` |
| Créer un dossier | `mkdir nom`, `mkdir -p rep1/rep2` |
| Supprimer | `rm fichier`, `rm *.txt`, `rm -r rep` |
| Copier | `cp src dest`, `cp -r rep1 rep2` |
| Déplacer ou renommer | `mv src dest` |
| Voir le contenu | `cat`, `more`, `less`, `head`, `tail` |
| Chercher un fichier | `find . -name "*.txt"` |

## Droits et permissions

### Lecture de `ls -l`

```
-rwxr--r--
```

- 1er caractère : le type (`-` fichier, `d` dossier, `l` lien).
- Puis 3 groupes de 3 : propriétaire (owner), groupe (group), autres (others).

### Valeurs numériques

| Droit | Valeur |
|---|---|
| r (lecture) | 4 |
| w (écriture) | 2 |
| x (exécution) | 1 |

Exemple : `chmod 754 fichier` donne propriétaire = 7 (4+2+1), groupe = 5 (4+1), autres = 4.

### Commandes

| Action | Commande |
|---|---|
| Modifier les droits | `chmod 755 fichier`, `chmod u+x fichier` |
| Modifier le propriétaire | `chown user fichier` |
| Modifier le groupe | `chgrp groupe fichier` |
| Voir le numéro d'inode | `ls -i fichier` |

### Umask

Le umask indique les droits à **retirer** à la création :

- dossier : droits de départ `777`, moins les bits du umask ;
- fichier : droits de départ `666`, moins les bits du umask.

Exemple : `umask 027` donne `640` pour un fichier et `750` pour un dossier.

Attention, c'est un retrait de bits, pas une vraie soustraction : avec `umask 033`, un fichier obtient `644` (et non `633`), car le bit x n'existait pas au départ.

## Processus

- `systemd` (init) est le premier processus lancé : PID 1.
- Chaque processus a un PID, un parent (PPID) et un état : R (en cours), S (en attente), T (stoppé), Z (zombie).

| Action | Commande |
|---|---|
| Lister les processus | `ps aux`, `top`, `htop` |
| Lancer en arrière-plan | `commande &` |
| Suspendre | `Ctrl+Z` |
| Reprendre | `bg` (arrière-plan), `fg` (premier plan) |
| Voir les tâches du shell | `jobs` |
| Terminer | `kill PID`, `kill -9 PID` |

## Redirections et pipes

| Action | Symbole | Exemple |
|---|---|---|
| Écrire dans un fichier (écrase) | `>` | `ls > f1` |
| Ajouter à la fin d'un fichier | `>>` | `echo hi >> f1` |
| Lire depuis un fichier | `<` | `sort < f1` |
| Rediriger les erreurs | `2>` | `cmd 2> err.txt` |

Le pipe envoie la sortie d'une commande vers l'entrée de la suivante :

```bash
ls -l | wc -l               # nombre de lignes affichées par ls -l
cat /etc/passwd | grep bash # utilisateurs dont le shell est bash
```

## Expressions régulières (grep)

| Expression | Signification |
|---|---|
| `^mot` | Ligne qui commence par `mot` |
| `mot$` | Ligne qui finit par `mot` |
| `.` | Un caractère quelconque |
| `*` | Le caractère précédent, 0 fois ou plus |
| `[a-z]` | Un caractère de la plage |
| `[^e]` | Tout caractère sauf `e` |

Exemples :

```bash
grep '^A' fichier          # lignes qui commencent par A
grep -E 'ERROR|WARN' log   # OU logique (avec -E)
grep -c 'root' /etc/passwd # nombre de lignes trouvées
```

## Utilisateurs et groupes

| Action | Commande |
|---|---|
| Ajouter un utilisateur | `sudo useradd nom` |
| Supprimer un utilisateur | `sudo userdel nom` |
| Changer un mot de passe | `sudo passwd nom` |
| Verrouiller un compte | `sudo passwd -l nom` |
| Créer un groupe | `sudo groupadd grp` |
| Ajouter un utilisateur à un groupe | `sudo usermod -aG grp user` |

Fichiers importants :

- `/etc/passwd` : informations sur les utilisateurs ;
- `/etc/group` : informations sur les groupes ;
- `/etc/shadow` : mots de passe chiffrés (lisible seulement par root).

## À savoir pour l'examen

- Manipuler fichiers et répertoires.
- Calculer et appliquer les permissions (`chmod`, `umask`).
- Gérer les processus (`ps`, `top`, `bg`, `fg`, `kill`).
- Utiliser pipes et redirections avec `grep`, `find`, `wc`, `sort`.
- Gérer utilisateurs et groupes.
- Écrire des expressions régulières simples.
