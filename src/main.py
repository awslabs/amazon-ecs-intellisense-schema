# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import os
import sys
import json
from src.api_reader import get_members
from src.intellisense import IntellisenseSchema


if __name__ == '__main__':
    model_dir = os.path.join(os.path.dirname(__file__), "model")

    api_file = os.path.join(model_dir, "api.json")
    api = json.load(open(api_file))

    doc_file = os.path.join(model_dir, "docs.json")
    doc = json.load(open(doc_file))

    operation = 'RegisterTaskDefinitionRequest'
    if operation not in api['shapes']:
        sys.exit('Operation "{op}" not found under "shapes"'.format(op=operation))

    reference, required = get_members(api, operation)
    intellisense = IntellisenseSchema(api, doc)
    schema = intellisense.build(reference, required, operation)

    schema_dir = os.path.join(model_dir, "schema")
    intellisense.write(schema_dir, schema)
