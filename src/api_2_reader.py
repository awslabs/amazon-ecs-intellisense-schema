import json
import os

cur_path = os.path.dirname(__file__)
path = os.path.join(cur_path, "JSON_files/api-2.json")
api_file = open(path)
api = json.load(api_file)

req = []
typeSet = set()


def get_task_def(s, action):
    task_def = {}
    for mem in api[s][action]:
        if mem == 'required':
            for r in api[s][action][mem]:
                req.append(r)

        if mem == 'members':
            for k in api[s][action][mem]:
                task_def[k] = api[s][action][mem][k]['shape']
                typeSet.add(api[s][action][mem][k]['shape'])

    return task_def


def write_task_def(construct):
    with open(os.path.join('JSON_files', 'ECS_task_def.json'), 'w') as outfile:
        json.dump(construct, outfile, indent=4, sort_keys=4)
