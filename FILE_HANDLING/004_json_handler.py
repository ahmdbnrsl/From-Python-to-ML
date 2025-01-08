import json

data = {
    "nama": "Ahmad",
    "usia": 25,
    "hobi": ["coding", "painting"]
}

with open('./file/data.json', 'w') as file:
    json.dump(data, file)

with open('./file/data.json', 'r') as file:
    data = json.load(file)
    print(data)