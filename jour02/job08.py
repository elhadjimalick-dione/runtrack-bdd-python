import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="azerty",
    database="zoo"
)
cursor = conn.cursor()

def ajouter_animal():
    nom = input("Nom de l'animal : ")
    race = input("Race de l'animal : ")
    cage_id = int(input("ID de la cage : "))
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    pays_origine = input("Pays d'origine : ")

    cursor.execute("INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)",
                   (nom, race, cage_id, date_naissance, pays_origine))
    conn.commit()
    print("Animal ajouté avec succès.")

def supprimer_animal():
    animal_id = int(input("ID de l'animal à supprimer : "))
    cursor.execute("DELETE FROM animal WHERE id=%s", (animal_id,))
    conn.commit()
    print("Animal supprimé avec succès.")

def modifier_animal():
    animal_id = int(input("ID de l'animal à modifier : "))
    nom = input("Nouveau nom de l'animal : ")
    race = input("Nouvelle race de l'animal : ")
    cage_id = int(input("Nouvel ID de la cage : "))
    date_naissance = input("Nouvelle date de naissance (YYYY-MM-DD) : ")
    pays_origine = input("Nouveau pays d'origine : ")

    cursor.execute("UPDATE animal SET nom=%s, race=%s, cage_id=%s, date_naissance=%s, pays_origine=%s WHERE id=%s",
                   (nom, race, cage_id, date_naissance, pays_origine, animal_id))
    conn.commit()
    print("Animal modifié avec succès.")

def afficher_animaux():
    cursor.execute("SELECT * FROM animal")
    animaux = cursor.fetchall()
    if animaux:
        for animal in animaux:
            print(animal)
    else:
        print("Aucun animal dans le zoo.")

def afficher_animaux_cage():
    cage_id = int(input("ID de la cage : "))
    cursor.execute("SELECT * FROM animal WHERE cage_id=%s", (cage_id,))
    animaux = cursor.fetchall()
    if animaux:
        for animal in animaux:
            print(animal)
    else:
        print(f"Aucun animal dans la cage {cage_id}.")

def calculer_superficie_totale():
    cursor.execute("SELECT SUM(superficie) FROM cage")
    superficie_totale = cursor.fetchone()[0]
    print(f"Superficie totale de toutes les cages : {superficie_totale} m²")

# Interface utilisateur
while True:
    print("\nMenu:")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Modifier un animal")
    print("4. Afficher tous les animaux")
    print("5. Afficher les animaux dans une cage")
    print("6. Calculer la superficie totale des cages")
    print("7. Quitter")

    choix = input("Choisissez une option (1-7) : ")

    if choix == '1':
        ajouter_animal()
    elif choix == '2':
        supprimer_animal()
    elif choix == '3':
        modifier_animal()
    elif choix == '4':
        afficher_animaux()
    elif choix == '5':
        afficher_animaux_cage()
    elif choix == '6':
        calculer_superficie_totale()
    elif choix == '7':
        print("Programme terminé.")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")