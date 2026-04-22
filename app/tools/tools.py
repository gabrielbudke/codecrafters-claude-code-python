import json

def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as file:
        schema = json.load(file)      
        print(f"> Loaded schema from {schema_path}: {schema}")  
    return schema


read_file_schema = load_schema("tools/schema/read_file.json")
write_file_schema = load_schema("tools/schema/write_file.json")
bash_schema = load_schema("tools/schema/bash.json")

print(write_file_schema)