import json
import os


class Log:
    def settings():
        # Définition du chemin du fichier config.json dans le répertoire racine
        project_root = os.path.dirname(os.path.abspath(__file__))  # Répertoire courant du fichier
        config_path = os.path.join(project_root, "../config.json")

        # Vérification de l'existence du fichier config.json
        if not os.path.exists(config_path):
            raise FileNotFoundError(
                f"Le fichier de configuration config.json est introuvable à l'emplacement suivant : {config_path}")

        # Lecture du contenu du fichier config.json
        try:
            with open(config_path, 'r', encoding="utf-8") as config_file:
                config = json.load(config_file)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON invalide dans le fichier de configuration : {e}")

        config = json.load(open("../config.json", 'r', encoding="utf-8"))
        host = config["database-host"]
        port = config["database-port"]
        database = config["database-name"]
        user = config["database-user"]
        password = config["database-password"]
        return {
            "host": host,
            "port": port,
            "database": database,
            "user": user,
            "password": password
        }