# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0


def get_members(api, operation):
    """
    Gets the operation's members from api.json. Includes metadata such as required
    parameters needed for the schema.

    Example: get_members(api, 'RegisterTaskDefinitionRequest')
    :param api: the api.json file read into JSON format
    :param operation: the type of task the user wants to use
    :return: all of the references, the required references
    """
    members = {}
    required = []

    if 'required' in api['shapes'][operation]:
        required.extend(api['shapes'][operation]['required'])

    if 'members' in api['shapes'][operation]:
        for member in api['shapes'][operation]['members']:
            members[member] = api['shapes'][operation]['members'][member]['shape']

    return members, required
