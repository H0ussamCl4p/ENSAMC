# Fiche de révision : scripts shell des TP

Les commandes utilisées dans les scripts du TP (`analyse_sys.sh`, `utilisateur.sh`, `cleanup.sh`).

## Tests de fichiers

| Test | Vrai si | Exemple |
|---|---|---|
| `[ -f fichier ]` | C'est un fichier régulier | `if [ -f "$fichier" ]` |
| `[ -r fichier ]` | Le fichier est lisible | `if [ -f "$fichier" ] && [ -r "$fichier" ]` |
| `[ -d dossier ]` | C'est un dossier | `if [ -d "$username" ]` |

Toujours vérifier qu'un fichier existe et est lisible avant de le traiter.

## Fichiers et entrées

| Commande | Rôle | Exemple |
|---|---|---|
| `mkdir -p dossier` | Crée un dossier (et ses parents) | `mkdir -p "$username"` |
| `mv source dest` | Renomme ou déplace | `mv "$fichier" "$nouveau_nom"` |
| `echo "texte"` | Affiche du texte | `echo "Nombre de lignes : $nb_lignes"` |
| `read -p "msg" var` | Lit une saisie | `read -p "Nom utilisateur : " username` |

## Boucles et menu

```bash
# Parcourir les fichiers du dossier courant (cleanup.sh)
for fichier in *; do
    echo "$fichier"
done

# Redemander tant que le nom est invalide (utilisateur.sh)
while ! [[ "$username" =~ ^[A-Za-z][A-Za-z0-9]{2,11}$ ]]; do
    read -p "Nom utilisateur : " username
done

# Menu interactif : boucle infinie, on sort avec exit
while true; do
    read -p "Choix : " choix
    case $choix in
        1) echo "Option 1" ;;
        2) echo "Option 2" ;;
        4) exit 0 ;;
        *) echo "Choix invalide" ;;
    esac
done
```

## Regex et extraction de texte

| Commande | Rôle |
|---|---|
| `[[ chaine =~ regex ]]` | Teste si la chaîne correspond à la regex |
| `grep -E "regex"` | Lignes qui correspondent (regex étendue) |
| `grep -Eo "regex"` | Seulement la partie qui correspond |
| `sed 's/ancien/nouveau/g'` | Remplace du texte |
| `wc -l` | Compte les lignes |
| `awk -F: '...'` | Découpe chaque ligne selon `:` |
| `sort` | Trie les lignes |
| `uniq -c` | Supprime les doublons consécutifs et les compte |

Exemples du TP :

```bash
nb_lignes=$(wc -l < "$fichier")

grep -E "ERROR|WARNING" "$LOG"                       # lignes d'erreur
grep -Eo "[A-Z][a-z]+" "$LOG" | sort | uniq -c       # noms et leur nombre
grep -Eo "[0-9]{2}:[0-9]{2}:[0-9]{2}" "$LOG"          # horodatages
awk -F: '$3 >= 1000 {print $1}' /etc/passwd          # utilisateurs normaux (UID >= 1000)

nouveau_nom=$(echo "$fichier" | sed 's/ /_/g')       # espaces remplacés par _
nouveau_nom=$(echo "$nouveau_nom" | sed 's/[^A-Za-z0-9._-]//g')  # caractères interdits supprimés
```

`uniq` ne retire que les doublons **qui se suivent**, d'où le `sort` avant.

## Regex à connaître

| Regex | Correspond à |
|---|---|
| `^[A-Za-z][A-Za-z0-9]{2,11}$` | Nom d'utilisateur : commence par une lettre, 3 à 12 caractères alphanumériques |
| `[^A-Za-z0-9._-]` | Tout caractère interdit dans un nom de fichier |
| `[A-Z][a-z]+` | Un nom (majuscule puis minuscules) |
| `[0-9]{2}:[0-9]{2}:[0-9]{2}` | Une heure `hh:mm:ss` |

## Informations système

```bash
echo "Date : $(date)"
echo "Répertoire : $(pwd)"
echo "Utilisateur : $USER"
```
