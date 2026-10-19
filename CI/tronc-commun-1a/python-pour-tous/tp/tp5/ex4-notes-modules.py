"""TP5 ex4 : notes par module, moyenne, meilleure note, modules validés et à rattraper."""

def saisie_donnees():
    modules = ["Mathématiques", "Physique", "Français", "Informatique"]
    notes = {}
    for module in modules:
        while True:
            try:
                note = float(input(f"Entrez la note du module de {module} : "))
                notes[module] = note
                break
            except ValueError:
                print("Erreur : Veuillez saisir un nombre valide.")
    return notes

def calcul_moyenne(notes):
    return sum(notes.values()) / len(notes)

def note_max(notes):
    return max(notes, key=notes.get), max(notes.values())

def modules_valide(notes):
    modules = [module for module, note in notes.items() if note >= 10]
    return modules

def modules_non_valide(notes):
    modules = [module for module, note in notes.items() if note < 10]
    if modules:
        print("Modules à rattraper :")
        for module in modules:
            points_manquants = 10 - notes[module]
            print(f"- {module} : {points_manquants:.2f} points manquants")
    else:
        print("Tous les modules sont validés.")


notes = saisie_donnees()
print(notes)
print("Moyenne des notes :", calcul_moyenne(notes))
print("La note maximale est : ", note_max(notes))
print("Le module valide est : ", modules_valide(notes))
modules_non_valide(notes)
