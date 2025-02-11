import configparser
from ctypes import resize
from doctest import debug
import json
import os 
from flask import Flask, jsonify

app = Flask(__name__)

def load_config(config_file):
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        return {"error": f"Configuration file '{config_file}' not found."}

    try:

        config.read(config_file)
        configdata = {section: dict(config.items(section)) for section in config.sections()}
        return configdata
    except FileNotFoundError as e:
        return {"Error" : e}
    except configparser.Error as e:
        return {"error": f"Error reading configuration file: {str(e)}"}
def savetomongodb(result):
    client = MongoClient("your-connection-string-of-mongodb")
    db = client["databasename"]
    collection = db["collectionname"]
    with open(r"path\to\output.json", "r", encoding="utf-8") as file:
        data = json.load(file)  
    if isinstance(data, list):
        collection.insert_many(data)  
    else:
        collection.insert_one(data)

@app.route('/config', methods=['GET'])
def get_config():
    config_file = r"path\to\read\config.ini"
    result = load_config(config_file)
    if result:
        with open(r"path\to\write\config_output.json", "w") as f:
            json.dump(result, f, indent=4)
        return jsonify(result)

if __name__ == "__main__":
    app.run(debug = True)

