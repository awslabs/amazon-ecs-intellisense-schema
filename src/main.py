import os, json
from api_reader import *

json_file_path = os.path.join(os.path.dirname(__file__), "JSON_files")
api_file = os.path.join(json_file_path, "api.json")
api = json.load(open(api_file))

construct, required = get_task_def(api, 'shapes', 'RegisterTaskDefinitionRequest')
write_task_def(construct, json_file_path)

