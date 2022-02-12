#!/bin/bash

set -eo pipefail

poetry run aws dynamodb delete-table --table-name local-table --endpoint-url http://localhost:8000
docker-compose stop
