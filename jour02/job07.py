import mysql.connector

class Employe:
    def __init__(self, host="localhost", user="root", password="azerty", database="landou"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employe (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                prenom VARCHAR(255) NOT NULL,
                salaire DECIMAL(10, 2) NOT NULL
            )
        ''')
        self.conn.commit()

    def ajouter_employe(self, nom, prenom, salaire):
        query = '''
            INSERT INTO employe (nom, prenom, salaire)
            VALUES (%s, %s, %s)
        '''
        values = (nom, prenom, salaire)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_employes(self):
        self.cursor.execute('SELECT * FROM employe')
        employes = self.cursor.fetchall()
        for employe in employes:
            print(employe)

    def mettre_a_jour_salaire(self, employe_id, nouveau_salaire):
        query = '''
            UPDATE employe
            SET salaire = %s
            WHERE id = %s
        '''
        values = (nouveau_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_employe(self, employe_id):
        query = 'DELETE FROM employe WHERE id = %s'
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# Exemple d'utilisation
entreprise = Employe()

entreprise.ajouter_employe("Doe", "John", 1500)
entreprise.ajouter_employe("Smith", "Jane", 3500)

print("Avant la mise à jour du salaire :")
entreprise.afficher_employes()

entreprise.mettre_a_jour_salaire(1, 1500)

print("Après la mise à jour du salaire :")
entreprise.afficher_employes()

entreprise.supprimer_employe(2)

print("Après la suppression d'un employé :")
entreprise.afficher_employes()
