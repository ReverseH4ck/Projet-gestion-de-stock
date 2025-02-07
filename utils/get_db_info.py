import json
import os


class Log:
    @staticmethod
    def settings():
        # Dynamically resolve the path to config.json in the root folder
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        config_path = os.path.join(root_dir, "config.json")

        # Check if the config.json file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(
                f"Le fichier de configuration config.json est introuvable à l'emplacement : {config_path}"
            )

        # Read the content of config.json
        try:
            with open(config_path, 'r', encoding="utf-8") as config_file:
                config = json.load(config_file)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON invalide dans le fichier config.json : {e}")

        # Fetch and return the required fields
        try:
            return {
                "host": config["database-host"],
                "port": config["database-port"],
                "database": config["database-name"],
                "user": config["database-user"],
                "password": config["database-password"],
            }
        except KeyError as e:
            raise KeyError(f"Clé manquante dans le fichier config.json : {e}")
