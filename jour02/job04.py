import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="azerty",
    database="laplateforme",
)


cursor = connexion.cursor()

requete = "SELECT nom, capacite FROM salle"
cursor.execute(requete)

resultats = cursor.fetchall()

for resultat in resultats:
    print(f"nom:{resultat[0]}, capacite: {resultat[1]}")


cursor.close()
connexion.close()