# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import os
from bs4 import BeautifulSoup


def get_description(documentation, reference, operation):
    """
    Gets the description for each of the references from the doc.json

    Example: get_description(documentation, reference, 'RegisterTaskDefinitionRequest')
    :param documentation: the docs.json file read into JSON format
    :param reference: all of the references inside the requested operation
    :param operation: the type of task the user wants to to use for their needs
    :return: all of the description for each parameters in JSON structure
    """
    description = {}

    for key in reference.keys():
        refs_value = operation + "$" + key

        if documentation['shapes'][reference[key]]['refs'][refs_value] is None:
            description[key] = "No description currently available"
        else:
            anchor_tag_removal = documentation['shapes'][reference[key]]['refs'][refs_value]\
                .replace("<a href=\"", "").replace("\">", " ")
            soup = BeautifulSoup(anchor_tag_removal, 'lxml')
            description[key] = soup.get_text()
    return description


def write_description(description, operation, file_path):
    """
    Writes to a file containing the description for the operation's references

    Example: write_description(description, 'RegisterTaskDefinitionRequest', json_file_path)
    :param description: the data containing the description for each reference
    :param operation: the type of task the user wants to use
    :param file_path: the file path where it writes our description
    """
    os.makedirs(file_path, exist_ok=True)
    with open(os.path.join(file_path, operation + '_doc.json'), 'w') as outfile:
        json.dump(description, outfile, indent=4)
