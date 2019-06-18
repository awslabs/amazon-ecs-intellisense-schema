import json
import os


def get_task_def(api, shapes, action):
    """
    Gets the task definition parameters from api.json. Includes metadata such as required
    parameters needed for the schema
    :param api: the api.json file parsed into JSON format
    :param shapes: the key value inside api.json where our constructs is located
    :param action: the type of the task the user wants to use for their needs
    :return: all of the task definitions, the required task definitions
    """
    task_def = {}
    req = []

    for req_elements in api[shapes][action]['required']:
        req.append(req_elements)

    for param in api[shapes][action]['members']:
        task_def[param] = api[shapes][action]['members'][param]['shape']

    return task_def, req


def write_task_def(construct, file_path):
    """
    Writes to a file containing the task definition parameters
    :param file_path: the file path to where we want to write our task definitions parameters
    :param construct: the data we received from parsing the api.json
    """
    with open(os.path.join(file_path, 'ECS_task_def.json'), 'w') as outfile:
        json.dump(construct, outfile, indent=4)
