#!/bin/bash

set -eo pipefail

docker-compose up -d --build
poetry run aws dynamodb create-table --table-name local-table\
    --attribute-definitions AttributeName=Name,AttributeType=S\
    --key-schema AttributeName=Name,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --endpoint-url http://localhost:8000
