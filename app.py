from os import environ
from sys import argv

from flask import Flask


# 1. Config
config = {
    "greeting": environ.get("GREETING", "Hello World")
}


# 2. App
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return config["greeting"]


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
