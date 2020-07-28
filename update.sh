#!/bin/bash

SCHEMA_VERSION=$1
SDK_VERSION=$2

if [ -z $1 ]; then
	echo "Error: Schema version is empty" && exit
fi

if [ -z $2 ]; then
	echo "Error: SDK version is empty" && exit
fi

cd src/model

API_URL=https://raw.githubusercontent.com/aws/aws-sdk-go/master/models/apis/ecs/2014-11-13/api-2.json
DOCS_URL=https://raw.githubusercontent.com/aws/aws-sdk-go/master/models/apis/ecs/2014-11-13/docs-2.json

curl $API_URL > api.json
curl $DOCS_URL > docs.json

cd ..

(cat > version.py)<<EOF
# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""
See the most recent version number for AWS SDK Go here:
https://github.com/aws/aws-sdk-go/releases
"""
schema_version = '${SCHEMA_VERSION}'
sdk_go_version = '${SDK_VERSION}'
EOF
