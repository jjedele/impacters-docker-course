from os import environ
from sys import argv

from flask import Flask
import redis


# 1. Config
config = {
    "greeting": environ.get("GREETING", "Hello World"),
    "redis_url": environ.get("REDIS_URL", "redis://localhost:6379")
}


# 2. App
app = Flask(__name__)
redis_client = redis.from_url(config["redis_url"])

@app.route("/", methods=["GET"])
def index():
    visited = redis_client.incr("visit_counter")
    response = config["greeting"] + "\n"
    response += f"I've been visited {visited} times."
    return response


# 3. Entry Point
if __name__ == "__main__":
    if len(argv) <= 1:
        raise Exception("At least 1 argument required.")

    command = argv[1]

    if command == "serve":
        app.run("0.0.0.0", 8000)
    elif command == "print_config":
        print("Config test:")
        print(config)
    else:
        raise Exception(f"Unsupported command: {command}")
