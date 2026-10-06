# 1. DESCRIPTION DU PROJET

Le système de gestion de bibliothèque (*Library Management System*) est une application complète (backend et frontend) développée avec **Flask**, **SQLite**, l'authentification **JWT** et **Streamlit**.

Le projet permet aux administrateurs de gérer les livres de la bibliothèque et permet aux utilisateurs de parcourir, d'emprunter ou d'acheter des livres.

Le système a été conçu selon une architecture propre fondée sur des routes, des services, une couche de base de données, un module d'authentification et des fonctions utilitaires.

Le projet comprend également :

* Une API REST


* L'authentification JWT


* Une application en ligne de commande (console)


* Une interface web Streamlit


* Une base de données SQLite



---

## 2. OBJECTIFS DU PROJET

Les objectifs de ce projet sont :

* Apprendre le développement d'API REST avec Flask


* Appliquer les concepts d'architecture logicielle


* Mettre en œuvre l'authentification JWT


* Utiliser une base de données SQLite


* Réaliser les opérations CRUD


* Séparer la logique métier des routes


* Créer une interface utilisateur professionnelle avec Streamlit


* Créer une application console pour les tests



---

## 3. TECHNOLOGIES UTILISÉES

| Technologie | Rôle / Usage |
| --- | --- |
| **Python** | Langage de programmation principal

 |
| **Flask** | Backend pour l'API REST

 |
| **SQLite** | Base de données

 |
| **Flask-JWT-Extended** | Gestion de l'authentification

 |
| **Streamlit** | Interface utilisateur (Frontend)

 |
| **Requests** | Communication avec l'API

 |
| **Postman** | Tests de l'API

 |

---

## 4. ARCHITECTURE DU PROJET

Le projet suit une architecture en couches :

* **Couche Routes (*Routes Layer*) :** Gère les points d'accès (endpoints) de l'API et les requêtes HTTP.


* **Couche Services (*Services Layer*) :** Contient la logique métier de l'application.


* **Couche Base de données (*Database Layer*) :** Gère la connexion à la base de données SQLite et la création des tables.


* **Couche Authentification (*Authentication Layer*) :** Gère l'authentification JWT et les autorisations.


* **Couche Utilitaires (*Utils Layer*) :** Contient les fonctions de validation et les utilitaires réutilisables.


* **Couche Frontend (*Frontend Layer*) :** Implémentée avec Streamlit pour l'interaction utilisateur.



---

## 5. STRUCTURE DU PROJET

```text
library_management_system/
│
├── app.py
├── database/
├── routes/
├── services/
├── auth/
├── utils/
├── models/
├── console_app/
└── streamlit_app/
```[cite: 4]

---

## 6. CONCEPTION DE LA BASE DE DONNÉES

### TABLE `USERS` (Utilisateurs)
* `id` (INTEGER, Clé primaire)[cite: 4]
* `username` (TEXT)[cite: 4]
* `password` (TEXT, Haché)[cite: 4]
* `role` (TEXT, ex. `admin`, `user`)[cite: 4]

### TABLE `BOOKS` (Livres)
* `id` (INTEGER, Clé primaire)[cite: 5]
* `title` (TEXT)[cite: 5]
* `author` (TEXT)[cite: 5]
* `description` (TEXT)[cite: 5]
* `available` (INTEGER / BOOLEAN)[cite: 5]

### TABLE `BORROWINGS` (Emprunts & Achats)
* `id` (INTEGER, Clé primaire)[cite: 5]
* `user_id` (INTEGER, Clé étrangère)[cite: 5]
* `book_id` (INTEGER, Clé étrangère)[cite: 5]
* `action_type` (TEXT, ex. `borrow`, `buy`)[cite: 5]
* `action_date` (DATETIME / TEXT)[cite: 5]

---

## 7. POINTS D'ACCÈS DE L'API (ENDPOINTS)

### ROUTES AUTHENTIFICATION
| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/auth/register` | Inscription d'un utilisateur[cite: 6] |
| **POST** | `/auth/login` | Connexion d'un utilisateur[cite: 6] |

### ROUTES LIVRES
| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/books/` | Obtenir tous les livres[cite: 6] |
| **POST** | `/books/` | Ajouter un livre[cite: 6] |
| **PUT** | `/books/{id}` | Mettre à jour un livre[cite: 6] |
| **DELETE** | `/books/delete-by-name/{title}` | Supprimer un livre[cite: 6] |

### ROUTES EMPRUNTS / ACHATS
| Méthode | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/borrow/borrow/{id}` | Emprunter un livre[cite: 6] |
| **POST** | `/borrow/buy/{id}` | Acheter un livre[cite: 6] |

---

## 8. SYSTÈME D'AUTHENTIFICATION
L'application utilise l'authentification par jeton JWT[cite: 7]. Lorsqu'un utilisateur se connecte avec succès, le serveur génère un jeton JWT qui est ensuite utilisé pour accéder aux routes protégées[cite: 7].

* **Les administrateurs peuvent :** Ajouter, mettre à jour et supprimer des livres[cite: 7].
* **Les utilisateurs normaux peuvent :** Consulter, emprunter et acheter des livres[cite: 7].

---

## 9. APPLICATION CONSOLE
Une application en ligne de commande a été développée afin de tester le système backend[cite: 7].

Cette application console permet :
* L'inscription[cite: 7]
* La connexion[cite: 7]
* La visualisation des livres[cite: 7]
* L'emprunt de livres[cite: 7]
* L'achat de livres ainsi que les opérations de gestion réservées aux administrateurs[cite: 7]

---

## 10. INTERFACE FRONTEND STREAMLIT
Une interface utilisateur professionnelle a été développée avec Streamlit[cite: 8].

**Fonctionnalités :**
* Page de connexion / inscription[cite: 8]
* Tableau de bord administrateur[cite: 8]
* Tableau de bord utilisateur[cite: 8]
* Gestion des livres[cite: 8]
* Fonctionnalités d'emprunt et d'achat[cite: 8]
* Mises à jour en temps réel de la base de données[cite: 8]

---

## 11. INSTRUCTIONS D'EXÉCUTION DU PROJET

1. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```[cite: 10]

2. **Lancer le backend Flask :**
   ```bash
   python app.py
   ```[cite: 10]

3. **Lancer le frontend Streamlit :**
   ```bash
   streamlit run streamlit_app/app.py
   ```[cite: 10]

4. **Lancer l'application console :**
   ```bash
   python console_app/main.py
   ```[cite: 10]

---

## CONCLUSION
Ce projet nous a permis de comprendre et d'appliquer les concepts d'architecture logicielle en utilisant Flask et SQLite[cite: 12].

Nous avons mis en œuvre :
* Des API REST[cite: 12]
* L'authentification JWT[cite: 12]
* Les opérations CRUD[cite: 12]
* La persistance des données[cite: 12]
* Des interfaces en console et web[cite: 12]

Le projet démontre une architecture backend propre, modulaire et évolutive[cite: 12].

```