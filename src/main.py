# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import json
import os
import sys
from src.api_reader import get_references, write_references
from src.docs_reader import get_description, write_description

json_file_path = os.path.join(os.path.dirname(__file__), "JSON_files")
api_file = os.path.join(json_file_path, "api.json")
api = json.load(open(api_file))
doc_file = os.path.join(json_file_path, "docs.json")
documentation = json.load(open(doc_file))

operation = 'RegisterTaskDefinitionRequest'

if operation not in api['shapes']:
    sys.exit('Operation "{op}" not found under "shapes"'.format(op=operation))


reference, required = get_references(api, operation)
write_references(reference, operation, json_file_path)

description = get_description(documentation, reference, operation)
write_description(description, operation, json_file_path)
