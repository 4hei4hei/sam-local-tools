#!/bin/bash

set -eo pipefail

poetry run aws dynamodb delete-table --table-name local-table --endpoint-url http://localhost:8000
rm -r ./resource/data/*
docker-compose stop
