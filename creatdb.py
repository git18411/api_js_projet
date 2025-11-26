import mysql.connector

def ex():
    connection = None
    cursor = None
    
    try:
        # Connexion à la base de données "math_educ"
        connection = mysql.connector.connect(
            host="mysql-math-educ-zonantenainasecondraymond-9b74.j.aivencloud.com",
            port=12706,
            user="avnadmin",
            password="AVNS_F4tkvhaLIHxULm3dcZ1",
            database="api_js2",
            ssl_ca="ca.pem"
        )
        
        cursor = connection.cursor()
        print('✅ Connexion à la base de données "api_js" réussie!')
        
        # Création de la table admin
        query = """
CREATE TABLE livres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    auteur_id INT,
    genre VARCHAR(50),
    annee_publication INT,
    isbn VARCHAR(20),
    FOREIGN KEY (auteur_id) REFERENCES auteurs(id)
);
        """
        cursor.execute(query)
        connection.commit()
        print("📌 Table 'utulisateur' créée (ou déjà existante).")


    except mysql.connector.Error as e:
        print(f"❌ Erreur MySQL: {e}")
        
    except Exception as e:
        print(f"❌ Erreur générale: {e}")
        
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print('\n🔌 Connexion fermée.')

ex()
