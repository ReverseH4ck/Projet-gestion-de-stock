## 📦 Installation

1. **Cloner le dépôt**  
   Clonez ce dépôt GitHub en local :  

   ```bash
   git clone https://github.com//ReverseH4ck/Projet-gestion-de-stock.git
   cd Projet-gestion-de-stock
   ```

2. **Installer les dépendances**  
   Assurez-vous d'avoir Python 3 installé sur votre machine, puis installez les packages nécessaires avec `pip` :

   ```bash
   pip install mysql mysql-connector-python
   ```

---

## 🔑 Configuration

Pour connecter votre application à la base de données MySQL, vous devrez récupérer le fichier `config.json`. Ce fichier contient les informations de connexion à la base de données.

### Étapes pour obtenir `config.json` :
1. Rendez-vous sur le Discord du projet.
2. Allez dans le salon **#database**.
3. Téléchargez le fichier `config.json` mis à disposition.

Une fois téléchargé, placez le fichier à la racine du projet.

---

## 🐈️ Utilisation

Exécutez le script principal pour démarrer l'application :

```bash
python main.py
```

Testez la connection à la base de données :

```bash
python utils/db_connection.py
```

---

## 📚 Dépendances utilisées

- **[mysql](https://pypi.org/project/mysql/)** : Utilisé pour interagir avec les bases de données MySQL.  
- **[mysql-connector-python](https://pypi.org/project/mysql-connector-python/)** : Fournit un connecteur natif pour MySQL compatible avec Python.

---
