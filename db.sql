-- Table Auteurs
CREATE TABLE auteurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    nationalite VARCHAR(50),
    date_naissance DATE
);

-- Table Livres  
CREATE TABLE livres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    auteur_id INT,
    genre VARCHAR(50),
    annee_publication INT,
    isbn VARCHAR(20),
    FOREIGN KEY (auteur_id) REFERENCES auteurs(id)
);

-- Données d'exemple
INSERT INTO auteurs (nom, nationalite, date_naissance) VALUES 
('Victor Hugo', 'Française', '1802-02-26'),
('George Orwell', 'Britannique', '1903-06-25'),
('J.K. Rowling', 'Britannique', '1965-07-31');

INSERT INTO livres (titre, auteur_id, genre, annee_publication, isbn) VALUES 
('Les Misérables', 1, 'Classique', 1862, '978-2013228434'),
('1984', 2, 'Science-Fiction', 1949, '978-2070368228'),
('Harry Potter à l école des sorciers', 3, 'Fantasy', 1997, '978-2070541270');



