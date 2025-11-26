from fastapi import FastAPI, HTTPException, status
import mysql.connector
from typing import List, Dict, Any
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="API Bibliothèque")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèles Pydantic
class AuteurCreate(BaseModel):
    nom: str
    nationalite: str
    date_naissance: date

class LivreCreate(BaseModel):
    titre: str
    auteur_id: int
    genre: str
    annee_publication: int
    isbn: str

# Connexion DB
def db_get():
    return mysql.connector.connect(
        host="mysql-math-educ-zonantenainasecondraymond-9b74.j.aivencloud.com",
        port=12706,
        user="avnadmin",
        password="AVNS_F4tkvhaLIHxULm3dcZ1",
        database="api_js2",
        ssl_ca="ca.pem"
    )

@app.get('/')
async def root():
    return {"message": "API Bibliothèque"}

# === CRUD AUTEURS ===
@app.post("/auteurs/", status_code=201)
async def create_auteur(auteur: AuteurCreate):
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    
    query = "INSERT INTO auteurs (nom, nationalite, date_naissance) VALUES (%s, %s, %s)"
    cursor.execute(query, (auteur.nom, auteur.nationalite, auteur.date_naissance))
    conn.commit()
    auteur_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    return {"id": auteur_id, "message": "Auteur créé"}

@app.get("/auteurs/")
async def get_all_auteurs():
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM auteurs")
    auteurs = cursor.fetchall()
    cursor.close()
    conn.close()
    return auteurs

@app.put("/auteurs/{auteur_id}")
async def update_auteur(auteur_id: int, auteur: AuteurCreate):
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    
    query = "UPDATE auteurs SET nom=%s, nationalite=%s, date_naissance=%s WHERE id=%s"
    cursor.execute(query, (auteur.nom, auteur.nationalite, auteur.date_naissance, auteur_id))
    conn.commit()
    
    cursor.close()
    conn.close()
    return {"message": "Auteur modifié"}

@app.delete("/auteurs/{auteur_id}")
async def delete_auteur(auteur_id: int):
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM auteurs WHERE id=%s", (auteur_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Auteur supprimé"}

# === CRUD LIVRES ===
@app.post("/livres/", status_code=201)
async def create_livre(livre: LivreCreate):
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    
    query = """INSERT INTO livres (titre, auteur_id, genre, annee_publication, isbn) 
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (livre.titre, livre.auteur_id, livre.genre, livre.annee_publication, livre.isbn))
    conn.commit()
    livre_id = cursor.lastrowid
    
    cursor.close()
    conn.close()
    return {"id": livre_id, "message": "Livre créé"}

@app.get("/livres/")
async def get_all_livres():
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT l.*, a.nom as auteur_nom 
        FROM livres l 
        JOIN auteurs a ON l.auteur_id = a.id
    """)
    livres = cursor.fetchall()
    cursor.close()
    conn.close()
    return livres

@app.put("/livres/{livre_id}")
async def update_livre(livre_id: int, livre: LivreCreate):
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    
    query = """UPDATE livres SET titre=%s, auteur_id=%s, genre=%s, 
               annee_publication=%s, isbn=%s WHERE id=%s"""
    cursor.execute(query, (livre.titre, livre.auteur_id, livre.genre, livre.annee_publication, livre.isbn, livre_id))
    conn.commit()
    
    cursor.close()
    conn.close()
    return {"message": "Livre modifié"}

@app.delete("/livres/{livre_id}")
async def delete_livre(livre_id: int):
    conn = db_get()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM livres WHERE id=%s", (livre_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Livre supprimé"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)