import boto3
import datetime
import json
import os
from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

local_flag = os.getenv("LOCAL_FLAG")
table_name = os.getenv("TABLE_NAME")

if local_flag:
    dynamodb = boto3.resource("dynamodb", endpoint_url="http://dynamodb-local:8000")
    table_name = "local-table"
else:
    dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    if "ID" in event["headers"] or "id" in event["headers"]:
        id = str(event["headers"]["ID"])
    else:
        logger.info("Specific header is not found. Default value is set.")
        id = "1"

    item = {
        "ID": id,
        "Time": str(datetime.datetime.now()),
    }
    resp = table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "put item",
            }
        ),
    }
