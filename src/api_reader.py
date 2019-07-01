# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import os


def get_references(api, operation):
    """
    Gets the operation's references from api.json. Includes metadata such as required
    parameters needed for the schema

    Example: get_references(api, 'RegisterTaskDefinitionRequest')
    :param api: the api.json file read into JSON format
    :param operation: the type of task the user wants to use
    :return: all of the references, the required references
    """
    references = {}
    required = []

    if 'required' in api['shapes'][operation]:
        required.extend(api['shapes'][operation]['required'])

    if 'members' in api['shapes'][operation]:
        for member in api['shapes'][operation]['members']:
            references[member] = api['shapes'][operation]['members'][member]['shape']

    return references, required


def write_references(refs, operation, file_path):
    """
    Writes to a file containing the references

    Example: write_references(reference, 'RegisterTaskDefinitionRequest', json_file_path)
    :param refs: the references we received from parsing the api.json
    :param operation: the type of task the user wants to use
    :param file_path: the file path where it writes the task definitions parameters
    """
    os.makedirs(file_path, exist_ok=True)
    with open(os.path.join(file_path, operation + '_refs.json'), 'w') as outfile:
        json.dump(refs, outfile, indent=4)
