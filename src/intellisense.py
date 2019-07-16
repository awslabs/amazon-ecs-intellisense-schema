# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import json
from src.sanitizer import sanitize


class IntellisenseSchema:

    """
    These types allows restriction on JSON values.

    See: https://cswr.github.io/JsonSchema/spec/basic_types/#restrictions
    """
    restricted_types = {
        'max': 'maxLength',
        'min': 'minLength',
        'integer': 'integer',
        'enum': 'enum',
        'pattern': 'pattern',
    }

    def __init__(self, api, doc):
        """
        Constructor for the Intellisense Schema class, to initialize the api and doc variables
        :param api: the api.json file
        :param doc: the doc.json file
        """
        self.api = api
        self.doc = doc

    def build(self, members, required, operation):
        """
        Builds the template for the schema and calls construct to complete the schema for the operation

        :param members: the members of the operation
        :param required: the required members for the operation
        :param operation: the task the user wants to use
        :return:
        """
        schema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {},
            "required": required,
            "additionalProperties": False,  # Error checks against misspellings or invalid parameters
        }

        for name, shape in members.items():
            doc_key = {  # See docs.json
                "shape_name": shape,
                "refs_parent": operation,
                "refs_member": name
            }
            schema['properties'][name] = {}
            schema['properties'][name]['description'] = sanitize(
                self.doc['shapes'][shape]['refs'][operation + '$' + name])

            self._construct(doc_key, schema['properties'], self.api['shapes'][shape])

        return schema

    def _construct(self, doc_key, schema, shape_value):
        """
        Does a DFS traversal to explore every construct in each reference and appends the data to the
        JSON schema structure

        Example of a construct inside a doc file:
        VolumeList: {
            refs: {
                RegisterTaskDefinitionRequest$volumes: "..."
            }
        }
        :param doc_key: A dictionary that contains three key/value pair.
        A shape key where the name of the key is the name of the construct of where the
        reference description is located inside the doc file.
        A construct key, needed to keep track of the current's parent for the doc file.
        A refs key, the value of the key is the current schema construct we are building
        :param schema: the current structure that will be our JSON schema
        :param shape_value: the construct we are accessing inside the api.json
        """
        new_field = ''

        refs_value = doc_key['shape_name']
        parent = doc_key['refs_parent']
        current = doc_key['refs_member']

        for element in shape_value:
            if element in self.restricted_types:
                schema[current][self.restricted_types[element]] = shape_value[element]
            if element not in shape_value:
                continue
            if element == 'required':
                schema[current]['required'] = shape_value['required']
            elif element == 'type':
                if shape_value['type'] == 'list':
                    schema[current]['type'] = 'array'
                    schema[current]['items'] = {}
                    new_field = 'items'
                    schema[current]['additionalProperties'] = False
                elif shape_value['type'] == 'structure':
                    schema[current]['type'] = 'object'
                    schema[current]['properties'] = {}
                    new_field = 'properties'
                    schema[current]['additionalProperties'] = False
                elif shape_value['type'] == 'map':
                    schema[current]['type'] = 'object'
                    schema[current]['properties'] = {}
                    schema[current]['properties']['keyName'] = {"type": "string"}
                    schema[current]['description'] = sanitize(self.doc['shapes']
                                                               [refs_value]['refs'][parent+'$'+current])
                else:
                    schema[current]['type'] = shape_value['type']
            elif element == 'member':
                doc_key = {
                    "shape_name": shape_value['member'].get('shape'),
                    "refs_parent": refs_value,
                    "refs_member": new_field
                }

                self._construct(doc_key, schema[current], self.api['shapes'][shape_value['member']['shape']])
            elif element == 'members':
                for member in shape_value['members']:
                    schema[current][new_field][member] = {}
                    schema[current][new_field][member]['description'] = sanitize(
                        self.doc['shapes'][shape_value['members'][member]['shape']]['refs'][refs_value + '$' + member])

                    doc_key = {
                        "shape_name": shape_value['members'][member]['shape'],
                        "refs_parent": refs_value,
                        "refs_member": member
                    }

                    self._construct(doc_key, schema[current][new_field],
                                    self.api['shapes'][shape_value['members'][member]['shape']])

    def write(self, dir_path, schema, file_name='schema.json'):
        """
        Writes to a file containing the JSON schema for the operation

        Example: write_schema(schema, 'RegisterTaskDefinitionRequest', file_path)
        :param dir_path: the file path were it writes the JSON schema
        :param schema: the JSON schema structure parsed from the api.json and docs.json files
        :param file_name: the name of the schema file
        """
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(dir_path, file_name), 'w') as outfile:
            json.dump(schema, outfile, indent=4)
