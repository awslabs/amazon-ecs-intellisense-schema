# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

restricted_types = {
   'max': 'maxLength',
   'min': 'minLength',
   'integer': 'integer',
   'enum': 'enum',
   'pattern': 'pattern',
}


def construct_schema(current, schema, construct, api):
    """
    Does a DFS traversal to explore every construct in each reference and appends the data to the
    JSON schema structure

    :param current: the key in the schema we are appending the data to
    :param schema: the current structure that will be our JSON schema
    :param construct: the construct we are accessing inside the api.json
    :param api: the api.json file read into JSON format
    """
    new_field = ''

    for element in construct:
        if element in restricted_types:
            schema[current][restricted_types[element]] = construct[element]

        if 'required' in construct:
            schema[current]['required'] = construct['required']

        if 'type' in construct:
            if construct['type'] == 'list':
                schema[current]['type'] = 'array'
                schema[current]['items'] = {}
                new_field = 'items'
                schema[current]['additionalProperties'] = False
            elif construct['type'] == 'structure':
                schema[current]['type'] = 'object'
                schema[current]['properties'] = {}
                new_field = 'properties'
                schema[current]['additionalProperties'] = False
            elif construct['type'] == 'map':
                schema[current]['type'] = 'object'
                schema[current]['properties'] = {}
                schema[current]['properties']['keyName'] = {"type": "string"}
            else:
                schema[current]['type'] = construct['type']

        if 'member' in construct:
            construct_schema(new_field, schema[current], api['shapes'][construct['member']['shape']], api)

        if 'members' in construct:
            for member in construct['members']:
                schema[current][new_field][member] = {}
                construct_schema(member, schema[current][new_field],
                                 api['shapes'][construct['members'][member]['shape']], api)
