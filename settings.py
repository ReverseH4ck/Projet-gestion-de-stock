import json
class Log:
  def settings():
    config = json.load(open("config.json", 'r', encoding="utf-8"))
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