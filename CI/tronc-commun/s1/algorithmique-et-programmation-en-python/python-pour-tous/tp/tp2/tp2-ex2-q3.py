print("Donner un caractère entre 1 et 5")
n=int(input())
match n:
    case 1:
        print("Un")
    case 2:
        print("Deux")
    case 3:
        print("Trois")
    case 4:
        print("Quatre")
    case 5:
        print("Cinq")
    case _:
        print("Chiffre non supporté")