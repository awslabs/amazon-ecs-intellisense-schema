# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import os
from src.traversal import construct_schema


def get_schema(reference, description, required, api):
    """
    Gets the JSON schema structure for the requested operation

    :param reference: the data containing the references from the operation request
    :param description: the data containing the description for each reference
    :param required: the required references from the operation request
    :param api: the api.json file read into JSON format
    :return: the JSON schema structure
    """
    schema = dict()
    schema['$schema'] = "http://json-schema.org/draft-07/schema#"
    schema['type'] = "object"
    schema['properties'] = {}
    schema['additionalProperties'] = False  # Error checks against misspellings or invalid parameters
    schema['required'] = required

    for refs_name, refs_value in reference.items():
        schema['properties'][refs_name] = {}
        schema['properties'][refs_name]['description'] = description[refs_name]
        construct_schema(refs_name, schema['properties'], api['shapes'][refs_value], api)
    return schema


def write_schema(schema, operation, file_path):
    """
    Writes to a file containing the JSON schema for the operation

    Example: write_schema(schema, 'RegisterTaskDefinitionRequest', file_path)
    :param schema: the JSON schema structure parsed from the api.json and docs.json files
    :param operation: the type of task the wants to use
    :param file_path: the file path were it writes the JSON schema
    """
    os.makedirs(file_path, exist_ok=True)
    with open(os.path.join(file_path, operation + '_schema.json'), 'w') as outfile:
        json.dump(schema, outfile, indent=4)
